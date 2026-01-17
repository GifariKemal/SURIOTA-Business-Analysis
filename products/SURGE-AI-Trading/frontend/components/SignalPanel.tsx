'use client';

import { Target, Brain, Database, MessageSquare, Zap } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { Separator } from '@/components/ui/separator';
import { useTradingStore } from '@/store/tradingStore';
import { cn, getSignalColor, getConfidenceLevel, getConfidenceColor } from '@/lib/utils';

export function SignalPanel() {
  const { signal } = useTradingStore();

  if (!signal) {
    return (
      <Card className="animate-pulse">
        <CardHeader>
          <div className="h-5 bg-surface-light rounded w-32" />
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="h-10 bg-surface-light rounded" />
            <div className="h-4 bg-surface-light rounded w-3/4" />
            <div className="space-y-2">
              {[1, 2, 3, 4].map((i) => (
                <div key={i} className="h-6 bg-surface-light rounded" />
              ))}
            </div>
          </div>
        </CardContent>
      </Card>
    );
  }

  const { direction, confidence, kalman_breakdown } = signal;

  // Determine badge variant based on direction
  const badgeVariant = direction === 'LONG' ? 'long' : direction === 'SHORT' ? 'short' : 'neutral';

  return (
    <Card>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            <Target className="h-5 w-5 text-primary" />
            Signal Panel
          </CardTitle>
          {signal.is_actionable && (
            <span className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-success opacity-75" />
              <span className="relative inline-flex rounded-full h-3 w-3 bg-success" />
            </span>
          )}
        </div>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Current Signal */}
        <div className="flex items-center justify-between">
          <div>
            <div className="text-sm text-text-muted mb-1">Current Signal</div>
            <Badge variant={badgeVariant} className="text-lg px-4 py-1">
              {direction}
            </Badge>
          </div>
          <div className="text-right">
            <div className="text-sm text-text-muted mb-1">Confidence</div>
            <div className={cn("text-2xl font-bold font-mono", getConfidenceColor(confidence))}>
              {confidence.toFixed(1)}%
            </div>
            <div className={cn("text-xs", getConfidenceColor(confidence))}>
              {getConfidenceLevel(confidence)}
            </div>
          </div>
        </div>

        <Separator className="my-4" />

        {/* Kalman Breakdown */}
        <div className="space-y-3">
          <div className="text-sm font-medium text-text-secondary">Kalman Filter Breakdown</div>

          {/* ML Signal */}
          <div className="space-y-1">
            <div className="flex items-center justify-between text-sm">
              <div className="flex items-center gap-2">
                <Brain className="h-4 w-4 text-info" />
                <span className="text-text-secondary">Kalman ML</span>
                <span className="text-xs text-text-muted">({(kalman_breakdown.ml_weight * 100).toFixed(0)}%)</span>
              </div>
              <span className="font-mono font-medium">{kalman_breakdown.ml_signal.toFixed(1)}%</span>
            </div>
            <Progress
              value={kalman_breakdown.ml_signal}
              className="h-1.5"
              indicatorClassName="bg-info"
            />
          </div>

          {/* DB Signal */}
          <div className="space-y-1">
            <div className="flex items-center justify-between text-sm">
              <div className="flex items-center gap-2">
                <Database className="h-4 w-4 text-accent" />
                <span className="text-text-secondary">Kalman DB</span>
                <span className="text-xs text-text-muted">({(kalman_breakdown.db_weight * 100).toFixed(0)}%)</span>
              </div>
              <span className="font-mono font-medium">{kalman_breakdown.db_signal.toFixed(1)}%</span>
            </div>
            <Progress
              value={kalman_breakdown.db_signal}
              className="h-1.5"
              indicatorClassName="bg-accent"
            />
          </div>

          {/* Sentiment Signal */}
          <div className="space-y-1">
            <div className="flex items-center justify-between text-sm">
              <div className="flex items-center gap-2">
                <MessageSquare className="h-4 w-4 text-warning" />
                <span className="text-text-secondary">Kalman Sent</span>
                <span className="text-xs text-text-muted">({(kalman_breakdown.sentiment_weight * 100).toFixed(0)}%)</span>
              </div>
              <span className="font-mono font-medium">{kalman_breakdown.sentiment_signal.toFixed(1)}%</span>
            </div>
            <Progress
              value={kalman_breakdown.sentiment_signal}
              className="h-1.5"
              indicatorClassName="bg-warning"
            />
          </div>

          {/* Enhanced Signal */}
          <div className="space-y-1">
            <div className="flex items-center justify-between text-sm">
              <div className="flex items-center gap-2">
                <Zap className="h-4 w-4 text-primary" />
                <span className="text-text-secondary">Kalman Enh</span>
                <span className="text-xs text-text-muted">(Fused)</span>
              </div>
              <span className="font-mono font-medium text-primary">{kalman_breakdown.enhanced_signal.toFixed(1)}%</span>
            </div>
            <Progress
              value={kalman_breakdown.enhanced_signal}
              className="h-1.5"
              indicatorClassName="bg-primary"
            />
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
