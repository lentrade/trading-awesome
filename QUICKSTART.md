# Quick Start Guide

> New to algorithmic trading? This guide gives you a concrete path from zero to your first backtest or paper trade in under 30 minutes.

---

## Step 0: Before You Start

### What you need

| Skill level | Minimum requirements |
|-------------|---------------------|
| **Complete beginner** | Basic Python, a text editor, and curiosity |
| **Some coding experience** | Familiarity with pandas, REST APIs, and JSON |
| **Professional developer** | You can skip to the [Comparison Matrix](COMPARISON.md) |

### Essential concepts to understand first

1. **OHLCV data** — Open, High, Low, Close, Volume. The building block of almost all trading analysis.
2. **Backtesting** — Running a strategy on historical data to see how it would have performed. **Not** a guarantee of future results.
3. **Paper trading** — Simulated trading with real market data but fake money.
4. **API keys** — Credentials that let your code talk to a broker or data provider. Keep them secret.

---

## Path 1: "I want to backtest a simple strategy" (15 min)

### Goal
Download historical stock data and run a moving-average crossover strategy.

### 1. Install Python packages
```bash
pip install yfinance backtesting pandas
```

### 2. Get data
```python
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01", end="2024-12-31")
print(data.head())
```

### 3. Run a strategy
```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as ta

class SmaCross(Strategy):
    def init(self):
        self.sma1 = self.I(ta.sma, self.data.Close, 10)
        self.sma2 = self.I(ta.sma, self.data.Close, 30)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

bt = Backtest(data, SmaCross, cash=10_000, commission=0.002)
stats = bt.run()
print(stats)
bt.plot()
```

### What's happening here?
- `yfinance` pulls free end-of-day data from Yahoo Finance
- `backtesting.py` handles the simulation loop, accounting, and reporting
- The strategy buys when the 10-day SMA crosses above the 30-day SMA, sells on the reverse

### Next steps
- Try different assets (`SPY`, `BTC-USD`, `EURUSD=X`)
- Add a stop-loss: `self.buy(sl=self.data.Close[-1] * 0.95)`
- Read the [backtesting.py docs](https://kernc.github.io/backtesting.py/)

---

## Path 2: "I want to paper-trade U.S. stocks" (20 min)

### Goal
Connect to Alpaca and place a simulated order.

### 1. Sign up
- Create a free [Alpaca](https://alpaca.markets/) account
- Generate API keys (paper trading environment)

### 2. Install SDK
```bash
pip install alpaca-py
```

### 3. Place a paper trade
```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

# Replace with your paper API keys
API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Check account
account = client.get_account()
print(f"Buying power: ${account.buying_power}")

# Place a market order
order = MarketOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)

client.submit_order(order)
print("Order submitted!")
```

### What's happening here?
- `paper=True` ensures no real money is at risk
- Alpaca provides free real-time market data for U.S. equities
- Orders are simulated but executed against real market prices

### Next steps
- Fetch your positions: `client.get_all_positions()`
- Set up a scheduled script to run daily
- Read the [Alpaca docs](https://docs.alpaca.markets/)

---

## Path 3: "I want crypto market data" (10 min)

### Goal
Fetch real-time crypto prices using a free API.

### Option A: CoinGecko (no API key needed)
```python
import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)
data = response.json()

for coin, info in data.items():
    print(f"{coin}: ${info['usd']} (24h: {info['usd_24h_change']:.2f}%)")
```

### Option B: Binance (no API key for public data)
```python
import requests

url = "https://api.binance.com/api/v3/ticker/24hr"
params = {"symbol": "BTCUSDT"}

response = requests.get(url, params=params)
data = response.json()

print(f"BTC/USDT: ${float(data['lastPrice']):,.2f}")
print(f"24h change: {float(data['priceChangePercent']):.2f}%")
print(f"24h volume: {float(data['volume']):,.2f} BTC")
```

### What's happening here?
- Both APIs are free for basic public data
- CoinGecko is simpler but has stricter rate limits
- Binance provides more granular data but requires understanding of their API structure

### Next steps
- Build a price alert (check price every minute, send notification)
- Store historical data in a local database
- Try [CCXT](https://github.com/ccxt/ccxt) to access multiple exchanges with one interface

---

## Path 4: "I want to analyze my portfolio" (15 min)

### Goal
Calculate key metrics for a portfolio of stocks.

### 1. Install packages
```bash
pip install quantstats yfinance
```

### 2. Analyze returns
```python
import yfinance as yf
import quantstats as qs

# Download data
spy = yf.download("SPY", start="2020-01-01")["Adj Close"]
portfolio = yf.download("AAPL,MSFT,GOOGL", start="2020-01-01")["Adj Close"]

# Equal-weighted portfolio
returns = portfolio.pct_change().mean(axis=1)

# Generate report
qs.reports.html(returns, benchmark=spy.pct_change(), output="report.html")
print("Report saved to report.html")
```

### What's happening here?
- `quantstats` calculates Sharpe ratio, max drawdown, CAGR, and dozens of other metrics
- The benchmark (SPY) lets you evaluate whether your portfolio beats the market
- The HTML report is shareable and interactive

### Next steps
- Add transaction costs and rebalancing logic
- Test different weighting schemes (equal, market-cap, risk-parity)
- Try [PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/) for optimization

---

## Common Pitfalls for Beginners

### 1. Overfitting
**Problem**: Your strategy looks perfect on historical data but fails in live trading.
**Solution**: Use out-of-sample testing, walk-forward analysis, and keep your strategy simple.

### 2. Ignoring costs
**Problem**: Backtests assume zero commissions and perfect execution.
**Solution**: Always include realistic commission, slippage, and market-impact assumptions.

### 3. Data leakage
**Problem**: Using information that wouldn't have been available at the time.
**Solution**: Be paranoid about timestamps. Use event time, not calendar time.

### 4. Survivorship bias
**Problem**: Only testing on companies that are still around.
**Solution**: Include delisted tickers or acknowledge the limitation.

### 5. Going live too early
**Problem**: Skipping paper trading and risking real money.
**Solution**: Paper trade for at least 3 months before going live. Track every discrepancy.

---

## Recommended Learning Path

| Week | Focus | Tools |
|------|-------|-------|
| 1–2 | Backtesting basics | backtesting.py, yfinance, pandas-ta |
| 3–4 | Data handling & cleaning | pandas, NumPy, TA-Lib |
| 5–6 | Paper trading | Alpaca, CCXT (crypto) |
| 7–8 | Portfolio analysis | quantstats, PyPortfolioOpt |
| 9–12 | Advanced topics | vectorbt (speed), NautilusTrader (production) |

---

## Need Help?

- **Stack Overflow** — Tag questions with `[algorithmic-trading]`, `[pandas]`, `[alpaca]`
- **Reddit** — r/algotrading, r/quantfinance
- **Discord** — Many communities exist for specific tools (check each tool's GitHub for invites)
- **This repo's Discussions** — Open a thread for general questions

---

## One-Line Starters

Copy-paste these to get started instantly:

```bash
# Full beginner stack
pip install yfinance backtesting pandas pandas-ta quantstats

# Crypto + trading stack
pip install ccxt pandas numpy

# Production stack
pip install nautilus_trader vectorbt

# All-in-one research stack
pip install yfinance backtesting quantstats pyportfolioopt
```

---

**Remember**: Every expert was once a beginner. Start simple, stay curious, and never risk money you can't afford to lose. 🚀
