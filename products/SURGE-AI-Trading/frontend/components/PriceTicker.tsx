'use client';

import { TrendingUp, TrendingDown, Minus } from 'lucide-react';
import { Card, CardContent } from '@/components/ui/card';
import { useTradingStore } from '@/store/tradingStore';
import { formatUSD, formatIDR, formatPercent, cn } from '@/lib/utils';

export function PriceTicker() {
  const { price, balance, risk } = useTradingStore();

  if (!price) {
    return (
      <div className="grid grid-cols-4 gap-4">
        {[1, 2, 3, 4].map((i) => (
          <Card key={i} className="animate-pulse">
            <CardContent className="p-4">
              <div className="h-4 bg-surface-light rounded w-20 mb-2" />
              <div className="h-8 bg-surface-light rounded w-32 mb-1" />
              <div className="h-4 bg-surface-light rounded w-24" />
            </CardContent>
          </Card>
        ))}
      </div>
    );
  }

  const change = price.change_24h_percent;
  const isPositive = change > 0;
  const isNegative = change < 0;

  // Simulated performance data
  const dailyPnl = 112.34;
  const dailyPnlPercent = 1.23;
  const winRate = 72.7;
  const wins = 16;
  const losses = 6;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {/* Price Card */}
      <Card className="relative overflow-hidden">
        <div className={cn(
          "absolute top-0 left-0 right-0 h-1",
          isPositive ? "bg-success" : isNegative ? "bg-danger" : "bg-warning"
        )} />
        <CardContent className="p-4">
          <div className="flex items-center justify-between mb-1">
            <span className="text-sm text-text-muted">{price.symbol}</span>
            <div className={cn(
              "flex items-center gap-1 text-sm font-medium",
              isPositive ? "text-success" : isNegative ? "text-danger" : "text-text-secondary"
            )}>
              {isPositive ? <TrendingUp className="h-3 w-3" /> :
               isNegative ? <TrendingDown className="h-3 w-3" /> :
               <Minus className="h-3 w-3" />}
              {formatPercent(change)}
            </div>
          </div>
          <div className="font-mono text-2xl font-bold text-white">
            {formatUSD(price.price_usd)}
          </div>
          <div className="font-mono text-sm text-text-secondary">
            {formatIDR(price.price_idr)}
          </div>
        </CardContent>
      </Card>

      {/* Portfolio Card */}
      <Card>
        <CardContent className="p-4">
          <div className="text-sm text-text-muted mb-1">Portfolio</div>
          <div className="font-mono text-2xl font-bold text-white">
            {formatUSD(balance?.total_usd ?? 9234.56)}
          </div>
          <div className="font-mono text-sm text-text-secondary">
            {formatIDR(balance?.total_idr ?? 147752960)}
          </div>
        </CardContent>
      </Card>

      {/* Daily P&L Card */}
      <Card>
        <CardContent className="p-4">
          <div className="text-sm text-text-muted mb-1">Daily P&L</div>
          <div className={cn(
            "font-mono text-2xl font-bold",
            dailyPnl >= 0 ? "text-success" : "text-danger"
          )}>
            {dailyPnl >= 0 ? '+' : ''}{formatUSD(dailyPnl)}
          </div>
          <div className={cn(
            "text-sm font-medium",
            dailyPnlPercent >= 0 ? "text-success" : "text-danger"
          )}>
            ({formatPercent(dailyPnlPercent)})
          </div>
        </CardContent>
      </Card>

      {/* Win Rate Card */}
      <Card>
        <CardContent className="p-4">
          <div className="text-sm text-text-muted mb-1">Win Rate</div>
          <div className="font-mono text-2xl font-bold text-white">
            {winRate.toFixed(1)}%
          </div>
          <div className="text-sm text-text-secondary">
            <span className="text-success">{wins}W</span>
            <span className="mx-1">/</span>
            <span className="text-danger">{losses}L</span>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
