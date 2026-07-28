# Awesome Trading Services, Market Data APIs & Crypto Analytics

![Trading awesome](https://i.postimg.cc/SstfKwXF/trading-awesome-github.jpg)

> A curated directory of **90+ trading services and open-source tools** for algorithmic traders, quantitative researchers, developers, and active investors. It covers broker and exchange APIs, stock and forex data, cryptocurrency market data, on-chain analytics, signal intelligence, backtesting, portfolio analytics, AI research, feature engineering, infrastructure, and financial visualization.

Reliable trading infrastructure is a prerequisite for serious research and automation. This SEO-friendly Awesome List makes it easier to compare **market-data APIs**, **brokerage APIs**, **crypto exchange APIs**, **forex platforms**, and **on-chain analytics tools** without treating fundamentally different products as interchangeable. It is intended as a practical discovery resource—not as an endorsement or a trading recommendation.

The list is ranked by **editorial practical significance** as of **27 July 2026**. The ranking weighs breadth and reliability of data or execution capability, API maturity, developer ecosystem, workflow relevance, distinctive specialization, and public accessibility. The rank is deliberately not a claim about market share, investment returns, or the quality of any individual strategy.

## 📚 Supplementary Guides

In addition to the main directory, this repository includes focused guides for specific needs:

| Guide | Who it's for | What it covers |
|-------|-------------|----------------|
| [🚀 Quick Start Guide](QUICKSTART.md) | Beginners | Step-by-step paths to your first backtest, paper trade, or data fetch in under 30 minutes |
| [⚖️ Detailed Comparisons](COMPARISON.md) | Evaluators | Side-by-side matrices across brokers, data APIs, crypto exchanges, backtesters, and more |
| [❓ FAQ](FAQ.md) | Everyone | Answers to common questions about choosing services, pricing, data quality, security, and legal |
| [🤝 Contributing](CONTRIBUTING.md) | Contributors | How to propose new entries, update pricing, and follow the editorial criteria |

---

## Table of Contents

| Section | What it covers |
| --- | --- |
| [How to use this list](#how-to-use-this-list) | Coverage labels, API and SDK conventions, and pricing caveats |
| [1. Brokerage, execution & algorithmic trading](#1-brokerage-execution--algorithmic-trading) | Multi-asset brokers, trading platforms, and automation frameworks |
| [2. Traditional markets, macro & multi-asset data](#2-traditional-markets-macro--multi-asset-data) | Equities, options, futures, forex, fundamentals, macro, and news APIs |
| [3. Crypto exchange APIs & interoperability](#3-crypto-exchange-apis--interoperability) | Programmatic spot and derivatives execution |
| [4. Crypto market intelligence & on-chain analytics](#4-crypto-market-intelligence--on-chain-analytics) | On-chain, DeFi, derivatives, social, and wallet intelligence |
| [5. Charting, research & no-code decision support](#5-charting-research--no-code-decision-support) | Visual research, dashboards, AI analysis, and no-code strategy tools |
| [6. Signal providers & event intelligence](#6-signal-providers--event-intelligence) | Alerts, news events, sentiment, strategy triggers, and signal routing |
| [7. Trading infrastructure & event-driven systems](#7-trading-infrastructure--event-driven-systems) | Databases, streams, messaging, metrics, and operational dashboards |
| [8. Backtesting engines & trading frameworks](#8-backtesting-engines--trading-frameworks) | Research engines, simulation, paper trading, and live deployment frameworks |
| [9. Portfolio analytics & risk](#9-portfolio-analytics--risk) | Performance reports, allocation, risk models, and portfolio optimization |
| [10. AI & machine-learning frameworks](#10-ai--machine-learning-frameworks) | Financial ML, reinforcement learning, LLM research, and agent orchestration |
| [11. Feature engineering & technical analysis](#11-feature-engineering--technical-analysis) | Indicators, time-series features, labeling, and research transformations |
| [12. Financial visualization](#12-financial-visualization) | Embeddable charts, dashboards, candlesticks, and research graphics |
| [Which service should I choose?](#which-service-should-i-choose) | Practical starting points for common trading and research tasks |
| [Reference links](#reference-links) | Primary provider documentation and pricing sources |

---

## How to use this list

Every entry links to the provider's official site. The **API & packages** column always points to public documentation when a public API is available. `Py`, `Go`, and `PHP` link to a GitHub package only when a relevant repository could be identified. Packages marked **community** are not represented as first-party software; validate maintenance, licensing, security, and compatibility before production use.

| Coverage label | Meaning |
| --- | --- |
| **Crypto — spot / on-chain / DeFi** | Digital-asset spot markets, blockchain data, stablecoins, decentralized finance, or NFT-related data where applicable |
| **Crypto — derivatives** | Perpetual futures, futures, options, funding, liquidations, open interest, or related market structure |
| **Traditional markets** | Equities, ETFs, options, futures, bonds, indices, fundamentals, filings, or financial news |
| **Forex / FX** | Spot FX, exchange rates, CFDs where legally available, or FX market data |
| **Brokerage / execution** | Programmatic orders, account access, paper trading, portfolio operations, or direct market access |
| **Research / automation** | Backtesting, charting, analytics, alerts, no-code workflows, or developer infrastructure |

> **Pricing convention.** Prices are public entry prices or plan descriptions reported by providers at the reference date. They may change by region, exchange, data-entitlement, billing interval, user type, and promotional terms. "Custom" or "contact sales" means no reliable public price was found; it does not mean the product is free.

---

## 1. Brokerage, execution & algorithmic trading

These tools are the strongest starting points when a workflow needs more than data: they support automated orders, brokerage integration, paper/live trading, or research-to-execution deployment. Regulatory eligibility and supported instruments can differ by country, account type, and product entity.[1] [3] [4]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 1 | **[Interactive Brokers](https://www.interactivebrokers.com/)** [1] | Global electronic broker with web, TWS, Excel, and FIX interfaces for custom trading workflows. | Traditional markets; Forex / FX; multi-asset; Brokerage / execution | [API docs](https://www.interactivebrokers.com/campus/ibkr-api-page/ibkr-api-home/) · Py: [official TWS API](https://github.com/InteractiveBrokers/tws-api-public) · Go: — · PHP: — | Trading commissions and market-data subscriptions vary by account, venue, and region; see [official pricing](https://www.interactivebrokers.com/en/pricing/commissions-home.php). |
| 2 | **[Alpaca](https://alpaca.markets/)** [2] | Developer-first trading, brokerage, and market-data platform built for algorithmic equity, options, and crypto workflows. | U.S. equities / ETFs / options; crypto; Brokerage / execution | [API docs](https://docs.alpaca.markets/) · Py: [official](https://github.com/alpacahq/alpaca-py) · Go: [official](https://github.com/alpacahq/alpaca-trade-api-go) · PHP: — | Commission-free U.S. stock/ETF trading is advertised; market-data plans include free and paid tiers, including a $99/month plan. |
| 3 | **[QuantConnect](https://www.quantconnect.com/)** [3] | Open-source algorithmic-trading platform for research, backtesting, optimization, and live deployment through broker integrations. | Traditional markets; Forex / FX; crypto; Research / automation | [Docs](https://www.quantconnect.com/docs/v2/) · Py/C#: [official LEAN engine](https://github.com/QuantConnect/Lean) · Go: — · PHP: — | Free plan; public individual plans start at **$84/month**. |
| 4 | **[MetaTrader 5](https://www.metatrader5.com/)** [4] | Multi-asset platform widely used through brokers for FX, CFDs, exchange-traded instruments, indicators, and automated trading. | Forex / FX; traditional markets; Research / automation | [Python integration docs](https://www.mql5.com/en/docs/python_metatrader5) · Py: platform package · Go: — · PHP: — | Platform access is generally broker-mediated; the terminal is free, while marketplace, hosting, signals, and broker costs vary. |
| 5 | **[OANDA](https://www.oanda.com/)** [5] | Regulated broker and FX platform with v20 REST API support for account, pricing, and trading workflows. | Forex / FX; CFDs and region-dependent instruments; Brokerage / execution | [v20 docs](https://developer.oanda.com/rest-live-v20/introduction/) · Py: [official](https://github.com/oanda/v20-python) · Go: — · PHP: — | Spread, commission, financing, and product availability are jurisdiction-specific; [official pricing](https://www.oanda.com/) applies by entity. |
| 6 | **[cTrader](https://ctrader.com/)** [6] | Broker-connected trading platform for charting, copy trading, cBots, and programmatic execution through Open API. | Forex / FX; CFDs; broker-dependent multi-asset execution | [Open API docs](https://help.ctrader.com/open-api/) · Py: [official](https://github.com/spotware/OpenApiPy) · Go: [community](https://github.com/diegobernardes/ctrader) · PHP: — | Core platform is commonly supplied through brokers; cBots, indicators, and copy-trading products have varied terms. |
| 7 | **[tastytrade](https://tastytrade.com/)** [7] | Active-trader brokerage emphasizing U.S. options and futures, with a public developer platform and Python SDK. | U.S. stocks / ETFs / options / futures; crypto; Brokerage / execution | [Developer docs](https://developer.tastytrade.com/) · Py: [official](https://github.com/tastytrade/tastytrade-sdk-python) · Go: — · PHP: — | U.S. stocks/ETFs: $0 commission; public options pricing is **$1/contract, capped at $10/leg**; other product fees apply. |
| 8 | **[Tradier](https://tradier.com/)** [8] | API-centric U.S. equities and options brokerage offering trading, account, and market-data endpoints. | U.S. equities / ETFs / options; Brokerage / execution | [API docs](https://docs.tradier.com/) · Py: [community](https://github.com/cablehead/python-tradier) · Go: [community](https://github.com/timpalpant/go-tradier) · PHP: — | Brokerage subscriptions publicly start at **$10/month**; commissions and exchange fees depend on plan and activity. |
| 9 | **[CCXT](https://github.com/ccxt/ccxt)** [9] | Open-source unified API library that normalizes market-data and trading interfaces across many crypto exchanges. | Crypto — spot / on-chain / DeFi; Crypto — derivatives; Research / automation | [Docs](https://docs.ccxt.com/) · Py: [official](https://github.com/ccxt/ccxt/tree/master/python) · Go: [official](https://github.com/ccxt/ccxt/tree/master/go) · PHP: [official](https://github.com/ccxt/ccxt/tree/master/php) | Open-source core; **CCXT Pro** WebSocket plans are publicly listed from **$79/month**. |

---

## 2. Traditional markets, macro & multi-asset data

For quantitative strategies and investment research, data quality depends on more than an endpoint count. Verify entitlement terms, adjustment basis, exchange coverage, latency, corporate-action treatment, and whether a data field is real-time, delayed, end-of-day, or derived. These providers span a practical range from accessible developer APIs to specialist institutional feeds.[10] [15] [16]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 10 | **[Finnhub](https://finnhub.io/)** [10] | Broad REST and WebSocket API for market prices, fundamentals, news, estimates, filings, alternatives, forex, and crypto. | Traditional markets; Forex / FX; crypto; Research / automation | [API docs](https://finnhub.io/docs/api) · Py: [official](https://github.com/Finnhub-Stock-API/finnhub-python) · Go: [official](https://github.com/Finnhub-Stock-API/finnhub-go) · PHP: [official](https://github.com/Finnhub-Stock-API/finnhub-php) | Free tier; public All-in-One plan listed at **$3,500/month billed annually**. |
| 11 | **[Twelve Data](https://twelvedata.com/)** [11] | Global market-data API and WebSocket service for equities, forex, crypto, ETFs, funds, indicators, fundamentals, and reference data. | Traditional markets; Forex / FX; crypto; multi-asset | [API docs](https://twelvedata.com/docs) · Py: [official](https://github.com/twelvedata/twelvedata-python) · Go: [official](https://github.com/twelvedata/twelvedata-go) · PHP: [community](https://github.com/ingelby/twelvedata) | Free Basic tier; public paid plans start at **$79/month billed annually**. |
| 12 | **[Massive](https://massive.com/)** [12] | Real-time and historical market-data platform, formerly Polygon.io, with REST, WebSocket, and flat-file delivery. | U.S. equities; options; indices; FX; futures; crypto | [Docs](https://massive.com/docs) · Py: [official](https://github.com/massive-com/client-python) · Go: [official](https://github.com/massive-com/client-go) · PHP: — | Free tier; individual plans publicly start at **$29/month**. |
| 13 | **[Alpha Vantage](https://www.alphavantage.co/)** [13] | Accessible API for equity, ETF, FX, crypto, economic, technical-indicator, and fundamental data. | Traditional markets; Forex / FX; crypto; Research / automation | [API docs](https://www.alphavantage.co/documentation/) · Py: [community](https://github.com/RomelTorres/alpha_vantage) · Go: [community](https://github.com/masonJamesWheeler/alpha-vantage-go-wrapper) · PHP: [community](https://github.com/kokspflanze/alpha-vantage-api) | Free tier is publicly limited to **25 requests/day**; premium plans start at **$49.99/month**. |
| 14 | **[Financial Modeling Prep](https://site.financialmodelingprep.com/)** [14] | Developer-focused source for market, fundamental, technical, economic, forex, crypto, and company-financial datasets. | Traditional markets; Forex / FX; crypto | [API docs](https://site.financialmodelingprep.com/developer/docs) · Py: [community](https://github.com/daxm/fmpsdk) · Go: — · PHP: — | Free tier; public paid plans start at **$22/month billed annually**. |
| 15 | **[EODHD](https://eodhd.com/)** [15] | API provider for global end-of-day, intraday, real-time, fundamental, FX, and crypto datasets. | Traditional markets; Forex / FX; crypto | [Financial API docs](https://eodhd.com/financial-apis/) · Py: [official](https://github.com/EodHistoricalData/EODHD-APIs-Python-Financial-Library) · Go: [eodhd-go](https://github.com/tigusigalpa/eodhd-go) · PHP: [official](https://github.com/EodHistoricalData/EODHistoricalData.PHP-Laravel) | Free tier; publicly listed plans begin at **$19.99/month**. |
| 16 | **[Databento](https://databento.com/)** [16] | Exchange-sourced historical and real-time market-data platform with standardized schemas for systematic workflows. | Equities; futures; options; FX; Traditional markets | [Docs](https://databento.com/docs) · Py: [official](https://github.com/databento/databento-python) · Go: — · PHP: — | Usage-based historical data; public plans include **$199/month** Standard, with free signup credits. |
| 17 | **[Tiingo](https://www.tiingo.com/)** [17] | API platform for equities, end-of-day pricing, news, fundamentals, IEX data, forex, and crypto. | Traditional markets; Forex / FX; crypto | [Docs](https://www.tiingo.com/documentation/) · Py: [community](https://github.com/hydrosquall/tiingo-python) · Go: [community](https://github.com/condrove10/go-tiingo-sdk) · PHP: — | Free Starter plan; Power and Commercial tiers are published by use case. |
| 18 | **[Intrinio](https://intrinio.com/)** [18] | Structured fundamentals, U.S. equities, options, and real-time financial data API for developers and enterprises. | Traditional markets; options; fundamentals | [API docs](https://docs.intrinio.com/documentation/api_v2/getting_started) · Py: [official](https://github.com/intrinio/python-sdk) · Go: [official](https://github.com/intrinio/intrinio-realtime-go-sdk) · PHP: — | Free trial; public individual plan starts at **$150/month**. |
| 19 | **[Barchart](https://www.barchart.com/)** [19] | Market-data, news, charting, and OnDemand API provider with extensive exchange and reference-data coverage. | Traditional markets; Forex / FX; crypto | [OnDemand API](https://www.barchart.com/ondemand/api) · Py: [official](https://github.com/barchart/barchart-ondemand-client-python) · Go: — · PHP: [official](https://github.com/barchart/barchart-ondemand-client-php) | Data packages and OnDemand access vary; public end-of-day data is listed from **$49/month**. |
| 20 | **[Nasdaq Data Link](https://data.nasdaq.com/)** [20] | Dataset marketplace and API for financial, economic, and alternative-data series. | Traditional markets; macro; alternative data | [Docs](https://docs.data.nasdaq.com/) · Py: [official](https://github.com/nasdaq/data-link-python) · Go: — · PHP: — | Freemium; selected datasets are free while premium datasets require separate subscriptions. |
| 21 | **[Trading Economics](https://tradingeconomics.com/)** [21] | Macroeconomic and market-data platform for indicators, calendars, forecasts, commodities, bonds, currencies, and APIs. | Macro; Forex / FX; Traditional markets | [API docs](https://docs.tradingeconomics.com/) · Py: [official](https://github.com/tradingeconomics/tradingeconomics-python) · Go/PHP: [official multi-language repo](https://github.com/tradingeconomics/tradingeconomics) | Public Basic plan starts at **$22/month billed annually**. |
| 22 | **[Marketstack](https://marketstack.com/)** [22] | REST API for end-of-day, intraday, and real-time equities data, designed for lightweight integrations. | Traditional markets; equities / ETFs | [API docs](https://docs.apilayer.com/marketstack/docs/api-documentation) · Py: [community](https://github.com/mreiche/marketstack-python) · Go: [community](https://github.com/tigusigalpa/marketstack-go) · PHP: [community](https://github.com/tigusigalpa/marketstack-php) | Free tier; public paid tiers start at **$9.99/month**. |
| 23 | **[Unusual Whales](https://unusualwhales.com/)** [23] | Options-flow, dark-pool, congressional-trading, and market-analysis platform with a public API. | U.S. options; equities; Research / automation | [API docs](https://api.unusualwhales.com/docs) · Py: — · Go: — · PHP: — | Retail plans publicly start at **$42/month billed annually**; enterprise begins at **$750/month**. |
|  | **[DepthFeed](https://depthfeed.com/)** [99] | Historical and live prediction-market order-book data for systematic backtesting and liquidity analysis. | Research / automation | [API docs](https://depthfeed.com/docs) · [MCP](https://github.com/vcorp-dev/depthfeed-mcp) · Py/Go/PHP: — | Free Explorer tier; paid plans are listed on the [official pricing page](https://depthfeed.com/pricing). |

---

## 3. Crypto exchange APIs & interoperability

Exchange APIs combine public market-data feeds with private account and order endpoints. They are powerful but operationally sensitive: use IP restrictions, least-privilege keys, subaccounts, testnet/paper environments where available, and exchange-specific rate-limit handling. Availability, leverage, derivatives access, and fees can be restricted by jurisdiction.[24] [25] [26]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 24 | **[Binance API](https://developers.binance.com/)** [24] | Official developer surface for Binance spot, derivatives, market-data, and account/trading workflows. | Crypto — spot / on-chain / DeFi; Crypto — derivatives; Brokerage / execution | [Spot API docs](https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG) · Py: [official](https://github.com/binance/binance-connector-python) · Go: [official](https://github.com/binance/binance-connector-go) · PHP: [official](https://github.com/binance/binance-connector-php) | API use is free; exchange trading fees and product access vary by venue and jurisdiction. |
| 25 | **[Coinbase Advanced Trade API](https://www.coinbase.com/developer-platform/products/advanced-trade-api)** [25] | Coinbase API for programmatic spot trading, order management, market data, and eligible derivatives functionality. | Crypto — spot; eligible derivatives; Brokerage / execution | [API docs](https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/overview) · Py: [official](https://github.com/coinbase/coinbase-advanced-py) · Go: — · PHP: — | API access is free; public Advanced Trade maker/taker fees start at **0.60% / 1.20%**, subject to volume and product. |
| 26 | **[Kraken API](https://www.kraken.com/)** [26] | REST, WebSocket, and FIX interfaces for crypto trading, market data, and institutional workflows. | Crypto — spot; Crypto — derivatives; Brokerage / execution | [API docs](https://docs.kraken.com/api/) · Py: [official](https://github.com/krakenfx/kraken-wsclient-py) · Go: [official](https://github.com/krakenfx/api-go) · PHP: [official](https://github.com/krakenfx/kraken-api-client) | API access is included with an account; exchange fees and product availability vary by geography. |
| 27 | **[Bybit API](https://www.bybit.com/)** [27] | Unified V5 API for crypto spot, derivatives, options, account, and trading endpoints. | Crypto — spot; Crypto — derivatives; Brokerage / execution | [V5 docs](https://bybit-exchange.github.io/docs/v5/intro) · Py: [official](https://github.com/bybit-exchange/pybit) · Go: [bybit-go](https://github.com/tigusigalpa/bybit-go) · PHP: [bybit-php](https://github.com/tigusigalpa/bybit-php) | API access is free; trading fees and product availability vary by market and jurisdiction. |
| 28 | **[OKX API](https://www.okx.com/)** [28] | Exchange API for spot, margin, futures, swaps, options, wallets, and market data. | Crypto — spot / DeFi; Crypto — derivatives; Brokerage / execution | [API portal](https://www.okx.com/okx-api) · Py: [official](https://github.com/okxapi/python-okx) · Go: [okx-go](https://github.com/tigusigalpa/okx-go) · PHP: [okx-php](https://github.com/tigusigalpa/okx-php) | API access is free; trading fees are tiered by volume, account, and instrument. |
| 29 | **[Hyperliquid](https://hyperliquid.xyz/)** [29] | Fully on-chain exchange infrastructure with perpetual-futures and spot order books plus a developer API. | Crypto — spot / DeFi; Crypto — derivatives; Brokerage / execution | [API docs](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api) · Py: [official](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) · Go: — · PHP: — | Public base fees include **0.015% maker / 0.045% taker** for perpetuals; discounts and conditions apply. |
| 30 | **[BingX](https://bingx.com)** | BingX — crypto exchange offering spot, futures, and copy trading for global users. | Crypto — spot / DeFi; Crypto — derivatives; Brokerage / execution | [API docs](https://bingx-api.github.io/docs-v3/#/en/info) · Py: [bingx-python](https://github.com/tigusigalpa/bingx-python) · Go: [bingx-go](https://github.com/tigusigalpa/bingx-go) · PHP: [bingx-php](https://github.com/tigusigalpa/bingx-php) | Public base fees include **0.015% maker / 0.045% taker** for perpetuals; discounts and conditions apply. |

---

## 4. Crypto market intelligence & on-chain analytics

On-chain analytics and crypto intelligence tools help traders evaluate network activity, wallet behavior, exchange flows, token economics, liquidation risk, social attention, and decentralized-finance activity. These signals are contextual rather than deterministic; they should be combined with market structure, liquidity, and risk controls rather than treated as standalone trade triggers.[30] [31] [32]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 31 | **[CoinGecko](https://www.coingecko.com/)** [30] | Independent crypto-data API covering prices, market capitalizations, exchange and asset metadata, DEX/on-chain data, WebSocket, and webhooks. | Crypto — spot / on-chain / DeFi; Crypto — derivatives | [API docs](https://docs.coingecko.com/) · Py: [official](https://github.com/coingecko/coingecko-python) · Go: [coingecko-go](https://github.com/tigusigalpa/coingecko-go) · PHP: [coingecko-php](https://github.com/tigusigalpa/coingecko-php) | Free Demo API; public paid API plans start at **$29/month billed annually**. |
| 32 | **[CoinMarketCap](https://coinmarketcap.com/)** [31] | Widely used cryptocurrency market-data aggregator with API access to listings, quotes, metadata, and market metrics. | Crypto — spot; market data | [API docs](https://coinmarketcap.com/api/documentation/) · Py: — · Go: [coinmarketcap-go](https://github.com/tigusigalpa/coinmarketcap-go) · PHP: [coinmarketcap-php](https://github.com/tigusigalpa/coinmarketcap-php) | Free Basic plan; public paid API tiers start at **$29/month**. |
| 33 | **[CoinGlass](https://www.coinglass.com/)** [32] | Crypto market-structure platform for futures, options, funding, open interest, liquidations, order books, ETF flows, and on-chain indicators. | Crypto — derivatives; spot; on-chain | [API docs](https://docs.coinglass.com/reference/getting-started-with-your-api) · Py: — · Go: [coinglass-go](https://github.com/tigusigalpa/coinglass-go) · PHP: [coinglass-php](https://github.com/tigusigalpa/coinglass-php) | Public API plans start at **$29/month**; enterprise is custom. |
| 34 | **[Glassnode](https://glassnode.com/)** [33] | Digital-asset intelligence platform combining on-chain and market metrics, research, and API-accessible data. | Crypto — spot / on-chain / DeFi; Crypto — derivatives | [API docs](https://docs.glassnode.com/basic-api/api) · Py: [official](https://github.com/glassnode/glassnode-api-python-client) · Go: — · PHP: — | Advanced dashboard plan publicly starts at **$49/month billed annually**; API/professional access varies by package. |
| 35 | **[Nansen](https://nansen.ai/)** [34] | Wallet labels, entity intelligence, dashboards, and programmatic on-chain data across supported blockchain networks. | Crypto — on-chain / DeFi / NFTs / stablecoins | [API docs](https://docs.nansen.ai/) · Py: — · Go: [nansen-go](https://github.com/tigusigalpa/nansen-go) · PHP: [nansen-php](https://github.com/tigusigalpa/nansen-php) | Pro is publicly listed from **$49/month billed annually**; API credits are separately metered. |
| 36 | **[CryptoQuant](https://cryptoquant.com/)** [35] | On-chain and exchange-flow analytics platform with market metrics, charts, alerts, and data APIs for crypto research. | Crypto — on-chain; Crypto — derivatives | [API docs](https://docs.cryptoquant.com/) · Py: — · Go: — · PHP: — | Free tier; public paid plans start at **$29/month billed annually**. |
| 37 | **[Dune](https://dune.com/)** [36] | SQL-oriented on-chain data platform for querying, visualizing, sharing, and programmatically consuming blockchain analytics. | Crypto — on-chain / DeFi / NFTs; Research / automation | [API docs](https://docs.dune.com/api-reference/overview/introduction) · Py: [official](https://github.com/duneanalytics/dune-client) · Go: [official](https://github.com/duneanalytics/duneapi-client-go) · PHP: — | Free plan includes public monthly credits; paid Analyst, Plus, and Enterprise plans are credit-based. |
| 38 | **[Coin Metrics](https://www.talos.com/our-solutions/data/overview)** [37] | Institutional digital-asset market and network-data service, now presented within Talos data solutions. | Crypto — spot / on-chain; reference rates; indexes | [API docs](https://docs.coinmetrics.io/api/v4/) · Py: [official](https://github.com/coinmetrics/api-client-python) · Go: — · PHP: — | Community access exists for selected data; commercial pricing is contact sales. |
| 39 | **[Kaiko](https://www.kaiko.com/)** [38] | Institutional crypto market-data, derivatives, index, and analytics provider for research, risk, and trading workflows. | Crypto — spot; Crypto — derivatives; market data | [API docs](https://docs.kaiko.com/) · Py: — · Go: [official](https://github.com/kaikodata/kaiko-go-sdk) · PHP: — | Enterprise-focused; pricing is on request. |
| 40 | **[Messari](https://messari.io/)** [39] | Crypto research and intelligence platform providing protocol, asset, market, and selected API data. | Crypto — spot / on-chain / DeFi; research | [API docs](https://docs.messari.io/introduction) · Py: [official](https://github.com/messari/messari-python-api) · Go: — · PHP: [community](https://github.com/codenix-sv/messari-api) | Public/free access exists for selected content; advanced data and enterprise terms are plan-dependent. |
| 41 | **[Santiment](https://santiment.net/)** [40] | Behavioral crypto-intelligence platform combining social, on-chain, development, NFT, and market metrics. | Crypto — on-chain / DeFi / NFTs; social intelligence | [SANAPI docs](https://academy.santiment.net/sanapi/) · Py: [official](https://github.com/santiment/sanpy) · Go: — · PHP: — | Free plan; paid Sanbase and business tiers are published by product. |
| 42 | **[DeFiLlama](https://defillama.com/)** [41] | Open DeFi analytics ecosystem for TVL, yields, protocol revenue, fees, DEX volumes, bridges, stablecoins, and chains. | Crypto — on-chain / DeFi / stablecoins | [API docs](https://api-docs.defillama.com/) · Py: — · Go: — · PHP: — | Core data API is publicly accessible; premium/commercial terms are not consistently published. |
| 43 | **[Arkham](https://arkhamintelligence.com/)** [42] | Blockchain intelligence service for entity labels, wallet activity, transaction tracing, and on-chain research. | Crypto — on-chain; wallet intelligence | [API docs](https://arkm.com/api/docs) · Py: — · Go: — · PHP: — | API access is application/pilot based; public pricing was not identified. |
| 44 | **[Whale Alert](https://whale-alert.io/)** [43] | Real-time large-transaction monitoring and blockchain analytics via alert streams and enterprise REST data. | Crypto — on-chain; stablecoins; alerts | [API docs](https://developer.whale-alert.io/api-account/documentation) · Py: code examples only · Go: code examples only · PHP: — | Alerts API: **$29.95/month**; Enterprise API: **$699/month**. |
| 45 | **[LunarCrush](https://lunarcrush.com/)** [44] | Social and market-intelligence service for crypto and broader trending assets, with developer endpoints. | Crypto; social intelligence; selected traditional assets | [Developer API](https://lunarcrush.com/en/developers/api) · Py: — · Go: [lunarcrush-go](https://github.com/tigusigalpa/lunarcrush-go) · PHP: [lunarcrush-php](https://github.com/tigusigalpa/lunarcrush-php) | Hobby free tier; paid developer plans publicly start at **$5/day**. |
| 46 | **[CoinAPI](https://www.coinapi.io/)** [45] | Unified crypto market-data service for exchange rates, trades, order books, OHLCV, and indexes. | Crypto — spot; Crypto — derivatives; market data | [API docs](https://docs.coinapi.io/) · Py: no verified official GitHub package · Go: — · PHP: — | Free credits; public paid plans start at **$249/month**. |

---

## 5. Charting, research & no-code decision support

These services are valuable to discretionary and hybrid workflows even when they do not provide a general public trading API. They prioritize charting, dashboards, research, portfolio views, AI-assisted analysis, or no-code strategy experimentation. API access should never be inferred from a web dashboard, embedded widget, Pine Script environment, or broker integration.[46] [47]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 47 | **[TradingView](https://www.tradingview.com/)** [46] | Mainstream charting, screening, market-data visualization, alerting, and Pine Script platform across many asset classes. | Traditional markets; Forex / FX; crypto; Research / automation | No general public data/indicator API for personal use · [Pine Script docs](https://www.tradingview.com/pine-script-docs/) · Py: — · Go: — · PHP: — | Free tier; public paid plans range from **$12.95/month to $199.95/month billed annually**. |
| 48 | **[Koyfin](https://www.koyfin.com/)** [47] | Financial research workspace for market dashboards, portfolio analysis, company fundamentals, and reporting. | Traditional markets; fundamentals; Research | No public API identified · Py: — · Go: — · PHP: — | Free, Plus **$39/month**, Premium **$79/month**, with higher advisor tiers. |
| 49 | **[CoinQuant](https://www.coinquant.ai/)** [48] | No-code, AI-assisted strategy builder and backtesting platform for market research and systematic experimentation. | Crypto; traditional markets; Research / automation | [Public API skills pack](https://www.coinquant.ai/documentation/public-api-skills-pack) · Py: — · Go: — · PHP: — | Free credits; public paid plans listed from **$12.99/week**. |
| 50 | **[TradingCursor](https://www.tradingcursor.com/)** [49] | AI-assisted multi-signal research product for stocks, ETFs, forex, and crypto decision support. | Traditional markets; Forex / FX; crypto; Research | No public API identified · Py: — · Go: — · PHP: — | Free daily analysis; Pro is publicly listed at **$9.90/month**. |
| 51 | **[LONA™](https://www.lona.agency/en)** [50] | No-code AI trading assistant for creating, backtesting, and optimizing trading ideas. | Traditional markets; Forex / FX; crypto; Research / automation | No public API identified · Py: — · Go: — · PHP: — | Free tier; Pro **$49/month**, Premium **$99/month**, Quant **$249/month**. |

---

## 6. Signal providers & event intelligence

A signal is an input to a decision process, not a promise of profit. This section prioritizes tools that turn price action, indicators, news, sentiment, or user-defined rules into alerts and machine-readable events. Before automating an action, test for repainting, duplicate delivery, stale events, clock drift, webhook retries, and the difference between an informational alert and an executable order instruction.[51] [53] [57]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 52 | **[TrendSpider](https://trendspider.com/)** [51] | Technical-analysis workspace with scanners, multi-factor alerts, strategy testing, cloud strategy bots, and outbound webhooks. | Traditional markets; Forex / FX; crypto; Research / automation | [Webhook docs](https://help.trendspider.com/articles/webhooks) · No general market-data API identified · Py/Go/PHP: — | Paid subscriptions; plan limits govern alerts, bots, data, and webhook availability. |
| 53 | **[LuxAlgo](https://www.luxalgo.com/)** [52] | TradingView-centered indicator, screener, backtesting, and alert toolkits with configurable technical and price-action signals. | Traditional markets; Forex / FX; crypto; Research | [Docs](https://docs.luxalgo.com/docs/getting-started/introduction) · Delivered primarily through TradingView · Py/Go/PHP: — | Free and paid indicator access; current plan terms are published on the provider site. |
| 54 | **[CryptoPanic](https://cryptopanic.com/)** [53] | Crypto news aggregator with currency filters, sentiment/community signals, alerting, and a developer news API. | Crypto; news; sentiment; Research / automation | [API docs](https://cryptopanic.com/developers/api/) · Py/Go/PHP: direct HTTP integration | Paid API plans; public Growth pricing is plan-based and enterprise webhook delivery is separately scoped. |
| 55 | **[Benzinga APIs](https://www.benzinga.com/apis/)** [54] | Financial news, earnings, analyst ratings, calendars, and market-moving event feeds for programmatic workflows. | Traditional markets; news; corporate events | [API docs](https://docs.benzinga.io/) · Py/Go/PHP: direct HTTP integration | Trial and commercial access; dataset pricing and redistribution terms are quote-based. |
| 56 | **[FinancialJuice](https://www.financialjuice.com/)** [55] | Real-time financial news, headlines, economic-calendar events, and audio squawk for event-driven discretionary research. | Macro; Traditional markets; Forex / FX; news | No general public API identified · Py/Go/PHP: — | Free and paid access; real-time features and delay conditions depend on plan. |
| 57 | **[GDELT](https://www.gdeltproject.org/)** [56] | Open global news and event datasets for custom geopolitical, narrative, and media-attention signals. | Global news; macro; alternative data; Research / automation | [DOC API](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) · [data access](https://www.gdeltproject.org/data.html) · Py/Go/PHP: direct HTTP or BigQuery clients | Open datasets and public endpoints; downstream cloud-query or storage charges may apply. |
| 58 | **[SignalStack](https://signalstack.com/)** [57] | Webhook-based order-routing layer that converts alerts from charting and strategy tools into broker orders. | Traditional markets; Forex / FX; crypto; Brokerage / execution | [Documentation](https://help.signalstack.com/) · Webhook integration · Py/Go/PHP: direct HTTP | Usage-based or subscription terms; broker fees remain separate. |

---

## 7. Trading infrastructure & event-driven systems

These are general-purpose infrastructure projects rather than signal generators. They become trading tools when used to ingest ticks, retain historical events, distribute market and order messages, calculate analytics, and monitor production systems. Architecture should follow measured throughput, latency, recovery, ordering, and retention requirements—not fashion.[58] [60] [63]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 59 | **[ClickHouse](https://clickhouse.com/)** [58] | Column-oriented analytical database suited to high-volume tick, order-book, event, and research queries. | Research / automation; market-data storage; analytics | [Docs](https://clickhouse.com/docs) · Py: [official](https://github.com/ClickHouse/clickhouse-connect) · Go: [official](https://github.com/ClickHouse/clickhouse-go) · PHP: [official](https://github.com/ClickHouse/clickhouse-php) | Open-source self-hosting; ClickHouse Cloud is usage-based. |
| 60 | **[QuestDB](https://questdb.com/)** [59] | Time-series database with SQL, high-throughput ingestion, time-series joins, and low-latency queries. | Research / automation; ticks; telemetry; market-data storage | [Docs](https://questdb.com/docs/) · Py/Go/Java/Rust clients are documented · PostgreSQL wire and REST interfaces | Open-source self-hosting; Enterprise and Cloud plans are separately priced. |
| 61 | **[TimescaleDB](https://www.timescale.com/)** [60] | PostgreSQL extension and platform for time-series storage, continuous aggregates, retention, and SQL analytics. | Research / automation; time series; operational analytics | [Docs](https://docs.timescale.com/) · Uses PostgreSQL drivers across Py/Go/PHP | Open-source components and paid cloud service; usage and support terms vary. |
| 62 | **[Redis](https://redis.io/)** [61] | In-memory data platform commonly used for caching, ephemeral state, pub/sub, streams, queues, and rate limiting. | Research / automation; low-latency state; messaging | [Docs](https://redis.io/docs/latest/) · Py: [official](https://github.com/redis/redis-py) · Go: [official](https://github.com/redis/go-redis) · PHP: [community](https://github.com/phpredis/phpredis) | Source-available/community distributions and commercial cloud products have different licenses and prices; review current terms. |
| 63 | **[Apache Kafka](https://kafka.apache.org/)** [62] | Distributed event-streaming platform for durable market-data, order, execution, audit, and downstream processing pipelines. | Research / automation; event streaming; data pipelines | [Docs](https://kafka.apache.org/documentation/) · Py: community clients · Go: community clients · Java: official client | Open source; managed Kafka and operational infrastructure are separately priced. |
| 64 | **[NATS](https://nats.io/)** [63] | Lightweight messaging system with request/reply, pub/sub, and JetStream persistence for event-driven services. | Research / automation; messaging; low-latency services | [Docs](https://docs.nats.io/) · Py: [official](https://github.com/nats-io/nats.py) · Go: [official](https://github.com/nats-io/nats.go) · PHP: [community](https://github.com/basis-company/nats.php) | Open source; Synadia cloud and enterprise support are commercially priced. |
| 65 | **[Prometheus](https://prometheus.io/)** [64] | Metrics collection, querying, and alerting for data feeds, strategy services, execution gateways, and infrastructure. | Research / automation; monitoring; observability | [Docs](https://prometheus.io/docs/introduction/overview/) · HTTP API and client libraries · Go: first-party implementation | Open source; storage, hosting, and managed-service costs depend on deployment. |
| 66 | **[Grafana](https://grafana.com/)** [65] | Dashboarding and alerting platform for market, portfolio, execution, risk, and infrastructure telemetry. | Research / automation; visualization; observability | [Docs](https://grafana.com/docs/grafana/latest/) · HTTP API · broad data-source ecosystem | Open-source self-hosting; Grafana Cloud has free and paid usage tiers. |

---

## 8. Backtesting engines & trading frameworks

Backtests are models of execution, not recordings of achievable returns. Compare engines by data model, event ordering, corporate actions, fee and slippage support, order semantics, portfolio accounting, reproducibility, and the path from research to live deployment. Guard explicitly against look-ahead bias, survivorship bias, overfitting, and unrealistic liquidity assumptions.[66] [67] [68]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 67 | **[NautilusTrader](https://nautilustrader.io/)** [66] | Production-grade, event-driven trading engine spanning deterministic simulation, portfolio/risk modeling, and live execution. | Multi-asset; multi-venue; Research / automation; Brokerage / execution | [Docs](https://nautilustrader.io/docs/latest/) · Py/Rust: [official](https://github.com/nautechsystems/nautilus_trader) · Go/PHP: — | Open source under LGPL; infrastructure, data, and venue costs are separate. |
| 68 | **[vectorbt](https://vectorbt.dev/)** [67] | Vectorized Python research and portfolio simulation framework optimized for exploring many strategy configurations quickly. | Multi-asset research; signal analysis; portfolio simulation | [Docs](https://vectorbt.dev/) · Py: [official](https://github.com/polakowo/vectorbt) · Go/PHP: — | Open-source core; vectorbt PRO is commercial. |
| 69 | **[Freqtrade](https://www.freqtrade.io/)** [68] | Crypto trading bot with strategy development, backtesting, hyperparameter optimization, dry-run, and live exchange execution. | Crypto; Research / automation; Brokerage / execution | [Docs](https://www.freqtrade.io/en/stable/) · Py: [official](https://github.com/freqtrade/freqtrade) · Go/PHP: — | Open source; exchange, hosting, and data costs are separate. |
| 70 | **[Backtrader](https://www.backtrader.com/)** [69] | Mature Python framework for event-driven strategy backtesting, indicators, analyzers, feeds, and broker integrations. | Traditional markets; Forex / FX; crypto; Research / automation | [Docs](https://www.backtrader.com/docu/) · Py: [official](https://github.com/mementum/backtrader) · Go/PHP: — | Open source; maintenance cadence and integrations should be evaluated before production use. |
| 71 | **[Zipline Reloaded](https://zipline.ml4trading.io/)** [70] | Community-maintained continuation of Zipline for event-driven backtesting with pipelines, calendars, and bundle-based data ingestion. | Traditional markets; Research / automation | [Docs](https://zipline.ml4trading.io/) · Py: [community-maintained](https://github.com/stefan-jansen/zipline-reloaded) · Go/PHP: — | Open source; market data and infrastructure are separate. |
| 72 | **[Jesse](https://jesse.trade/)** [71] | Python framework for researching, backtesting, optimizing, and deploying crypto trading strategies. | Crypto; Research / automation; Brokerage / execution | [Docs](https://docs.jesse.trade/) · Py: [official](https://github.com/jesse-ai/jesse) · Go/PHP: — | Open-source framework; commercial extensions or hosted features may have separate terms. |
| 73 | **[Hummingbot](https://hummingbot.org/)** [72] | Open-source framework focused on market making, arbitrage, connector-based crypto execution, backtesting, and bot operations. | Crypto; CEX / DEX; Brokerage / execution; Research / automation | [Docs](https://hummingbot.org/docs/) · Py: [official](https://github.com/hummingbot/hummingbot) · Go/PHP: — | Open source; trading, hosting, liquidity, and connector-specific costs apply. |
| 74 | **[backtesting.py](https://kernc.github.io/backtesting.py/)** [73] | Compact Python library for testing rule-based strategies on OHLC data with optimization and interactive result plots. | Multi-asset research; educational and lightweight backtests | [Docs](https://kernc.github.io/backtesting.py/) · Py: [official](https://github.com/kernc/backtesting.py) · Go/PHP: — | Open source; no hosted execution service is included. |

---

## 9. Portfolio analytics & risk

These libraries answer different questions: some explain realized performance, while others construct allocations under assumptions about expected returns, covariance, constraints, or tail risk. Do not treat an optimizer's precise weights as precise knowledge; validate estimation error, turnover, capacity, costs, constraints, and out-of-sample stability.[74] [75] [76]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 75 | **[QuantStats](https://github.com/ranaroussi/quantstats)** [74] | Python toolkit for return-series metrics, drawdowns, comparisons, tearsheets, and HTML performance reports. | Portfolio analytics; risk; reporting | Py: [official repository](https://github.com/ranaroussi/quantstats) · Go/PHP: — | Open source. |
| 76 | **[Riskfolio-Lib](https://riskfolio-lib.readthedocs.io/)** [75] | Portfolio optimization library supporting many risk measures, risk parity, factor models, constraints, and allocation reports. | Portfolio construction; risk; quantitative research | [Docs](https://riskfolio-lib.readthedocs.io/en/latest/) · Py: [official](https://github.com/dcajasn/Riskfolio-Lib) · Go/PHP: — | Open source; optional commercial solvers and consulting are separate. |
| 77 | **[skfolio](https://skfolio.org/)** [76] | Scikit-learn-compatible framework for portfolio optimization, model selection, cross-validation, stress testing, and risk measurement. | Portfolio construction; risk; ML research | [Docs](https://skfolio.org/user_guide/index.html) · Py: [official](https://github.com/skfolio/skfolio) · Go/PHP: — | Open source; enterprise support is separately available. |
| 78 | **[PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/)** [77] | Python implementation of mean-variance, Black-Litterman, hierarchical risk parity, shrinkage, and related allocation methods. | Portfolio construction; allocation research | [Docs](https://pyportfolioopt.readthedocs.io/en/latest/) · Py: [official](https://github.com/robertmartin8/PyPortfolioOpt) · Go/PHP: — | Open source. |
| 79 | **[empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded)** [78] | Maintained fork of the return and risk-statistics library historically used by the Quantopian analytics ecosystem. | Portfolio analytics; risk metrics; Research | Py: [community-maintained](https://github.com/stefan-jansen/empyrical-reloaded) · Go/PHP: — | Open source; verify compatibility and release cadence. |
| 80 | **[pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded)** [79] | Maintained fork of pyfolio for portfolio and risk tear sheets, exposure analysis, and transaction-level diagnostics. | Portfolio analytics; risk; reporting | Py: [community-maintained](https://github.com/stefan-jansen/pyfolio-reloaded) · Go/PHP: — | Open source; verify compatibility and release cadence. |

---

## 10. AI & machine-learning frameworks

AI frameworks can accelerate forecasting, representation learning, language analysis, research automation, and experimentation, but they do not solve data leakage, non-stationarity, execution costs, or weak validation. Financial LLM and reinforcement-learning projects in particular should be treated as research infrastructure until they pass realistic walk-forward, paper-trading, operational, and risk review.[80] [81] [83]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 81 | **[Microsoft Qlib](https://github.com/microsoft/qlib)** [80] | AI-oriented quantitative-investment platform with data, workflow, model, backtest, portfolio, and experiment-management components. | Traditional markets; quantitative ML; Research / automation | [Docs](https://qlib.readthedocs.io/) · Py: [official](https://github.com/microsoft/qlib) · Go/PHP: — | Open source; data and compute are separate. |
| 82 | **[FinRL-X](https://github.com/AI4Finance-Foundation/FinRL-Trading)** [81] | AI-native modular trading infrastructure positioned as the production-oriented successor to the original FinRL research framework. | Multi-asset; reinforcement learning; Research / automation | Py: [official](https://github.com/AI4Finance-Foundation/FinRL-Trading) · research paper and examples linked from repository · Go/PHP: — | Open source; venue, data, model, and compute costs are separate. |
| 83 | **[FinGPT](https://fingpt.io/)** [82] | Open-source financial LLM project with models and workflows for sentiment, forecasting, retrieval, fine-tuning, and benchmarks. | Financial text; news; sentiment; Research / automation | [Docs](https://fingpt.io/docs) · Py: [official](https://github.com/AI4Finance-Foundation/FinGPT) · models: [Hugging Face](https://huggingface.co/FinGPT) | Open source; hosted APIs, model compute, and enterprise services may be separately priced. |
| 84 | **[FinRL](https://github.com/AI4Finance-Foundation/FinRL)** [83] | Educational and research framework for financial reinforcement-learning environments, agents, datasets, and backtests. | Traditional markets; crypto; reinforcement learning; Research | [Docs](https://finrl.readthedocs.io/) · Py: [official](https://github.com/AI4Finance-Foundation/FinRL) · Go/PHP: — | Open source; the project directs production-oriented users toward FinRL-X. |
| 85 | **[TensorTrade](https://www.tensortrade.org/)** [84] | Modular Python framework for building trading environments, reward/action schemes, agents, portfolios, and RL experiments. | Multi-asset; reinforcement learning; Research | [Docs](https://www.tensortrade.org/) · Py: [official](https://github.com/tensortrade-org/tensortrade) · Go/PHP: — | Open source; verify current maintenance and dependency compatibility. |
| 86 | **[LangGraph](https://langchain-ai.github.io/langgraph/)** [85] | General-purpose framework for durable, stateful agent workflows that can orchestrate research tools, approvals, and human review. | AI orchestration; Research / automation; not trading-specific | [Docs](https://langchain-ai.github.io/langgraph/) · Py/JS: official packages · Go/PHP: — | Open-source libraries; hosted LangSmith services have separate plans. |
| 87 | **[DSPy](https://dspy.ai/)** [86] | Framework for programming and optimizing multi-stage language-model systems using evaluators, modules, and data-driven compilation. | Financial NLP research; AI evaluation; not trading-specific | [Docs](https://dspy.ai/) · Py: [official](https://github.com/stanfordnlp/dspy) · Go/PHP: — | Open source; model API and compute charges are separate. |

---

## 11. Feature engineering & technical analysis

Feature libraries make transformations repeatable; they do not make a feature predictive. Every rolling calculation, normalization, label, or learned representation must respect event time, publication delay, asset availability, and train/test boundaries. Pin formulas and package versions when indicator parity matters across research and production.[87] [89] [91]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 88 | **[TA-Lib](https://ta-lib.org/)** [87] | Long-established C/C++ technical-analysis library with indicators, candlestick recognition, and language wrappers. | Multi-asset technical analysis; Research / automation | [Core API](https://ta-lib.org/function.html) · Py: [community wrapper](https://github.com/TA-Lib/ta-lib-python) · other wrappers listed by project | Open source under BSD terms. |
| 89 | **[pandas-ta-classic](https://github.com/twopirllc/pandas-ta)** [88] | Community-maintained pandas extension providing a broad set of indicators, strategies, and candlestick patterns. | Multi-asset technical analysis; Research | [Docs](https://github.com/twopirllc/pandas-ta#readme) · Py: [community-maintained](https://github.com/twopirllc/pandas-ta) · Go/PHP: — | Open source; validate formula parity and pin versions. |
| 90 | **[Technical Analysis Library in Python](https://github.com/bukosabino/ta)** [89] | Pure-Python indicator library built around pandas series for momentum, trend, volatility, and volume features. | Multi-asset technical analysis; Research | [Docs](https://technical-analysis-library-in-python.readthedocs.io/) · Py: [official](https://github.com/bukosabino/ta) · Go/PHP: — | Open source. |
| 91 | **[tsfresh](https://tsfresh.com/)** [90] | Automated extraction and relevance filtering of large collections of time-series characteristics for ML pipelines. | Time-series ML; feature extraction; Research | [Docs](https://tsfresh.readthedocs.io/) · Py: [official](https://github.com/blue-yonder/tsfresh) · Go/PHP: — | Open source. |
| 92 | **[Featuretools](https://www.featuretools.com/)** [91] | Automated feature-engineering framework for temporal and relational datasets using Deep Feature Synthesis. | Tabular and temporal ML; alternative data; Research | [Docs](https://featuretools.alteryx.com/) · Py: [official](https://github.com/alteryx/featuretools) · Go/PHP: — | Open source; managed compute is not included. |
| 93 | **[mlfinpy](https://mlfinlab.com/)** [92] | Financial ML utilities for sampling, labeling, filters, fractional differentiation, feature importance, and portfolio research. | Financial ML; feature engineering; Research | [Docs](https://mlfinlab.readthedocs.io/) · Py: [official](https://github.com/hudson-and-thames/mlfinlab) · Go/PHP: — | Open source; review method assumptions and project maintenance before production use. |

---

## 12. Financial visualization

Visualization libraries differ from data vendors: most render data that you must source, license, normalize, and stream yourself. Evaluate update performance, time-zone handling, accessibility, annotation needs, export requirements, mobile behavior, and commercial licensing before selecting a charting layer.[93] [94] [96]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 94 | **[TradingView Lightweight Charts](https://www.tradingview.com/lightweight-charts/)** [93] | Compact open-source JavaScript library for responsive, streaming financial charts using custom data. | Web charting; candlesticks; time series; Research / automation | [Docs](https://tradingview.github.io/lightweight-charts/) · JS/TS: official · no market data included | Open source under Apache 2.0. |
| 95 | **[Plotly](https://plotly.com/)** [94] | Interactive graphing ecosystem with candlestick, OHLC, time-series, statistical, and dashboard-friendly charts. | Research visualization; dashboards; financial reporting | [Python docs](https://plotly.com/python/) · Py: [official](https://github.com/plotly/plotly.py) · JS: [official](https://github.com/plotly/plotly.js) | Open-source graphing libraries; commercial hosting and enterprise products are separate. |
| 96 | **[Apache ECharts](https://echarts.apache.org/)** [95] | High-performance JavaScript visualization library with candlestick, line, heatmap, scatter, and large-data rendering options. | Web dashboards; candlesticks; general analytics | [Docs](https://echarts.apache.org/en/option.html) · JS/TS: official · community wrappers exist | Open source under Apache 2.0. |
| 97 | **[Highcharts Stock](https://www.highcharts.com/products/stock/)** [96] | Commercial financial-charting library with data grouping, annotations, navigation, and built-in technical indicators. | Web and mobile financial charts; dashboards | [Docs](https://api.highcharts.com/highstock/) · JS/TS: official package · wrappers for major frameworks | Free for eligible non-commercial use under current terms; commercial licenses are paid. |
| 98 | **[Bokeh](https://bokeh.org/)** [97] | Python visualization library and server for interactive browser-based plots, linked views, streaming, and dashboards. | Research visualization; dashboards; time series | [Docs](https://docs.bokeh.org/) · Py: [official](https://github.com/bokeh/bokeh) · Go/PHP: — | Open source. |
| 99 | **[mplfinance](https://github.com/matplotlib/mplfinance)** [98] | Matplotlib-based Python package for candlestick, OHLC, volume, overlays, panels, and static financial charts. | Research visualization; notebooks; reports | Py: [official repository](https://github.com/matplotlib/mplfinance) · Go/PHP: — | Open source. |

---

## Which service should I choose?

There is no universal "best" service. Start with the narrowest tool that satisfies the actual workflow, then verify licensing, latency, geography, history depth, and operational limits. This matrix is a practical first stop, not a substitute for a proof of concept.

| If you need | Strong starting point | Why / caveat |
|---|---|---|
| Global multi-asset brokerage API | [Interactive Brokers](https://www.interactivebrokers.com/) [1] | Broad market access and mature interfaces; account eligibility, data subscriptions, and API complexity vary. |
| Developer-first U.S. equities trading | [Alpaca](https://alpaca.markets/) [2] | Accessible paper/live workflow and official SDKs; verify current asset and regional coverage. |
| One library across many crypto exchanges | [CCXT](https://github.com/ccxt/ccxt) [9] | Normalized REST/WebSocket interfaces; exchange-specific semantics still leak through. |
| Broad retail-friendly multi-asset API | [Twelve Data](https://twelvedata.com/) [11] | Wide coverage and straightforward docs; confirm entitlements, latency, and call budgets. |
| Exchange-sourced historical market data | [Databento](https://databento.com/) [16] | Standardized schemas and strong systematic-research workflow; venue data costs matter. |
| Macroeconomic indicators and calendars | [Trading Economics](https://tradingeconomics.com/) [21] | Structured macro, forecast, and calendar API; redistribution and plan limits require review. |
| Free public macro time series | FRED via an existing data provider or direct API | Excellent U.S.-centric macro baseline; release timing and revisions must be modeled. |
| Crypto prices and asset metadata | [CoinGecko](https://www.coingecko.com/) [30] | Practical discovery API with broad asset coverage; rate limits and commercial rights depend on plan. |
| Crypto derivatives, funding, and liquidations | [CoinGlass](https://www.coinglass.com/) [32] | Focused derivatives dashboards and API; methodology and venue aggregation should be verified. |
| Deep on-chain metrics | [Glassnode](https://glassnode.com/) [33] | Curated network and market metrics; advanced/API access can be expensive. |
| Custom blockchain SQL research | [Dune](https://dune.com/) [36] | Flexible public queries and dashboards; query freshness, credits, and chain schemas vary. |
| DeFi TVL, fees, yields, and protocol data | [DeFiLlama](https://defillama.com/) [41] | Broad open DeFi coverage; validate definitions before combining datasets. |
| Entity and wallet intelligence | [Nansen](https://nansen.ai/) [34] or [Arkham](https://arkhamintelligence.com/) [42] | Labeled wallet/entity workflows; labels are analytical inputs, not ground truth. |
| Technical alerts without building a platform | [TrendSpider](https://trendspider.com/) [51] or [TradingView](https://www.tradingview.com/) [46] | Mature chart-driven alerts; confirm webhook availability and repainting behavior. |
| News events delivered through an API | [Benzinga APIs](https://www.benzinga.com/apis/) [54] or [CryptoPanic](https://cryptopanic.com/) [53] | Structured event feeds; commercial redistribution terms differ significantly. |
| Production-grade backtesting + live trading | [NautilusTrader](https://nautilustrader.io/) [66] | Deterministic simulation and broker connectors; learning curve and infrastructure costs apply. |
| Rapid strategy research | [vectorbt](https://vectorbt.dev/) [67] | Vectorized exploration of many configurations; not a live-trading framework. |
| Crypto bot with backtesting | [Freqtrade](https://www.freqtrade.io/) [68] | Active community, dry-run support, and hyperopt; crypto-only. |
| Performance tear sheets | [QuantStats](https://github.com/ranaroussi/quantstats) [74] | Return metrics, drawdowns, and HTML reports; pure analytics, not execution. |
| Portfolio optimization | [Riskfolio-Lib](https://riskfolio-lib.readthedocs.io/) [75] or [skfolio](https://skfolio.org/) [76] | Risk parity, factor models, CVaR, and ML-compatible workflows. |
| Financial AI / ML research | [Microsoft Qlib](https://github.com/microsoft/qlib) [80] | End-to-end platform with data, models, and backtests; treat as research infrastructure. |
| Financial NLP / LLM | [FinGPT](https://fingpt.io/) [82] | Sentiment, forecasting, and retrieval models; verify benchmarks against your use case. |
| Technical indicators in Python | [TA-Lib](https://ta-lib.org/) [87] or [pandas-ta-classic](https://github.com/twopirllc/pandas-ta) [88] | Established libraries; pin versions when indicator parity matters across environments. |
| Time-series feature extraction | [tsfresh](https://tsfresh.com/) [90] | Automated extraction and relevance filtering; computation can be intensive on long series. |
| Financial charts on the web | [TradingView Lightweight Charts](https://www.tradingview.com/lightweight-charts/) [93] | Compact, streaming, free; you bring the data and the data license. |
| Research plots and dashboards | [Plotly](https://plotly.com/) [94] or [Bokeh](https://bokeh.org/) [97] | Interactive Python-native plotting; no market data included. |

---

## Reference links

[1] Interactive Brokers — [Official site](https://www.interactivebrokers.com/) · [API docs](https://www.interactivebrokers.com/campus/ibkr-api-page/ibkr-api-home/) · [Pricing](https://www.interactivebrokers.com/en/pricing/commissions-home.php)  
[2] Alpaca — [Official site](https://alpaca.markets/) · [Docs](https://docs.alpaca.markets/) · [Pricing](https://alpaca.markets/pricing)  
[3] QuantConnect — [Official site](https://www.quantconnect.com/) · [Docs](https://www.quantconnect.com/docs/v2/) · [LEAN](https://github.com/QuantConnect/Lean)  
[4] MetaTrader 5 — [Official site](https://www.metatrader5.com/) · [Python docs](https://www.mql5.com/en/docs/python_metatrader5)  
[5] OANDA — [Official site](https://www.oanda.com/) · [v20 API docs](https://developer.oanda.com/rest-live-v20/introduction/)  
[6] cTrader — [Official site](https://ctrader.com/) · [Open API docs](https://help.ctrader.com/open-api/)  
[7] tastytrade — [Official site](https://tastytrade.com/) · [Developer docs](https://developer.tastytrade.com/)  
[8] Tradier — [Official site](https://tradier.com/) · [API docs](https://docs.tradier.com/)  
[9] CCXT — [GitHub](https://github.com/ccxt/ccxt) · [Docs](https://docs.ccxt.com/) · [Pro pricing](https://ccxt.pro/)  
[10] Finnhub — [Official site](https://finnhub.io/) · [API docs](https://finnhub.io/docs/api) · [Pricing](https://finnhub.io/pricing)  
[11] Twelve Data — [Official site](https://twelvedata.com/) · [Docs](https://twelvedata.com/docs) · [Pricing](https://twelvedata.com/pricing)  
[12] Massive (formerly Polygon.io) — [Official site](https://massive.com/) · [Docs](https://massive.com/docs) · [Pricing](https://massive.com/pricing)  
[13] Alpha Vantage — [Official site](https://www.alphavantage.co/) · [Docs](https://www.alphavantage.co/documentation/) · [Pricing](https://www.alphavantage.co/premium/)  
[14] Financial Modeling Prep — [Official site](https://site.financialmodelingprep.com/) · [Docs](https://site.financialmodelingprep.com/developer/docs) · [Pricing](https://site.financialmodelingprep.com/pricing)  
[15] EODHD — [Official site](https://eodhd.com/) · [API docs](https://eodhd.com/financial-apis/) · [Pricing](https://eodhd.com/pricing)  
[16] Databento — [Official site](https://databento.com/) · [Docs](https://databento.com/docs) · [Pricing](https://databento.com/pricing)  
[17] Tiingo — [Official site](https://www.tiingo.com/) · [Docs](https://www.tiingo.com/documentation/) · [Pricing](https://www.tiingo.com/about/pricing)  
[18] Intrinio — [Official site](https://intrinio.com/) · [API docs](https://docs.intrinio.com/documentation/api_v2/getting_started) · [Pricing](https://intrinio.com/pricing)  
[19] Barchart — [Official site](https://www.barchart.com/) · [OnDemand API](https://www.barchart.com/ondemand/api) · [Pricing](https://www.barchart.com/solutions/data)  
[20] Nasdaq Data Link — [Official site](https://data.nasdaq.com/) · [Docs](https://docs.data.nasdaq.com/)  
[21] Trading Economics — [Official site](https://tradingeconomics.com/) · [API docs](https://docs.tradingeconomics.com/) · [Pricing](https://tradingeconomics.com/api)  
[22] Marketstack — [Official site](https://marketstack.com/) · [Docs](https://docs.apilayer.com/marketstack/docs/api-documentation) · [Pricing](https://marketstack.com/product)  
[23] Unusual Whales — [Official site](https://unusualwhales.com/) · [API docs](https://api.unusualwhales.com/docs) · [Pricing](https://unusualwhales.com/pricing)  
[24] Binance API — [Developer portal](https://developers.binance.com/) · [Spot docs](https://developers.binance.com/docs/binance-spot-api-docs/CHANGELOG)  
[25] Coinbase Advanced Trade API — [Developer platform](https://www.coinbase.com/developer-platform/products/advanced-trade-api) · [Docs](https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/overview)  
[26] Kraken API — [Official site](https://www.kraken.com/) · [API docs](https://docs.kraken.com/api/)  
[27] Bybit API — [Official site](https://www.bybit.com/) · [V5 docs](https://bybit-exchange.github.io/docs/v5/intro)  
[28] OKX API — [Official site](https://www.okx.com/) · [API portal](https://www.okx.com/okx-api)  
[29] Hyperliquid — [Official site](https://hyperliquid.xyz/) · [API docs](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api)  
[30] CoinGecko — [Official site](https://www.coingecko.com/) · [API docs](https://docs.coingecko.com/) · [Pricing](https://www.coingecko.com/en/api/pricing)  
[31] CoinMarketCap — [Official site](https://coinmarketcap.com/) · [API docs](https://coinmarketcap.com/api/documentation/) · [Pricing](https://coinmarketcap.com/api/pricing/)  
[32] CoinGlass — [Official site](https://www.coinglass.com/) · [API docs](https://docs.coinglass.com/reference/getting-started-with-your-api) · [Pricing](https://www.coinglass.com/pricing)  
[33] Glassnode — [Official site](https://glassnode.com/) · [API docs](https://docs.glassnode.com/basic-api/api) · [Pricing](https://glassnode.com/pricing)  
[34] Nansen — [Official site](https://nansen.ai/) · [API docs](https://docs.nansen.ai/) · [Pricing](https://www.nansen.ai/pricing)  
[35] CryptoQuant — [Official site](https://cryptoquant.com/) · [API docs](https://docs.cryptoquant.com/) · [Pricing](https://cryptoquant.com/pricing)  
[36] Dune — [Official site](https://dune.com/) · [API docs](https://docs.dune.com/api-reference/overview/introduction) · [Pricing](https://dune.com/pricing)  
[37] Coin Metrics — [Official site](https://www.talos.com/our-solutions/data/overview) · [API docs](https://docs.coinmetrics.io/api/v4/)  
[38] Kaiko — [Official site](https://www.kaiko.com/) · [API docs](https://docs.kaiko.com/)  
[39] Messari — [Official site](https://messari.io/) · [API docs](https://docs.messari.io/introduction)  
[40] Santiment — [Official site](https://santiment.net/) · [API docs](https://academy.santiment.net/sanapi/) · [Pricing](https://santiment.net/pricing/)  
[41] DeFiLlama — [Official site](https://defillama.com/) · [API docs](https://api-docs.defillama.com/)  
[42] Arkham — [Official site](https://arkhamintelligence.com/) · [API docs](https://arkm.com/api/docs)  
[43] Whale Alert — [Official site](https://whale-alert.io/) · [API docs](https://developer.whale-alert.io/api-account/documentation) · [Pricing](https://whale-alert.io/pricing)  
[44] LunarCrush — [Official site](https://lunarcrush.com/) · [Developer API](https://lunarcrush.com/en/developers/api) · [Pricing](https://lunarcrush.com/pricing)  
[45] CoinAPI — [Official site](https://www.coinapi.io/) · [API docs](https://docs.coinapi.io/) · [Pricing](https://www.coinapi.io/pricing)  
[46] TradingView — [Official site](https://www.tradingview.com/) · [Pine Script docs](https://www.tradingview.com/pine-script-docs/) · [Pricing](https://www.tradingview.com/pricing/)  
[47] Koyfin — [Official site](https://www.koyfin.com/) · [Pricing](https://www.koyfin.com/pricing/)  
[48] CoinQuant — [Official site](https://www.coinquant.ai/) · [Docs](https://www.coinquant.ai/documentation/public-api-skills-pack)  
[49] TradingCursor — [Official site](https://www.tradingcursor.com/) · [Pricing](https://www.tradingcursor.com/pricing)  
[50] LONA™ — [Official site](https://www.lona.agency/en) · [Pricing](https://www.lona.agency/en/pricing)  
[51] TrendSpider — [Official site](https://trendspider.com/) · [Webhook docs](https://help.trendspider.com/articles/webhooks) · [Pricing](https://trendspider.com/pricing/)  
[52] LuxAlgo — [Official site](https://www.luxalgo.com/) · [Docs](https://docs.luxalgo.com/docs/getting-started/introduction)  
[53] CryptoPanic — [Official site](https://cryptopanic.com/) · [API docs](https://cryptopanic.com/developers/api/)  
[54] Benzinga APIs — [Official site](https://www.benzinga.com/apis/) · [Docs](https://docs.benzinga.io/)  
[55] FinancialJuice — [Official site](https://www.financialjuice.com/)  
[56] GDELT — [Official site](https://www.gdeltproject.org/) · [DOC API](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) · [Data access](https://www.gdeltproject.org/data.html)  
[57] SignalStack — [Official site](https://signalstack.com/) · [Docs](https://help.signalstack.com/)  
[58] ClickHouse — [Official site](https://clickhouse.com/) · [Docs](https://clickhouse.com/docs)  
[59] QuestDB — [Official site](https://questdb.com/) · [Docs](https://questdb.com/docs/)  
[60] TimescaleDB — [Official site](https://www.timescale.com/) · [Docs](https://docs.timescale.com/)  
[61] Redis — [Official site](https://redis.io/) · [Docs](https://redis.io/docs/latest/)  
[62] Apache Kafka — [Official site](https://kafka.apache.org/) · [Docs](https://kafka.apache.org/documentation/)  
[63] NATS — [Official site](https://nats.io/) · [Docs](https://docs.nats.io/)  
[64] Prometheus — [Official site](https://prometheus.io/) · [Docs](https://prometheus.io/docs/introduction/overview/)  
[65] Grafana — [Official site](https://grafana.com/) · [Docs](https://grafana.com/docs/grafana/latest/)  
[66] NautilusTrader — [Official site](https://nautilustrader.io/) · [Docs](https://nautilustrader.io/docs/latest/)  
[67] vectorbt — [Official site](https://vectorbt.dev/) · [Docs](https://vectorbt.dev/)  
[68] Freqtrade — [Official site](https://www.freqtrade.io/) · [Docs](https://www.freqtrade.io/en/stable/)  
[69] Backtrader — [Official site](https://www.backtrader.com/) · [Docs](https://www.backtrader.com/docu/)  
[70] Zipline Reloaded — [Official site](https://zipline.ml4trading.io/) · [Docs](https://zipline.ml4trading.io/)  
[71] Jesse — [Official site](https://jesse.trade/) · [Docs](https://docs.jesse.trade/)  
[72] Hummingbot — [Official site](https://hummingbot.org/) · [Docs](https://hummingbot.org/docs/)  
[73] backtesting.py — [Official site](https://kernc.github.io/backtesting.py/) · [Docs](https://kernc.github.io/backtesting.py/)  
[74] QuantStats — [GitHub](https://github.com/ranaroussi/quantstats)  
[75] Riskfolio-Lib — [Official site](https://riskfolio-lib.readthedocs.io/) · [Docs](https://riskfolio-lib.readthedocs.io/en/latest/)  
[76] skfolio — [Official site](https://skfolio.org/) · [Docs](https://skfolio.org/user_guide/index.html)  
[77] PyPortfolioOpt — [Official site](https://pyportfolioopt.readthedocs.io/) · [Docs](https://pyportfolioopt.readthedocs.io/en/latest/)  
[78] empyrical-reloaded — [GitHub](https://github.com/stefan-jansen/empyrical-reloaded)  
[79] pyfolio-reloaded — [GitHub](https://github.com/stefan-jansen/pyfolio-reloaded)  
[80] Microsoft Qlib — [GitHub](https://github.com/microsoft/qlib) · [Docs](https://qlib.readthedocs.io/)  
[81] FinRL-X — [GitHub](https://github.com/AI4Finance-Foundation/FinRL-Trading)  
[82] FinGPT — [Official site](https://fingpt.io/) · [Docs](https://fingpt.io/docs) · [Models](https://huggingface.co/FinGPT)  
[83] FinRL — [GitHub](https://github.com/AI4Finance-Foundation/FinRL) · [Docs](https://finrl.readthedocs.io/)  
[84] TensorTrade — [Official site](https://www.tensortrade.org/) · [Docs](https://www.tensortrade.org/)  
[85] LangGraph — [Official site](https://langchain-ai.github.io/langgraph/) · [Docs](https://langchain-ai.github.io/langgraph/)  
[86] DSPy — [Official site](https://dspy.ai/) · [Docs](https://dspy.ai/)  
[87] TA-Lib — [Official site](https://ta-lib.org/) · [Core API](https://ta-lib.org/function.html)  
[88] pandas-ta-classic — [GitHub](https://github.com/twopirllc/pandas-ta)  
[89] Technical Analysis Library in Python — [GitHub](https://github.com/bukosabino/ta) · [Docs](https://technical-analysis-library-in-python.readthedocs.io/)  
[90] tsfresh — [Official site](https://tsfresh.com/) · [Docs](https://tsfresh.readthedocs.io/)  
[91] Featuretools — [Official site](https://www.featuretools.com/) · [Docs](https://featuretools.alteryx.com/)  
[92] mlfinpy — [Official site](https://mlfinlab.com/) · [Docs](https://mlfinlab.readthedocs.io/)  
[93] TradingView Lightweight Charts — [Official site](https://www.tradingview.com/lightweight-charts/) · [Docs](https://tradingview.github.io/lightweight-charts/)  
[94] Plotly — [Official site](https://plotly.com/) · [Python docs](https://plotly.com/python/)  
[95] Apache ECharts — [Official site](https://echarts.apache.org/) · [Docs](https://echarts.apache.org/en/option.html)  
[96] Highcharts Stock — [Official site](https://www.highcharts.com/products/stock/) · [Docs](https://api.highcharts.com/highstock/)  
[97] Bokeh — [Official site](https://bokeh.org/) · [Docs](https://docs.bokeh.org/)  
[98] mplfinance — [GitHub](https://github.com/matplotlib/mplfinance)  
[99] DepthFeed — [Official site](https://depthfeed.com/) · [API docs](https://depthfeed.com/docs) · [MCP](https://github.com/vcorp-dev/depthfeed-mcp) · [Pricing](https://depthfeed.com/pricing)

---

## License

This curated list is provided as-is for informational and educational purposes. It does not constitute financial, investment, or legal advice. Always verify current terms, pricing, and regulatory requirements directly with service providers before making decisions.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on proposing new services, updating pricing, and following our editorial criteria.

---

<p align="center">
  <sub>Curated with ❤️ for the trading and quant community. Last updated: 27 July 2026.</sub>
</p>
