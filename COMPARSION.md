# Detailed Service Comparisons

> Side-by-side matrices to help you choose between similar services. These are starting points — always run your own proof of concept before committing.

---

## 1. Brokerage & Execution APIs

| Feature | Interactive Brokers | Alpaca | tastytrade | Tradier | OANDA |
|---------|-------------------|--------|------------|---------|-------|
| **Markets** | Global multi-asset | U.S. equities, options, crypto | U.S. stocks, options, futures, crypto | U.S. equities, options | Forex, CFDs |
| **API types** | REST, WebSocket, FIX, TWS | REST, WebSocket | REST | REST, WebSocket | REST (v20) |
| **Paper trading** | ✅ | ✅ | ❌ | ❌ | ✅ (demo) |
| **Commission** | Variable by tier | $0 (stocks/ETFs) | $0 (stocks), $1/contract (options) | From $10/month | Spread-based |
| **Min. deposit** | $0 | $0 | $0 | $0 | $0 |
| **Python SDK** | ✅ Official | ✅ Official | ✅ Official | ⚠️ Community | ✅ Official |
| **Go SDK** | ❌ | ✅ Official | ❌ | ⚠️ Community | ❌ |
| **Rate limits** | ~100 req/2s | 200 req/min | 300 req/min | 480 req/min | 100 req/2s |
| **Best for** | Serious multi-asset traders | U.S. algo beginners | Active options traders | API-first developers | Forex specialists |
| **Complexity** | High | Low | Medium | Low | Medium |

### Quick picks
- **First time + U.S. stocks** → Alpaca
- **Global multi-asset + low commissions** → Interactive Brokers
- **Options-focused** → tastytrade
- **Forex only** → OANDA
- **Lowest friction API** → Tradier ( brokerage fee but simple )

---

## 2. Market Data APIs — Traditional Markets

| Feature | Finnhub | Twelve Data | Massive (ex-Polygon) | Alpha Vantage | Databento |
|---------|---------|-------------|---------------------|---------------|-----------|
| **Real-time** | ✅ WebSocket | ✅ WebSocket | ✅ WebSocket | ❌ Delayed | ✅ WebSocket |
| **Historical depth** | 1+ years | Varies by plan | 20+ years | 20+ years | Exchange-native |
| **Asset classes** | Stocks, forex, crypto, fundamentals | Stocks, forex, crypto, ETFs, funds | U.S. stocks, options, indices, futures, FX | Stocks, forex, crypto, tech indicators | Futures, options, equities, FX |
| **Free tier** | ✅ 60 calls/min | ✅ 800 calls/day | ✅ (limited) | ✅ 25 calls/day | ✅ Signup credits |
| **Python SDK** | ✅ Official | ✅ Official | ✅ Official | ⚠️ Community | ✅ Official |
| **Go SDK** | ✅ Official | ✅ Official | ✅ Official | ⚠️ Community | ❌ |
| **Pricing (entry)** | $3,500/mo (All-in-One) | $79/mo | $29/mo | $49.99/mo | $199/mo |
| **Data quality** | Aggregated | Aggregated | Exchange-sourced | Aggregated | **Exchange-direct** |
| **Best for** | Broad coverage | Developer-friendly | U.S. equities & options | Beginners, low volume | Systematic research |

### Quick picks
- **Free + broad** → Finnhub or Twelve Data
- **Serious U.S. equities research** → Massive or Databento
- **Lowest cost entry** → Alpha Vantage (limited) or Marketstack ($9.99/mo)
- **Institutional quality** → Databento (exchange-native)

---

## 3. Crypto Exchange APIs

| Feature | Binance | Coinbase | Kraken | Bybit | OKX |
|---------|---------|----------|--------|-------|-----|
| **Spot trading** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Futures / Derivatives** | ✅ | Eligible | ✅ | ✅ | ✅ |
| **Options** | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Python SDK** | ✅ Official | ✅ Official | ✅ Official | ✅ Official | ✅ Official |
| **Go SDK** | ✅ Official | ❌ | ✅ Official | ⚠️ Community | ⚠️ Community |
| **WebSocket** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Testnet** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Fee (maker/taker)** | 0.1% / 0.1% | 0.60% / 1.20% | 0.16% / 0.26% | 0.02% / 0.055% | 0.08% / 0.1% |
| **Jurisdiction** | Global (restrictions apply) | Global (restrictions apply) | Global (restrictions apply) | Global | Global |
| **Best for** | Liquidity + features | U.S. compliance | Security reputation | Derivatives | All-in-one |

### Quick picks
- **Highest liquidity** → Binance
- **U.S. regulatory comfort** → Coinbase
- **Security-first** → Kraken
- **Derivatives + low fees** → Bybit or OKX
- **One library for all** → CCXT (unified API)

---

## 4. Backtesting Frameworks

| Feature | Backtrader | vectorbt | Zipline Reloaded | NautilusTrader | backtesting.py |
|---------|-----------|----------|------------------|----------------|----------------|
| **Speed** | Event-driven (slow) | Vectorized (fast) | Event-driven (slow) | Rust + Python (fastest) | Vectorized (fast) |
| **Live trading** | ✅ (limited brokers) | ❌ (research only) | ❌ (backtest only) | ✅ (production-grade) | ❌ |
| **Asset classes** | Multi-asset | Multi-asset | Equities only | Multi-asset | Multi-asset |
| **Python version** | 3.6+ | 3.8+ | 3.8+ | 3.10+ | 3.7+ |
| **Learning curve** | Medium | Medium | High | High | Low |
| **Community** | Large, but slow maintenance | Active | Small | Growing | Active |
| **Best for** | Mature backtesting | Rapid strategy research | Quantopian alumni | Production systems | Simple backtests |

### Quick picks
- **Beginner + quick results** → backtesting.py
- **Research + parameter sweeps** → vectorbt
- **Production deployment** → NautilusTrader
- **Mature but maintenance concerns** → Backtrader

---

## 5. Crypto Market Intelligence

| Feature | CoinGecko | CoinMarketCap | CoinGlass | Glassnode | Dune |
|---------|-----------|---------------|-----------|-----------|------|
| **Price data** | ✅ | ✅ | ✅ | ✅ | ✅ (via queries) |
| **On-chain metrics** | ✅ (DEX) | ❌ | ✅ | ✅ | ✅ (SQL) |
| **Futures data** | ⚠️ Limited | ❌ | ✅ (excellent) | ⚠️ Limited | ⚠️ Via queries |
| **Social sentiment** | ❌ | ❌ | ❌ | ⚠️ (Santiment) | ❌ |
| **API free tier** | ✅ Generous | ✅ Basic | ❌ | ⚠️ Dashboard only | ✅ Credits |
| **SQL access** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Best for** | Price + metadata | Rankings + listings | Derivatives analytics | On-chain research | Custom blockchain research |

### Quick picks
- **Free crypto prices** → CoinGecko
- **Futures + funding data** → CoinGlass
- **On-chain deep dive** → Glassnode
- **Custom SQL research** → Dune
- **All-in-one social + on-chain** → Santiment or LunarCrush

---

## 6. Portfolio Analytics

| Feature | QuantStats | Riskfolio-Lib | skfolio | PyPortfolioOpt |
|---------|-----------|---------------|---------|----------------|
| **Performance metrics** | ✅ (comprehensive) | ⚠️ (allocation-focused) | ⚠️ (allocation-focused) | ❌ |
| **Risk measures** | ✅ (drawdowns, VaR) | ✅ (20+ risk measures) | ✅ (CVaR, CDaR) | ⚠️ (mean-variance) |
| **Optimization** | ❌ | ✅ (extensive) | ✅ (scikit-learn style) | ✅ (mean-var, HRP, BL) |
| **ML integration** | ❌ | ❌ | ✅ | ❌ |
| **Reporting** | ✅ (HTML tearsheets) | ⚠️ | ⚠️ | ❌ |
| **Best for** | Performance reporting | Advanced risk optimization | ML-based allocation | Classical portfolio theory |

### Quick picks
- **Beautiful HTML reports** → QuantStats
- **Complex risk optimization** → Riskfolio-Lib
- **Scikit-learn workflow** → skfolio
- **Mean-variance + Black-Litterman** → PyPortfolioOpt

---

## 7. Infrastructure — Time-Series Databases

| Feature | ClickHouse | QuestDB | TimescaleDB | InfluxDB* |
|---------|-----------|---------|-------------|-----------|
| **Storage model** | Column-oriented | Column-oriented (relational) | PostgreSQL extension | Column-oriented |
| **SQL support** | ✅ (dialect) | ✅ (ANSI) | ✅ (full PostgreSQL) | ✅ (InfluxQL/Flux) |
| **Ingestion speed** | Excellent | Excellent | Good | Good |
| **Best for ticks** | ✅ | ✅ | ⚠️ | ⚠️ |
| **Joins** | ⚠️ (limited) | ✅ (time-series joins) | ✅ (full SQL) | ⚠️ |
| **Open source** | ✅ | ✅ | ✅ | ✅ |
| **Managed cloud** | ✅ | ✅ | ✅ | ✅ |
| **Best for** | Large-scale analytics | Tick data + SQL | PostgreSQL users | Metrics/IoT |

*InfluxDB is not in the main README but commonly used; included for completeness.

### Quick picks
- **Already using PostgreSQL** → TimescaleDB
- **Maximum ingestion speed** → QuestDB
- **Analytical queries on large history** → ClickHouse

---

## 8. AI / ML Frameworks

| Feature | Microsoft Qlib | FinRL | FinGPT | TensorTrade |
|---------|---------------|-------|--------|-------------|
| **Focus** | Quant research platform | RL for trading | Financial LLMs | RL framework |
| **Includes data** | ✅ (built-in) | ⚠️ (examples) | ❌ | ❌ |
| **Includes backtest** | ✅ | ✅ | ❌ | ✅ |
| **Includes live trading** | ❌ | ⚠️ (FinRL-X) | ❌ | ⚠️ |
| **Active maintenance** | ✅ (Microsoft) | ⚠️ (research) | ⚠️ (research) | ⚠️ (stalled) |
| **Best for** | End-to-end quant research | RL research | NLP/sentiment research | RL experimentation |

### Quick picks
- **Full quant pipeline** → Qlib
- **Reinforcement learning** → FinRL
- **LLM + sentiment** → FinGPT
- **Note**: All AI/ML frameworks should be treated as **research tools**, not production systems.

---

## Decision Trees

### "I need to choose ONE tool for..."

**Data (free, starting out)**
```
Crypto prices? → CoinGecko
U.S. stocks? → yfinance (free) or Alpaca (free tier)
Forex? → OANDA demo
Global macro? → FRED (direct) or Trading Economics
```

**Execution (going live)**
```
U.S. stocks? → Alpaca (simple) or Interactive Brokers (advanced)
Crypto? → Binance (liquidity) or Kraken (security)
Forex? → OANDA (regulated) or cTrader (broker choice)
```

**Backtesting**
```
Learning / simple? → backtesting.py
Research / parameter sweeps? → vectorbt
Production-ready? → NautilusTrader
```

**Portfolio Analysis**
```
Reporting to clients? → QuantStats
Complex optimization? → Riskfolio-Lib
ML pipeline? → skfolio
```

---

## Methodology Notes

- **"Official" SDK** = maintained by the service provider or explicitly endorsed
- **"Community" SDK** = third-party; verify maintenance and security before production use
- **Pricing** = entry-level public pricing as of 27 July 2026; always verify current rates
- **"Best for"** = editorial opinion based on common use cases; your needs may differ

---

## Contributing Comparisons

Found an error or want to add a comparison? See [CONTRIBUTING.md](CONTRIBUTING.md). Comparisons should be:
- **Fact-based** (not opinionated marketing)
- **Source-linked** (pricing, feature claims)
- **Up-to-date** (verified within 6 months)
