'use client';

import { Shield, AlertTriangle, XOctagon, Activity } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { Button } from '@/components/ui/button';
import { useTradingStore } from '@/store/tradingStore';
import { cn, calcProgress, formatUSD } from '@/lib/utils';
import { api } from '@/lib/api';

export function RiskDashboard() {
  const { risk, position } = useTradingStore();

  const handleResetKillSwitch = async () => {
    try {
      await api.risk.resetKillSwitch();
    } catch (error) {
      console.error('Failed to reset kill switch:', error);
    }
  };

  if (!risk) {
    return (
      <Card className="animate-pulse">
        <CardHeader>
          <div className="h-5 bg-surface-light rounded w-36" />
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {[1, 2, 3, 4].map((i) => (
              <div key={i} className="h-12 bg-surface-light rounded" />
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  const {
    current_drawdown_percent,
    max_drawdown_percent,
    daily_loss_percent,
    daily_loss_limit_percent,
    current_exposure_percent,
    max_exposure_percent,
    kill_switch_active,
    kill_switch_reason,
  } = risk;

  // Calculate progress percentages
  const drawdownProgress = calcProgress(current_drawdown_percent, max_drawdown_percent);
  const dailyLossProgress = calcProgress(daily_loss_percent, daily_loss_limit_percent);
  const exposureProgress = calcProgress(current_exposure_percent, max_exposure_percent);

  // Get color classes based on progress
  const getProgressColor = (progress: number) => {
    if (progress >= 80) return 'bg-danger';
    if (progress >= 50) return 'bg-warning';
    return 'bg-success';
  };

  return (
    <Card>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            <Shield className="h-5 w-5 text-primary" />
            Risk Dashboard
          </CardTitle>
          <Badge variant={kill_switch_active ? 'danger' : 'success'}>
            {kill_switch_active ? 'KILL SWITCH ON' : 'Active'}
          </Badge>
        </div>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Kill Switch Alert */}
        {kill_switch_active && (
          <div className="flex items-center justify-between bg-danger-bg text-danger rounded-lg p-3">
            <div className="flex items-center gap-2">
              <XOctagon className="h-5 w-5" />
              <span className="text-sm font-medium">{kill_switch_reason || 'Kill switch activated'}</span>
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={handleResetKillSwitch}
              className="text-danger border-danger hover:bg-danger hover:text-white"
            >
              Reset
            </Button>
          </div>
        )}

        {/* Drawdown */}
        <div className="space-y-2">
          <div className="flex items-center justify-between text-sm">
            <span className="text-text-secondary">Drawdown</span>
            <span className={cn(
              "font-mono font-medium",
              drawdownProgress >= 80 ? 'text-danger' : drawdownProgress >= 50 ? 'text-warning' : 'text-text-primary'
            )}>
              {current_drawdown_percent.toFixed(1)}% / {max_drawdown_percent}% max
            </span>
          </div>
          <Progress
            value={drawdownProgress}
            className="h-2"
            indicatorClassName={getProgressColor(drawdownProgress)}
          />
        </div>

        {/* Daily Loss */}
        <div className="space-y-2">
          <div className="flex items-center justify-between text-sm">
            <span className="text-text-secondary">Daily Loss</span>
            <span className={cn(
              "font-mono font-medium",
              dailyLossProgress >= 80 ? 'text-danger' : dailyLossProgress >= 50 ? 'text-warning' : 'text-text-primary'
            )}>
              {daily_loss_percent.toFixed(1)}% / {daily_loss_limit_percent}% max
            </span>
          </div>
          <Progress
            value={dailyLossProgress}
            className="h-2"
            indicatorClassName={getProgressColor(dailyLossProgress)}
          />
        </div>

        {/* Exposure */}
        <div className="space-y-2">
          <div className="flex items-center justify-between text-sm">
            <span className="text-text-secondary">Exposure</span>
            <span className={cn(
              "font-mono font-medium",
              exposureProgress >= 80 ? 'text-danger' : exposureProgress >= 50 ? 'text-warning' : 'text-text-primary'
            )}>
              {current_exposure_percent.toFixed(1)}% / {max_exposure_percent}% max
            </span>
          </div>
          <Progress
            value={exposureProgress}
            className="h-2"
            indicatorClassName={getProgressColor(exposureProgress)}
          />
        </div>

        {/* Current Position */}
        <div className="bg-surface-light rounded-lg p-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Activity className="h-4 w-4 text-text-muted" />
              <span className="text-sm text-text-secondary">Position</span>
            </div>
            {position ? (
              <div className="text-right">
                <Badge variant={position.side === 'LONG' ? 'success' : 'danger'}>
                  {position.side}
                </Badge>
                <div className="text-xs text-text-muted mt-1">
                  {position.quantity} {position.symbol.replace('USDT', '')}
                </div>
              </div>
            ) : (
              <span className="text-sm text-text-muted">None</span>
            )}
          </div>
          {position && (
            <div className="mt-2 pt-2 border-t border-border">
              <div className="flex items-center justify-between text-sm">
                <span className="text-text-muted">Unrealized PnL</span>
                <span className={cn(
                  "font-mono font-medium",
                  position.unrealized_pnl_usd >= 0 ? 'text-success' : 'text-danger'
                )}>
                  {position.unrealized_pnl_usd >= 0 ? '+' : ''}
                  {formatUSD(position.unrealized_pnl_usd)}
                  <span className="text-xs ml-1">
                    ({position.unrealized_pnl_percent >= 0 ? '+' : ''}
                    {position.unrealized_pnl_percent.toFixed(2)}%)
                  </span>
                </span>
              </div>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
