'use client';

import { useEffect } from 'react';
import { Header } from '@/components/Header';
import { PriceTicker } from '@/components/PriceTicker';
import { SignalPanel } from '@/components/SignalPanel';
import { TradeRecommendation } from '@/components/TradeRecommendation';
import { RiskDashboard } from '@/components/RiskDashboard';
import { PerformanceChart } from '@/components/PerformanceChart';
import { ActivityFeed } from '@/components/ActivityFeed';
import { useWebSocket } from '@/hooks/useWebSocket';
import { useTradingStore } from '@/store/tradingStore';
import { api } from '@/lib/api';

export default function Dashboard() {
  const { isConnected, connect } = useWebSocket({ autoConnect: true });
  const {
    setPrice,
    setSignal,
    setRecommendation,
    setBalance,
    setRisk,
    setPosition,
    setLoading,
  } = useTradingStore();

  // Initial data fetch
  useEffect(() => {
    const fetchInitialData = async () => {
      setLoading(true);
      try {
        const [price, signal, recommendation, balance, risk, position] = await Promise.all([
          api.market.getPrice('BTCUSDT').catch(() => null),
          api.signals.getCurrent('BTCUSDT').catch(() => null),
          api.signals.getRecommendation('BTCUSDT').catch(() => null),
          api.trading.getBalance().catch(() => null),
          api.risk.getStatus().catch(() => null),
          api.trading.getPosition().catch(() => null),
        ]);

        if (price) setPrice(price);
        if (signal) setSignal(signal);
        if (recommendation) setRecommendation(recommendation);
        if (balance) setBalance(balance);
        if (risk) setRisk(risk);
        if (position) setPosition(position);
      } catch (error) {
        console.error('Failed to fetch initial data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchInitialData();
  }, [setPrice, setSignal, setRecommendation, setBalance, setRisk, setPosition, setLoading]);

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <Header />

      {/* Main Content */}
      <main className="container mx-auto px-4 py-6">
        {/* Top Stats Row */}
        <section className="mb-6">
          <PriceTicker />
        </section>

        {/* Main Dashboard Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Column - Signal & Trade */}
          <div className="lg:col-span-4 space-y-6">
            <SignalPanel />
            <TradeRecommendation />
          </div>

          {/* Middle Column - Charts & Risk */}
          <div className="lg:col-span-4 space-y-6">
            <PerformanceChart />
            <RiskDashboard />
          </div>

          {/* Right Column - Activity Feed */}
          <div className="lg:col-span-4">
            <ActivityFeed />
          </div>
        </div>

        {/* Footer */}
        <footer className="mt-8 pt-4 border-t border-border text-center text-sm text-text-muted">
          <p>
            SURGE-AI Trading Dashboard v1.0.0 | Semi-Autonomous Trading System
          </p>
          <p className="text-xs mt-1">
            {isConnected ? (
              <span className="text-success">● Connected to server</span>
            ) : (
              <span className="text-danger">● Disconnected - Attempting to reconnect...</span>
            )}
          </p>
        </footer>
      </main>
    </div>
  );
}
