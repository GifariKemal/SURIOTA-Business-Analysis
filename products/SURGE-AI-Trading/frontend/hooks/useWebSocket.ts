/**
 * SURGE-AI Trading Dashboard - WebSocket Hook
 * Manages real-time connection to the backend
 */
'use client';

import { useEffect, useRef, useCallback, useState } from 'react';
import { useTradingStore } from '@/store/tradingStore';
import type {
  PriceData,
  Signal,
  TradeRecommendation,
  Position,
  Balance,
  RiskMetrics,
  TradeResult,
  WSEventType,
} from '@/types';

const WS_URL = process.env.NEXT_PUBLIC_WS_URL || 'ws://localhost:8000/ws';

interface UseWebSocketOptions {
  autoConnect?: boolean;
  reconnectInterval?: number;
  maxReconnectAttempts?: number;
}

interface UseWebSocketReturn {
  isConnected: boolean;
  connect: () => void;
  disconnect: () => void;
  sendMessage: (event: string, data: unknown) => void;
  refreshSignal: () => void;
  executeTrade: (action: string, symbol: string, quantity: number, stopLoss?: number, takeProfit?: number) => void;
}

export function useWebSocket(options: UseWebSocketOptions = {}): UseWebSocketReturn {
  const {
    autoConnect = true,
    reconnectInterval = 3000,
    maxReconnectAttempts = 10,
  } = options;

  const ws = useRef<WebSocket | null>(null);
  const reconnectAttempts = useRef(0);
  const reconnectTimer = useRef<NodeJS.Timeout | null>(null);

  const [isConnected, setIsConnected] = useState(false);

  const {
    setConnected,
    setPrice,
    setSignal,
    setRecommendation,
    setPosition,
    setBalance,
    setRisk,
    addActivity,
    setError,
  } = useTradingStore();

  // Handle incoming WebSocket messages
  const handleMessage = useCallback(
    (event: MessageEvent) => {
      try {
        const message = JSON.parse(event.data);
        const { event: eventType, data, timestamp } = message as {
          event: WSEventType;
          data: unknown;
          timestamp: string;
        };

        switch (eventType) {
          case 'price_update':
            setPrice(data as PriceData);
            break;

          case 'signal_update':
            const signal = data as Signal;
            setSignal(signal);

            // Add activity for new signals
            if (signal.is_actionable) {
              addActivity({
                type: 'signal',
                timestamp: signal.timestamp,
                title: `${signal.direction} Signal (${signal.confidence.toFixed(1)}% confidence)`,
                description: `New ${signal.direction} signal generated`,
                signal,
                details: [
                  `ML: ${signal.reasoning.ml_reason}`,
                  `DB: ${signal.reasoning.db_reason}`,
                  `Sentiment: ${signal.reasoning.sentiment_reason}`,
                ],
                is_expanded: false,
              });
            }
            break;

          case 'recommendation_update':
            setRecommendation(data as TradeRecommendation);
            break;

          case 'position_update':
            setPosition(data as Position);
            break;

          case 'balance_update':
            setBalance(data as Balance);
            break;

          case 'risk_update':
            const risk = data as RiskMetrics;
            setRisk(risk);

            // Add activity for risk alerts
            if (risk.kill_switch_active) {
              addActivity({
                type: 'alert',
                timestamp: new Date().toISOString(),
                title: 'KILL SWITCH ACTIVATED',
                description: risk.kill_switch_reason || 'Risk limit exceeded',
                details: [`Reason: ${risk.kill_switch_reason}`],
                is_expanded: false,
              });
            }
            break;

          case 'trade_executed':
            const trade = data as TradeResult;
            addActivity({
              type: 'trade',
              timestamp: trade.timestamp,
              title: `Trade ${trade.success ? 'EXECUTED' : 'FAILED'}: ${trade.action} ${trade.symbol}`,
              description: trade.success
                ? `${trade.action} ${trade.quantity} @ $${trade.price.toFixed(2)}`
                : trade.error || 'Trade failed',
              trade,
              details: trade.success
                ? [
                    `Quantity: ${trade.quantity}`,
                    `Price: $${trade.price.toFixed(2)}`,
                    `Value: $${trade.total_value_usd.toFixed(2)}`,
                  ]
                : [trade.error || 'Unknown error'],
              is_expanded: false,
            });
            break;

          case 'error':
            const errorData = data as { message: string };
            setError(errorData.message);
            break;

          default:
            console.log('Unknown WebSocket event:', eventType, data);
        }
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
      }
    },
    [
      setPrice,
      setSignal,
      setRecommendation,
      setPosition,
      setBalance,
      setRisk,
      addActivity,
      setError,
    ]
  );

  // Connect to WebSocket
  const connect = useCallback(() => {
    if (ws.current?.readyState === WebSocket.OPEN) {
      return;
    }

    try {
      ws.current = new WebSocket(WS_URL);

      ws.current.onopen = () => {
        console.log('WebSocket connected');
        setIsConnected(true);
        setConnected(true);
        reconnectAttempts.current = 0;

        // Subscribe to all channels
        ws.current?.send(
          JSON.stringify({
            event: 'subscribe',
            data: { channels: ['price', 'signal', 'risk', 'trade'] },
          })
        );
      };

      ws.current.onmessage = handleMessage;

      ws.current.onclose = () => {
        console.log('WebSocket disconnected');
        setIsConnected(false);
        setConnected(false);

        // Attempt reconnection
        if (reconnectAttempts.current < maxReconnectAttempts) {
          reconnectTimer.current = setTimeout(() => {
            reconnectAttempts.current++;
            console.log(
              `Reconnecting... (${reconnectAttempts.current}/${maxReconnectAttempts})`
            );
            connect();
          }, reconnectInterval);
        }
      };

      ws.current.onerror = (error) => {
        console.error('WebSocket error:', error);
        setError('WebSocket connection error');
      };
    } catch (error) {
      console.error('Failed to create WebSocket:', error);
      setError('Failed to connect to server');
    }
  }, [
    handleMessage,
    setConnected,
    setError,
    reconnectInterval,
    maxReconnectAttempts,
  ]);

  // Disconnect from WebSocket
  const disconnect = useCallback(() => {
    if (reconnectTimer.current) {
      clearTimeout(reconnectTimer.current);
    }
    reconnectAttempts.current = maxReconnectAttempts; // Prevent reconnection
    ws.current?.close();
    setIsConnected(false);
    setConnected(false);
  }, [setConnected, maxReconnectAttempts]);

  // Send message to server
  const sendMessage = useCallback((event: string, data: unknown) => {
    if (ws.current?.readyState === WebSocket.OPEN) {
      ws.current.send(JSON.stringify({ event, data }));
    } else {
      console.warn('WebSocket not connected');
    }
  }, []);

  // Refresh signal
  const refreshSignal = useCallback(() => {
    sendMessage('refresh_signal', {});
  }, [sendMessage]);

  // Execute trade via WebSocket
  const executeTrade = useCallback(
    (
      action: string,
      symbol: string,
      quantity: number,
      stopLoss?: number,
      takeProfit?: number
    ) => {
      sendMessage('execute_trade', {
        action,
        symbol,
        quantity,
        stop_loss: stopLoss,
        take_profit: takeProfit,
      });
    },
    [sendMessage]
  );

  // Auto-connect on mount
  useEffect(() => {
    if (autoConnect) {
      connect();
    }

    return () => {
      if (reconnectTimer.current) {
        clearTimeout(reconnectTimer.current);
      }
      ws.current?.close();
    };
  }, [autoConnect, connect]);

  return {
    isConnected,
    connect,
    disconnect,
    sendMessage,
    refreshSignal,
    executeTrade,
  };
}
