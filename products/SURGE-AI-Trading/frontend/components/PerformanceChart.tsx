'use client';

import { TrendingUp } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Area,
  AreaChart,
} from 'recharts';
import { formatUSD, formatPercent } from '@/lib/utils';

// Generate mock equity curve data
const generateEquityData = () => {
  const data = [];
  let equity = 10000;
  const days = 30;

  for (let i = 0; i < days; i++) {
    const date = new Date();
    date.setDate(date.getDate() - (days - i));

    // Random daily change between -2% and +3%
    const change = (Math.random() * 5 - 2) / 100;
    equity = equity * (1 + change);

    data.push({
      date: date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
      equity: Math.round(equity * 100) / 100,
      pnl: ((equity - 10000) / 10000) * 100,
    });
  }

  return data;
};

const equityData = generateEquityData();

export function PerformanceChart() {
  const currentEquity = equityData[equityData.length - 1]?.equity ?? 10000;
  const totalPnl = currentEquity - 10000;
  const totalPnlPercent = (totalPnl / 10000) * 100;

  return (
    <Card>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            <TrendingUp className="h-5 w-5 text-primary" />
            Performance Chart
          </CardTitle>
          <div className="text-right">
            <div className="text-sm text-text-muted">Equity Curve (30 days)</div>
            <div className={`font-mono font-bold ${totalPnl >= 0 ? 'text-success' : 'text-danger'}`}>
              {totalPnl >= 0 ? '+' : ''}{formatUSD(totalPnl)} ({formatPercent(totalPnlPercent)})
            </div>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div className="h-[200px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart
              data={equityData}
              margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
            >
              <defs>
                <linearGradient id="equityGradient" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#6366f1" stopOpacity={0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#2a2a3a" />
              <XAxis
                dataKey="date"
                stroke="#71717a"
                fontSize={10}
                tickLine={false}
                axisLine={false}
              />
              <YAxis
                stroke="#71717a"
                fontSize={10}
                tickLine={false}
                axisLine={false}
                tickFormatter={(value) => `$${(value / 1000).toFixed(1)}k`}
                domain={['dataMin - 500', 'dataMax + 500']}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: '#121218',
                  border: '1px solid #2a2a3a',
                  borderRadius: '8px',
                  padding: '8px 12px',
                }}
                labelStyle={{ color: '#a1a1aa', marginBottom: '4px' }}
                formatter={(value: number, name: string) => {
                  if (name === 'equity') {
                    return [formatUSD(value), 'Equity'];
                  }
                  return [formatPercent(value), 'P&L'];
                }}
              />
              <Area
                type="monotone"
                dataKey="equity"
                stroke="#6366f1"
                strokeWidth={2}
                fill="url(#equityGradient)"
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  );
}
