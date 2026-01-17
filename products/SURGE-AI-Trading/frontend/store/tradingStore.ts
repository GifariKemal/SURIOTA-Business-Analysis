/**
 * SURGE-AI Trading Dashboard - Zustand Store
 * Global state management for the trading dashboard
 */
import { create } from 'zustand';
import { devtools } from 'zustand/middleware';
import type {
  PriceData,
  Signal,
  TradeRecommendation,
  Position,
  Balance,
  RiskMetrics,
  ActivityItem,
  PerformanceMetrics,
  EquityPoint,
  TradeResult,
} from '@/types';
import { generateId } from '@/lib/utils';

// ============================================================
// State Interface
// ============================================================

interface TradingState {
  // Connection
  isConnected: boolean;
  lastUpdate: string | null;

  // Market Data
  price: PriceData | null;
  idrRate: number;

  // Signals
  signal: Signal | null;
  recommendation: TradeRecommendation | null;

  // Trading
  position: Position | null;
  balance: Balance | null;

  // Risk
  risk: RiskMetrics | null;

  // Activity Feed
  activities: ActivityItem[];

  // Performance
  performance: PerformanceMetrics | null;
  equityCurve: EquityPoint[];

  // UI State
  isLoading: boolean;
  error: string | null;

  // Actions
  setConnected: (connected: boolean) => void;
  setPrice: (price: PriceData) => void;
  setSignal: (signal: Signal) => void;
  setRecommendation: (recommendation: TradeRecommendation) => void;
  setPosition: (position: Position | null) => void;
  setBalance: (balance: Balance) => void;
  setRisk: (risk: RiskMetrics) => void;
  addActivity: (activity: Omit<ActivityItem, 'id'>) => void;
  clearActivities: () => void;
  setPerformance: (performance: PerformanceMetrics) => void;
  addEquityPoint: (point: EquityPoint) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  reset: () => void;
}

// ============================================================
// Initial State
// ============================================================

const initialState = {
  isConnected: false,
  lastUpdate: null,
  price: null,
  idrRate: 16000,
  signal: null,
  recommendation: null,
  position: null,
  balance: null,
  risk: null,
  activities: [],
  performance: null,
  equityCurve: [],
  isLoading: false,
  error: null,
};

// ============================================================
// Create Store
// ============================================================

export const useTradingStore = create<TradingState>()(
  devtools(
    (set, get) => ({
      ...initialState,

      // Connection
      setConnected: (connected) =>
        set({ isConnected: connected, lastUpdate: new Date().toISOString() }),

      // Market Data
      setPrice: (price) =>
        set({
          price,
          idrRate: price.idr_rate,
          lastUpdate: new Date().toISOString(),
        }),

      // Signals
      setSignal: (signal) =>
        set({ signal, lastUpdate: new Date().toISOString() }),

      setRecommendation: (recommendation) =>
        set({ recommendation, lastUpdate: new Date().toISOString() }),

      // Trading
      setPosition: (position) =>
        set({ position, lastUpdate: new Date().toISOString() }),

      setBalance: (balance) =>
        set({ balance, lastUpdate: new Date().toISOString() }),

      // Risk
      setRisk: (risk) =>
        set({ risk, lastUpdate: new Date().toISOString() }),

      // Activity Feed
      addActivity: (activity) => {
        const newActivity: ActivityItem = {
          ...activity,
          id: generateId(),
        };

        set((state) => ({
          activities: [newActivity, ...state.activities].slice(0, 50), // Keep last 50
          lastUpdate: new Date().toISOString(),
        }));
      },

      clearActivities: () => set({ activities: [] }),

      // Performance
      setPerformance: (performance) =>
        set({ performance, lastUpdate: new Date().toISOString() }),

      addEquityPoint: (point) =>
        set((state) => ({
          equityCurve: [...state.equityCurve, point].slice(-100), // Keep last 100 points
        })),

      // UI State
      setLoading: (loading) => set({ isLoading: loading }),
      setError: (error) => set({ error }),

      // Reset
      reset: () => set(initialState),
    }),
    { name: 'trading-store' }
  )
);

// ============================================================
// Selectors
// ============================================================

export const selectIsConnected = (state: TradingState) => state.isConnected;
export const selectPrice = (state: TradingState) => state.price;
export const selectSignal = (state: TradingState) => state.signal;
export const selectRecommendation = (state: TradingState) => state.recommendation;
export const selectPosition = (state: TradingState) => state.position;
export const selectBalance = (state: TradingState) => state.balance;
export const selectRisk = (state: TradingState) => state.risk;
export const selectActivities = (state: TradingState) => state.activities;
export const selectPerformance = (state: TradingState) => state.performance;

// Computed selectors
export const selectHasPosition = (state: TradingState) => state.position !== null;
export const selectIsKillSwitchActive = (state: TradingState) =>
  state.risk?.kill_switch_active ?? false;
export const selectCanTrade = (state: TradingState) =>
  state.isConnected &&
  state.recommendation?.is_executable &&
  !state.risk?.kill_switch_active;
