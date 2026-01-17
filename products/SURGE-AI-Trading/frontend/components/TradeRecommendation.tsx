'use client';

import { useState } from 'react';
import {
  Wallet,
  ArrowUpCircle,
  ArrowDownCircle,
  ShieldAlert,
  Target,
  Loader2,
  CheckCircle2,
  XCircle,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { useTradingStore } from '@/store/tradingStore';
import { useWebSocket } from '@/hooks/useWebSocket';
import { formatUSD, formatIDR, formatCrypto, cn } from '@/lib/utils';
import { api } from '@/lib/api';

export function TradeRecommendation() {
  const { recommendation, risk } = useTradingStore();
  const { executeTrade } = useWebSocket();
  const [isExecuting, setIsExecuting] = useState(false);
  const [lastResult, setLastResult] = useState<'success' | 'error' | null>(null);

  const handleExecute = async () => {
    if (!recommendation?.is_executable || isExecuting) return;

    setIsExecuting(true);
    setLastResult(null);

    try {
      const result = await api.trading.executeTrade({
        action: recommendation.action,
        symbol: recommendation.symbol,
        quantity: recommendation.quantity_btc,
        stop_loss: recommendation.stop_loss_usd,
        take_profit: recommendation.take_profit_usd,
      });

      if (result.success) {
        setLastResult('success');
        // Also send via WebSocket for real-time update
        executeTrade(
          recommendation.action,
          recommendation.symbol,
          recommendation.quantity_btc,
          recommendation.stop_loss_usd,
          recommendation.take_profit_usd
        );
      } else {
        setLastResult('error');
      }
    } catch (error) {
      console.error('Trade execution failed:', error);
      setLastResult('error');
    } finally {
      setIsExecuting(false);
      // Clear result after 3 seconds
      setTimeout(() => setLastResult(null), 3000);
    }
  };

  if (!recommendation) {
    return (
      <Card className="animate-pulse">
        <CardHeader>
          <div className="h-5 bg-surface-light rounded w-40" />
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="h-12 bg-surface-light rounded" />
            <div className="grid grid-cols-2 gap-4">
              {[1, 2, 3, 4].map((i) => (
                <div key={i} className="h-16 bg-surface-light rounded" />
              ))}
            </div>
            <div className="h-12 bg-surface-light rounded" />
          </div>
        </CardContent>
      </Card>
    );
  }

  const { action, symbol, is_executable, blocked_reason } = recommendation;
  const isLong = action === 'BUY';
  const isShort = action === 'SELL';
  const isHold = action === 'HOLD';
  const killSwitchActive = risk?.kill_switch_active ?? false;

  return (
    <Card>
      <CardHeader className="pb-3">
        <CardTitle className="flex items-center gap-2">
          <Wallet className="h-5 w-5 text-primary" />
          Trade Recommendation
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Action Badge */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            {isLong && <ArrowUpCircle className="h-8 w-8 text-success" />}
            {isShort && <ArrowDownCircle className="h-8 w-8 text-danger" />}
            {isHold && <Target className="h-8 w-8 text-warning" />}
            <div>
              <Badge
                variant={isLong ? 'success' : isShort ? 'danger' : 'warning'}
                className="text-lg px-4 py-1"
              >
                {action} {symbol}
              </Badge>
            </div>
          </div>
          {!is_executable && (
            <Badge variant="outline" className="text-text-muted">
              Blocked
            </Badge>
          )}
        </div>

        {/* Price & Amount Details */}
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-surface-light rounded-lg p-3">
            <div className="text-xs text-text-muted mb-1">Price</div>
            <div className="font-mono font-bold text-white">
              {formatUSD(recommendation.price_usd)}
            </div>
            <div className="font-mono text-xs text-text-secondary">
              {formatIDR(recommendation.price_idr)}
            </div>
          </div>

          <div className="bg-surface-light rounded-lg p-3">
            <div className="text-xs text-text-muted mb-1">Amount</div>
            <div className="font-mono font-bold text-white">
              {formatCrypto(recommendation.quantity_btc)} BTC
            </div>
            <div className="font-mono text-xs text-text-secondary">
              {formatUSD(recommendation.quantity_usd)}
            </div>
          </div>

          <div className="bg-surface-light rounded-lg p-3">
            <div className="text-xs text-text-muted mb-1">Value (IDR)</div>
            <div className="font-mono font-bold text-white">
              {formatIDR(recommendation.quantity_idr)}
            </div>
          </div>

          <div className="bg-surface-light rounded-lg p-3">
            <div className="text-xs text-text-muted mb-1">Confidence</div>
            <div className="font-mono font-bold text-white">
              {recommendation.confidence.toFixed(1)}%
            </div>
          </div>
        </div>

        <Separator />

        {/* Stop Loss & Take Profit */}
        <div className="grid grid-cols-2 gap-4">
          <div>
            <div className="text-xs text-text-muted mb-1">Stop Loss</div>
            <div className="font-mono text-sm text-danger">
              {formatUSD(recommendation.stop_loss_usd)}
            </div>
            <div className="font-mono text-xs text-text-muted">
              {formatIDR(recommendation.stop_loss_idr)}
            </div>
          </div>
          <div>
            <div className="text-xs text-text-muted mb-1">Take Profit</div>
            <div className="font-mono text-sm text-success">
              {formatUSD(recommendation.take_profit_usd)}
            </div>
            <div className="font-mono text-xs text-text-muted">
              {formatIDR(recommendation.take_profit_idr)}
            </div>
          </div>
        </div>

        {/* Blocked Reason */}
        {blocked_reason && (
          <div className="flex items-start gap-2 bg-warning-bg text-warning rounded-lg p-3 text-sm">
            <ShieldAlert className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <span>{blocked_reason}</span>
          </div>
        )}

        {/* Kill Switch Warning */}
        {killSwitchActive && (
          <div className="flex items-start gap-2 bg-danger-bg text-danger rounded-lg p-3 text-sm">
            <ShieldAlert className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <span>Kill switch is active. Trading disabled.</span>
          </div>
        )}

        {/* Execute Button */}
        <Button
          onClick={handleExecute}
          disabled={!is_executable || isExecuting || killSwitchActive || isHold}
          className={cn(
            "w-full h-12 text-lg font-bold transition-all",
            is_executable && !killSwitchActive && !isHold
              ? isLong
                ? "bg-success hover:bg-success/90"
                : "bg-danger hover:bg-danger/90"
              : "opacity-50 cursor-not-allowed"
          )}
        >
          {isExecuting ? (
            <>
              <Loader2 className="h-5 w-5 mr-2 animate-spin" />
              Executing...
            </>
          ) : lastResult === 'success' ? (
            <>
              <CheckCircle2 className="h-5 w-5 mr-2" />
              Trade Executed!
            </>
          ) : lastResult === 'error' ? (
            <>
              <XCircle className="h-5 w-5 mr-2" />
              Trade Failed
            </>
          ) : (
            <>
              {isLong ? '🟢' : isShort ? '🔴' : '⚪'} EXECUTE {action}
            </>
          )}
        </Button>
      </CardContent>
    </Card>
  );
}
