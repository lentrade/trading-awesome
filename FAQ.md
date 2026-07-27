# Frequently Asked Questions

## General

### Why this list exists

**Q: There are dozens of "awesome-trading" lists already. Why another one?**

A: Most existing lists are either (1) abandoned since 2020–2022, (2) focused on a single language or asset class, or (3) indiscriminately mix data APIs with brokerage APIs as if they solve the same problem. This list is actively maintained, cross-asset, and explicitly separates *data* from *execution*.

**Q: How often is this list updated?**

A: The editorial ranking is reviewed quarterly. Pricing and feature descriptions are spot-checked against provider sites. The current revision is dated **27 July 2026**.

**Q: Can I trust the rankings?**

A: Rankings reflect *editorial practical significance* — breadth, reliability, API maturity, and developer ecosystem. They are **not** investment advice, performance claims, or market-share data.

---

## Choosing a Service

**Q: I am a complete beginner. Where do I start?**

A: See the [Quick Start Guide](QUICKSTART.md). In short:
- Want to *paper-trade* U.S. stocks with code → **Alpaca**
- Want to *backtest* Python strategies → **Backtrader** or **vectorbt**
- Want *free crypto data* → **CoinGecko** API
- Want *free market data* for research → **Yahoo Finance** (via `yfinance`) or **Alpha Vantage**

**Q: I need real-time data. What's the cheapest option?**

A: It depends on the asset class:
- **U.S. equities**: Alpaca (free tier), Massive ($29/month), or Interactive Brokers (with live account)
- **Crypto**: Binance, Bybit, OKX — all provide real-time WebSocket feeds at no cost
- **Forex**: OANDA demo account includes real-time FX data
- **Global macro**: Trading Economics (from $22/month)

**Q: Which broker has the best API for algorithmic trading?**

A: There is no single "best" — it depends on your jurisdiction, assets, and latency requirements:
| If you need... | Consider... | Caveat |
|---|---|---|
| Lowest commissions + global access | Interactive Brokers | Steep learning curve; API is powerful but verbose |
| Simple U.S. equities automation | Alpaca | Limited to U.S. markets |
| FX + CFDs | OANDA, cTrader | Regional restrictions apply |
| Options-focused | tastytrade | U.S.-only |
| Crypto multi-exchange | CCXT | You still manage exchange-specific risks |

**Q: Is there a free way to get institutional-grade data?**

A: Not truly "institutional-grade" for free, but several providers offer generous free tiers:
- **Databento** — free signup credits for exchange-sourced data
- **Nasdaq Data Link** — many free datasets
- **FRED** (Federal Reserve) — free U.S. macro data (access via direct API or through a provider)
- **DeFiLlama** — completely free DeFi analytics
- **GDELT** — free global news/event datasets

---

## Technical

**Q: Do I need to know Python?**

A: No, but it helps. Roughly 70% of the libraries in this list offer first-party Python support. However, many services also provide:
- **Go** SDKs (Finnhub, Twelve Data, Binance, CCXT)
- **JavaScript/TypeScript** (TradingView charts, Plotly, ECharts)
- **PHP** (Finnhub, CCXT, some crypto exchange wrappers)
- **C#** (QuantConnect LEAN engine)

**Q: What's the difference between REST and WebSocket APIs?**

A: | | REST | WebSocket |
|---|---|---|
| **Direction** | Request-response (you ask, server answers) | Bi-directional (server pushes data to you) |
| **Use case** | Historical data, placing orders, account info | Real-time price feeds, live order book updates |
| **Rate limits** | Usually stricter | Often more permissive for subscriptions |
| **Complexity** | Simpler to implement | Requires connection management, reconnection logic |

For most retail algo-trading, REST is sufficient. WebSocket becomes critical for high-frequency or market-making strategies.

**Q: What are testnet / paper trading / sandbox environments?**

A:
- **Paper trading** — Simulated trading with real market data but fake money. No real orders hit the market.
- **Testnet / Sandbox** — A separate API environment with fake data and fake money, used for integration testing.
- **Dry-run** — Some frameworks (e.g., Freqtrade) can run against live exchange APIs but without placing real orders.

**Always test on paper/testnet before going live.**

---

## Pricing & Licensing

**Q: Why are some prices marked "contact sales"?**

A: Enterprise or institutional data providers rarely publish fixed prices because costs depend on:
- Data depth (top-of-book vs. full order book)
- Historical lookback required
- Redistribution rights
- Number of users / API keys
- Exchange fees passed through

"Contact sales" does **not** mean the service is expensive — it means pricing is negotiated.

**Q: What hidden costs should I watch for?**

A:
1. **Exchange fees** — Some data providers pass through exchange licensing fees separately
2. **Market data subscriptions** — Interactive Brokers charges separately for real-time data
3. **Rate limit overages** — Exceeding free tier limits can trigger unexpected bills
4. **WebSocket premium** — Some providers (e.g., CCXT Pro) charge for WebSocket access
5. **Redistribution restrictions** — Using data in a public app or commercial product often requires a more expensive license

**Q: Can I use open-source tools commercially?**

A: Depends on the license:
- **MIT / BSD / Apache 2.0** — Generally yes, with attribution
- **LGPL** (e.g., NautilusTrader) — Yes, but modifications to the library itself must be open-sourced
- **GPL** — Your entire project may need to be open-sourced if you link to the library
- **Source-available / BSL** (e.g., some Redis distributions) — Check current terms; may have restrictions

---

## Data Quality

**Q: What's the difference between adjusted and unadjusted prices?**

A: **Adjusted prices** account for corporate actions (splits, dividends, spin-offs) so that historical charts reflect true returns. **Unadjusted prices** show the actual traded price at the time. For backtesting, you almost always want adjusted prices. Always verify which one a provider delivers.

**Q: How do I handle survivorship bias?**

A: Survivorship bias occurs when your dataset only contains companies that are *still alive*, ignoring delisted ones. This inflates backtested returns. To mitigate:
- Use providers with **delisted ticker coverage** (e.g., Databento, Massive)
- Maintain a **point-in-time** database of ticker changes
- Be explicit about this limitation in your research

**Q: What is look-ahead bias?**

A: Using information in a backtest that would not have been available at the decision time. Common examples:
- Using **end-of-day** data before the market closes
- Using **revised** economic data instead of **initial release**
- Using **full-sample** mean/variance in a rolling strategy

Always model **event time** — the moment information actually becomes available.

---

## Security

**Q: How do I safely store API keys?**

A: **Never hardcode API keys in your scripts.**

Best practices:
1. Use environment variables (`os.environ['API_KEY']`)
2. Use a secrets manager (AWS Secrets Manager, HashiCorp Vault, 1Password CLI)
3. Use `.env` files that are **gitignored**
4. Rotate keys regularly
5. Use **IP whitelisting** where available
6. Use **read-only** keys for data-only workflows
7. Enable **2FA** on all exchange accounts

**Q: What permissions should I give API keys?**

A: Principle of least privilege:
| Workflow | Minimum Permissions |
|---|---|
| Data collection only | Read-only market data |
| Paper trading | Trading (simulated) + read |
| Live trading (conservative) | Spot trading + read, no withdrawals |
| Live trading (full) | Trading + read, withdrawals only via manual approval |

Never enable **withdrawal** permissions on API keys used by automated systems unless absolutely necessary.

---

## Contributing

**Q: How do I suggest a new service?**

A: See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome pull requests for:
- New services with public APIs or active open-source development
- Pricing updates (with a source link)
- SDK links for additional languages
- Corrections to descriptions or coverage labels

**Q: Why is my favorite tool not on the list?**

A: Possible reasons:
- It may not have a public API or active open-source repository
- It may have been deprioritized due to maintenance concerns
- It may be covered by a more general entry (e.g., CCXT covers many individual exchange wrappers)
- The editorial ranking may have placed it outside the top 99

Feel free to open an issue with justification.

---

## Legal & Regulatory

**Q: Can I legally use these APIs for automated trading in my country?**

A: **This list does not provide legal advice.** Regulations vary dramatically:
- **U.S.** — SEC, CFTC, and FINRA rules apply; pattern-day-trader rules for equities; accredited-investor requirements for some products
- **EU / UK** — MiFID II, GDPR (for data handling), ESMA leverage limits on CFDs
- **Other jurisdictions** — Check local securities and data-protection laws

Consult a qualified attorney before deploying automated trading systems.

**Q: Is the data on this list allowed for commercial use?**

A: Every provider has different terms. "Free tier" does **not** automatically mean "commercial use allowed." Always read the provider's Terms of Service, especially:
- Redistribution restrictions
- Display requirements (attribution, delayed vs. real-time labeling)
- Derivative works clauses

---

## Troubleshooting

**Q: My API requests are being rate-limited. What do I do?**

A:
1. Check the provider's rate-limit documentation (usually measured in requests/second or requests/minute)
2. Implement **exponential backoff** with jitter
3. Use **WebSocket** feeds instead of polling REST endpoints
4. Cache responses when the data doesn't change frequently
5. Consider upgrading to a paid plan

**Q: My backtest results look too good. What am I doing wrong?**

A: Common culprits:
- **Look-ahead bias** — using future information
- **Survivorship bias** — only testing on currently-listed assets
- **Overfitting** — too many parameters relative to data points
- **Ignoring transaction costs** — commissions, slippage, market impact
- **Unrealistic liquidity assumptions** — assuming you can trade unlimited size at the last price

See Section 8 (Backtesting) for tools that help mitigate these issues.
