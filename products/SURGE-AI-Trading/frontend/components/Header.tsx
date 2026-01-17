'use client';

import { Activity, Settings, Wifi, WifiOff } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useTradingStore } from '@/store/tradingStore';
import { formatIDR, getRelativeTime } from '@/lib/utils';

export function Header() {
  const { isConnected, lastUpdate, idrRate } = useTradingStore();

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between px-4">
        {/* Logo & Title */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-primary to-accent flex items-center justify-center">
              <Activity className="h-5 w-5 text-white" />
            </div>
            <div>
              <h1 className="text-lg font-bold text-white">SURGE-AI Trading</h1>
              <p className="text-xs text-text-muted">Semi-Autonomous Dashboard</p>
            </div>
          </div>
        </div>

        {/* Status Indicators */}
        <div className="flex items-center gap-4">
          {/* Connection Status */}
          <div className="flex items-center gap-2">
            {isConnected ? (
              <>
                <div className="relative">
                  <Wifi className="h-4 w-4 text-success" />
                  <span className="absolute -right-1 -top-1 h-2 w-2 rounded-full bg-success animate-pulse" />
                </div>
                <span className="text-sm text-success">Connected</span>
              </>
            ) : (
              <>
                <WifiOff className="h-4 w-4 text-danger" />
                <span className="text-sm text-danger">Disconnected</span>
              </>
            )}
          </div>

          {/* IDR Rate */}
          <Badge variant="secondary" className="font-mono">
            1 USD = {formatIDR(idrRate)}
          </Badge>

          {/* Last Update */}
          {lastUpdate && (
            <span className="text-xs text-text-muted">
              Updated {getRelativeTime(lastUpdate)}
            </span>
          )}

          {/* Settings Button */}
          <Button variant="ghost" size="icon">
            <Settings className="h-5 w-5" />
          </Button>
        </div>
      </div>
    </header>
  );
}
