'use client';

import { useState } from 'react';
import {
  Activity,
  Target,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  ShieldAlert,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { useTradingStore } from '@/store/tradingStore';
import { formatTime, cn } from '@/lib/utils';
import type { ActivityItem, ActivityType } from '@/types';

// Mock activity data for demo
const mockActivities: ActivityItem[] = [
  {
    id: '1',
    type: 'signal',
    timestamp: new Date(Date.now() - 5 * 60000).toISOString(),
    title: 'LONG Signal (72.3% confidence)',
    description: 'Recommended: BUY 0.0142 BTC @ $87,648',
    details: [
      'ML: RSI oversold bounce + MACD crossover',
      'DB: 87/100 similar patterns → +3.2% avg',
      'Sentiment: Neutral (Fear & Greed: 52)',
      'Risk: Position size 12.5% (Half Kelly)',
    ],
    is_expanded: false,
  },
  {
    id: '2',
    type: 'trade',
    timestamp: new Date(Date.now() - 15 * 60000).toISOString(),
    title: 'Trade CLOSED | SELL @ $87,648 | +2.9%',
    description: 'Entry: $85,180 → Exit: $87,648 | Profit: $350',
    details: ['Hold time: 4h 23m', 'Max drawdown: 0.8%'],
    is_expanded: false,
  },
  {
    id: '3',
    type: 'blocked',
    timestamp: new Date(Date.now() - 45 * 60000).toISOString(),
    title: 'Signal BLOCKED',
    description: 'Confidence 58% below 70% threshold',
    details: ['ML Signal: 52.3%', 'DB Signal: 61.2%', 'Sentiment: 49.8%'],
    is_expanded: false,
  },
  {
    id: '4',
    type: 'alert',
    timestamp: new Date(Date.now() - 2 * 3600000).toISOString(),
    title: 'Drawdown Warning',
    description: 'Drawdown approaching 50% of limit',
    details: ['Current: 7.2%', 'Limit: 15%'],
    is_expanded: false,
  },
];

const getActivityIcon = (type: ActivityType) => {
  switch (type) {
    case 'signal':
      return <Target className="h-4 w-4 text-success" />;
    case 'trade':
      return <CheckCircle2 className="h-4 w-4 text-info" />;
    case 'blocked':
      return <XCircle className="h-4 w-4 text-warning" />;
    case 'alert':
      return <AlertTriangle className="h-4 w-4 text-danger" />;
    case 'risk':
      return <ShieldAlert className="h-4 w-4 text-danger" />;
    default:
      return <Activity className="h-4 w-4 text-text-muted" />;
  }
};

const getActivityBadge = (type: ActivityType) => {
  switch (type) {
    case 'signal':
      return 'success';
    case 'trade':
      return 'info';
    case 'blocked':
      return 'warning';
    case 'alert':
    case 'risk':
      return 'danger';
    default:
      return 'secondary';
  }
};

function ActivityCard({ activity }: { activity: ActivityItem }) {
  const [isExpanded, setIsExpanded] = useState(activity.is_expanded);

  return (
    <div className="bg-surface-light rounded-lg p-4 transition-all hover:bg-surface-hover">
      <div className="flex items-start gap-3">
        <div className="mt-0.5">{getActivityIcon(activity.type)}</div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs text-text-muted font-mono">
              {formatTime(activity.timestamp)}
            </span>
            <Badge variant={getActivityBadge(activity.type) as any} className="text-xs">
              {activity.type.toUpperCase()}
            </Badge>
          </div>
          <div className="font-medium text-white mt-1">{activity.title}</div>
          <div className="text-sm text-text-secondary mt-0.5">{activity.description}</div>

          {/* Expandable Details */}
          {activity.details.length > 0 && (
            <>
              {isExpanded && (
                <div className="mt-3 space-y-1 pl-4 border-l-2 border-border">
                  {activity.details.map((detail, index) => (
                    <div key={index} className="text-xs text-text-muted">
                      {detail}
                    </div>
                  ))}
                </div>
              )}
              <Button
                variant="ghost"
                size="sm"
                onClick={() => setIsExpanded(!isExpanded)}
                className="mt-2 h-7 text-xs text-text-muted hover:text-white"
              >
                {isExpanded ? (
                  <>
                    <ChevronUp className="h-3 w-3 mr-1" />
                    Hide Details
                  </>
                ) : (
                  <>
                    <ChevronDown className="h-3 w-3 mr-1" />
                    Show Details
                  </>
                )}
              </Button>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export function ActivityFeed() {
  const { activities: storeActivities } = useTradingStore();

  // Use store activities if available, otherwise use mock data
  const activities = storeActivities.length > 0 ? storeActivities : mockActivities;

  return (
    <Card>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            <Activity className="h-5 w-5 text-primary" />
            Activity Feed
          </CardTitle>
          <span className="text-xs text-text-muted">AI Decisions</span>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-3 max-h-[400px] overflow-y-auto pr-2">
          {activities.length === 0 ? (
            <div className="text-center text-text-muted py-8">
              <Activity className="h-8 w-8 mx-auto mb-2 opacity-50" />
              <p>No activity yet</p>
              <p className="text-xs">Signals and trades will appear here</p>
            </div>
          ) : (
            activities.map((activity) => (
              <ActivityCard key={activity.id} activity={activity} />
            ))
          )}
        </div>
      </CardContent>
    </Card>
  );
}
