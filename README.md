# Awesome Trading Services, Market Data APIs & Crypto Analytics

![Trading awesome](https://i.postimg.cc/SstfKwXF/trading-awesome-github.jpg)

> A curated directory of **90+ trading services and open-source tools** for algorithmic traders, quantitative researchers, developers, and active investors. It covers broker and exchange APIs, stock and forex data, cryptocurrency market data, on-chain analytics, signal intelligence, backtesting, portfolio analytics, AI research, feature engineering, infrastructure, and financial visualization.

Reliable trading infrastructure is a prerequisite for serious research and automation. This SEO-friendly Awesome List makes it easier to compare **market-data APIs**, **brokerage APIs**, **crypto exchange APIs**, **forex platforms**, and **on-chain analytics tools** without treating fundamentally different products as interchangeable. It is intended as a practical discovery resource—not as an endorsement or a trading recommendation.

The list is ranked by **editorial practical significance** as of **27 July 2026**. The ranking weighs breadth and reliability of data or execution capability, API maturity, developer ecosystem, workflow relevance, distinctive specialization, and public accessibility. The rank is deliberately not a claim about market share, investment returns, or the quality of any individual strategy.

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

## How to use this list

Every entry links to the provider’s official site. The **API & packages** column always points to public documentation when a public API is available. `Py`, `Go`, and `PHP` link to a GitHub package only when a relevant repository could be identified. Packages marked **community** are not represented as first-party software; validate maintenance, licensing, security, and compatibility before production use.

| Coverage label | Meaning |
| --- | --- |
| **Crypto — spot / on-chain / DeFi** | Digital-asset spot markets, blockchain data, stablecoins, decentralized finance, or NFT-related data where applicable |
| **Crypto — derivatives** | Perpetual futures, futures, options, funding, liquidations, open interest, or related market structure |
| **Traditional markets** | Equities, ETFs, options, futures, bonds, indices, fundamentals, filings, or financial news |
| **Forex / FX** | Spot FX, exchange rates, CFDs where legally available, or FX market data |
| **Brokerage / execution** | Programmatic orders, account access, paper trading, portfolio operations, or direct market access |
| **Research / automation** | Backtesting, charting, analytics, alerts, no-code workflows, or developer infrastructure |

> **Pricing convention.** Prices are public entry prices or plan descriptions reported by providers at the reference date. They may change by region, exchange, data-entitlement, billing interval, user type, and promotional terms. “Custom” or “contact sales” means no reliable public price was found; it does not mean the product is free.

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
| 30 | **[BingX](https://bingx.com)** | BingX — crypto exchange offering spot, futures, and copy trading for global users. | Crypto — spot / DeFi; Crypto — derivatives; Brokerage / execution | [API docs](https://bingx-api.github.io/docs-v3/#/en/info) · Py: [bingx-python](https://github.com/tigusigalpa/bingx-python) · Go: [bingx-go](https://github.com/tigusigalpa/bingx-go) · PHP: [bingx-php](https://github.com/tigusigalpa/bingx-php) | Public base fees include **0.015% maker / 0.045% taker** for perpetuals; discounts and conditions apply. |

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

## 5. Charting, research & no-code decision support

These services are valuable to discretionary and hybrid workflows even when they do not provide a general public trading API. They prioritize charting, dashboards, research, portfolio views, AI-assisted analysis, or no-code strategy experimentation. API access should never be inferred from a web dashboard, embedded widget, Pine Script environment, or broker integration.[46] [47]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 47 | **[TradingView](https://www.tradingview.com/)** [46] | Mainstream charting, screening, market-data visualization, alerting, and Pine Script platform across many asset classes. | Traditional markets; Forex / FX; crypto; Research / automation | No general public data/indicator API for personal use · [Pine Script docs](https://www.tradingview.com/pine-script-docs/) · Py: — · Go: — · PHP: — | Free tier; public paid plans range from **$12.95/month to $199.95/month billed annually**. |
| 48 | **[Koyfin](https://www.koyfin.com/)** [47] | Financial research workspace for market dashboards, portfolio analysis, company fundamentals, and reporting. | Traditional markets; fundamentals; Research | No public API identified · Py: — · Go: — · PHP: — | Free, Plus **$39/month**, Premium **$79/month**, with higher advisor tiers. |
| 49 | **[CoinQuant](https://www.coinquant.ai/)** [48] | No-code, AI-assisted strategy builder and backtesting platform for market research and systematic experimentation. | Crypto; traditional markets; Research / automation | [Public API skills pack](https://www.coinquant.ai/documentation/public-api-skills-pack) · Py: — · Go: — · PHP: — | Free credits; public paid plans listed from **$12.99/week**. |
| 50 | **[TradingCursor](https://www.tradingcursor.com/)** [49] | AI-assisted multi-signal research product for stocks, ETFs, forex, and crypto decision support. | Traditional markets; Forex / FX; crypto; Research | No public API identified · Py: — · Go: — · PHP: — | Free daily analysis; Pro is publicly listed at **$9.90/month**. |
| 51 | **[LONA™](https://www.lona.agency/en)** [50] | No-code AI trading assistant for creating, backtesting, and optimizing trading ideas. | Traditional markets; Forex / FX; crypto; Research / automation | No public API identified · Py: — · Go: — · PHP: — | Free tier; Pro **$49/month**, Premium **$99/month**, Quant **$249/month**. |

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

## 10. AI & machine-learning frameworks

AI frameworks can accelerate forecasting, representation learning, language analysis, research automation, and experimentation, but they do not solve data leakage, non-stationarity, execution costs, or weak validation. Financial LLM and reinforcement-learning projects in particular should be treated as research infrastructure until they pass realistic walk-forward, paper-trading, operational, and risk review.[80] [81] [83]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 81 | **[Microsoft Qlib](https://github.com/microsoft/qlib)** [80] | AI-oriented quantitative-investment platform with data, workflow, model, backtest, portfolio, and experiment-management components. | Traditional markets; quantitative ML; Research / automation | [Docs](https://qlib.readthedocs.io/) · Py: [official](https://github.com/microsoft/qlib) · Go/PHP: — | Open source; data and compute are separate. |
| 82 | **[FinRL-X](https://github.com/AI4Finance-Foundation/FinRL-Trading)** [81] | AI-native modular trading infrastructure positioned as the production-oriented successor to the original FinRL research framework. | Multi-asset; reinforcement learning; Research / automation | Py: [official](https://github.com/AI4Finance-Foundation/FinRL-Trading) · research paper and examples linked from repository · Go/PHP: — | Open source; venue, data, model, and compute costs are separate. |
| 83 | **[FinGPT](https://fingpt.io/)** [82] | Open-source financial LLM project with models and workflows for sentiment, forecasting, retrieval, fine-tuning, and benchmarks. | Financial text; news; sentiment; Research / automation | [Docs](https://fingpt.io/docs) · Py: [official](https://github.com/AI4Finance-Foundation/FinGPT) · models: [Hugging Face](https://huggingface.co/FinGPT) | Open source; hosted APIs, model compute, and enterprise services may be separately priced. |
| 84 | **[FinRL](https://github.com/AI4Finance-Foundation/FinRL)** [83] | Educational and research framework for financial reinforcement-learning environments, agents, datasets, and backtests. | Traditional markets; crypto; reinforcement learning; Research | [Docs](https://finrl.readthedocs.io/) · Py: [official](https://github.com/AI4Finance-Foundation/FinRL) · Go/PHP: — | Open source; the project directs production-oriented users toward FinRL-X. |
| 85 | **[TensorTrade](https://www.tensortrade.org/)** [84] | Modular Python framework for building trading environments, reward/action schemes, agents, portfolios, and RL experiments. | Multi-asset; reinforcement learning; Research | [Docs](https://www.tensortrade.org/en/latest/) · Py: [official](https://github.com/tensortrade-org/tensortrade) · Go/PHP: — | Open source; verify current maintenance and dependency compatibility. |
| 86 | **[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)** [85] | General-purpose framework for durable, stateful agent workflows that can orchestrate research tools, approvals, and human review. | AI orchestration; Research / automation; not trading-specific | [Docs](https://docs.langchain.com/oss/python/langgraph/overview) · Py/JS: official packages · Go/PHP: — | Open-source libraries; hosted LangSmith services have separate plans. |
| 87 | **[DSPy](https://dspy.ai/)** [86] | Framework for programming and optimizing multi-stage language-model systems using evaluators, modules, and data-driven compilation. | Financial NLP research; AI evaluation; not trading-specific | [Docs](https://dspy.ai/) · Py: [official](https://github.com/stanfordnlp/dspy) · Go/PHP: — | Open source; model API and compute charges are separate. |

## 11. Feature engineering & technical analysis

Feature libraries make transformations repeatable; they do not make a feature predictive. Every rolling calculation, normalization, label, or learned representation must respect event time, publication delay, asset availability, and train/test boundaries. Pin formulas and package versions when indicator parity matters across research and production.[87] [89] [91]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 88 | **[TA-Lib](https://ta-lib.org/)** [87] | Long-established C/C++ technical-analysis library with indicators, candlestick recognition, and language wrappers. | Multi-asset technical analysis; Research / automation | [Core API](https://ta-lib.org/api/) · Py: [community wrapper](https://github.com/TA-Lib/ta-lib-python) · other wrappers listed by project | Open source under BSD terms. |
| 89 | **[pandas-ta-classic](https://xgboosted.github.io/pandas-ta-classic/)** [88] | Community-maintained pandas extension providing a broad set of indicators, strategies, and candlestick patterns. | Multi-asset technical analysis; Research | [Docs](https://xgboosted.github.io/pandas-ta-classic/) · Py: [community-maintained](https://github.com/xgboosted/pandas-ta-classic) · Go/PHP: — | Open source; validate formula parity and pin versions. |
| 90 | **[Technical Analysis Library in Python](https://technical-analysis-library-in-python.readthedocs.io/)** [89] | Pure-Python indicator library built around pandas series for momentum, trend, volatility, and volume features. | Multi-asset technical analysis; Research | [Docs](https://technical-analysis-library-in-python.readthedocs.io/) · Py: [official](https://github.com/bukosabino/ta) · Go/PHP: — | Open source. |
| 91 | **[tsfresh](https://tsfresh.readthedocs.io/)** [90] | Automated extraction and relevance filtering of large collections of time-series characteristics for ML pipelines. | Time-series ML; feature extraction; Research | [Docs](https://tsfresh.readthedocs.io/en/stable/) · Py: [official](https://github.com/blue-yonder/tsfresh) · Go/PHP: — | Open source. |
| 92 | **[Featuretools](https://www.featuretools.com/)** [91] | Automated feature-engineering framework for temporal and relational datasets using Deep Feature Synthesis. | Tabular and temporal ML; alternative data; Research | [Docs](https://docs.featuretools.com/en/stable/) · Py: [official](https://github.com/alteryx/featuretools) · Go/PHP: — | Open source; managed compute is not included. |
| 93 | **[mlfinpy](https://mlfinpy.readthedocs.io/)** [92] | Financial ML utilities for sampling, labeling, filters, fractional differentiation, feature importance, and portfolio research. | Financial ML; feature engineering; Research | [Docs](https://mlfinpy.readthedocs.io/) · Py: [official](https://github.com/baobach/mlfinpy) · Go/PHP: — | Open source; review method assumptions and project maintenance before production use. |

## 12. Financial visualization

Visualization libraries differ from data vendors: most render data that you must source, license, normalize, and stream yourself. Evaluate update performance, time-zone handling, accessibility, annotation needs, export requirements, mobile behavior, and commercial licensing before selecting a charting layer.[93] [94] [96]

| Rank | Service | What it does | Markets / scope | API & packages | Public pricing / tariff |
| ---: | --- | --- | --- | --- | --- |
| 94 | **[TradingView Lightweight Charts](https://www.tradingview.com/lightweight-charts/)** [93] | Compact open-source JavaScript library for responsive, streaming financial charts using custom data. | Web charting; candlesticks; time series; Research / automation | [Docs](https://tradingview.github.io/lightweight-charts/) · JS/TS: [official](https://github.com/tradingview/lightweight-charts) · no market data included | Open source under Apache 2.0. |
| 95 | **[Plotly](https://plotly.com/)** [94] | Interactive graphing ecosystem with candlestick, OHLC, time-series, statistical, and dashboard-friendly charts. | Research visualization; dashboards; financial reporting | [Python docs](https://plotly.com/python/) · Py: [official](https://github.com/plotly/plotly.py) · JS: [official](https://github.com/plotly/plotly.js) | Open-source graphing libraries; commercial hosting and enterprise products are separate. |
| 96 | **[Apache ECharts](https://echarts.apache.org/)** [95] | High-performance JavaScript visualization library with candlestick, line, heatmap, scatter, and large-data rendering options. | Web dashboards; candlesticks; general analytics | [Docs](https://echarts.apache.org/en/index.html) · JS/TS: [official](https://github.com/apache/echarts) · community wrappers exist | Open source under Apache 2.0. |
| 97 | **[Highcharts Stock](https://www.highcharts.com/products/stock/)** [96] | Commercial financial-charting library with data grouping, annotations, navigation, and built-in technical indicators. | Web and mobile financial charts; dashboards | [Docs](https://www.highcharts.com/docs/stock/getting-started-stock) · JS/TS: official package · wrappers for major frameworks | Free for eligible non-commercial use under current terms; commercial licenses are paid. |
| 98 | **[Bokeh](https://bokeh.org/)** [97] | Python visualization library and server for interactive browser-based plots, linked views, streaming, and dashboards. | Research visualization; dashboards; time series | [Docs](https://docs.bokeh.org/en/latest/) · Py: [official](https://github.com/bokeh/bokeh) · Go/PHP: — | Open source. |
| 99 | **[mplfinance](https://github.com/matplotlib/mplfinance)** [98] | Matplotlib-based Python package for candlestick, OHLC, volume, overlays, panels, and static financial charts. | Research visualization; notebooks; reports | Py: [official repository](https://github.com/matplotlib/mplfinance) · Go/PHP: — | Open source. |

## Which service should I choose?

There is no universal “best” service. Start with the narrowest tool that satisfies the actual workflow, then verify licensing, latency, geography, history depth, and operational limits. This matrix is a practical first stop, not a substitute for a proof of concept.

| If you need | Strong starting point | Why / caveat |
| --- | --- | --- |
| Global multi-asset brokerage API | [Interactive Brokers](https://www.interactivebrokers.com/) | Broad market access and mature interfaces; account eligibility, data subscriptions, and API complexity vary. |
| Developer-first U.S. equities trading | [Alpaca](https://alpaca.markets/) | Accessible paper/live workflow and official SDKs; verify current asset and regional coverage. |
| One library across many crypto exchanges | [CCXT](https://github.com/ccxt/ccxt) | Normalized REST/WebSocket interfaces; exchange-specific semantics still leak through. |
| Broad retail-friendly multi-asset API | [Twelve Data](https://twelvedata.com/) | Wide coverage and straightforward docs; confirm entitlements, latency, and call budgets. |
| Exchange-sourced historical market data | [Databento](https://databento.com/) | Standardized schemas and strong systematic-research workflow; venue data costs matter. |
| Macroeconomic indicators and calendars | [Trading Economics](https://tradingeconomics.com/) | Structured macro, forecast, and calendar API; redistribution and plan limits require review. |
| Free public macro time series | [FRED](https://fred.stlouisfed.org/) via an existing data provider or direct API | Excellent U.S.-centric macro baseline; release timing and revisions must be modeled. |
| Crypto prices and asset metadata | [CoinGecko](https://www.coingecko.com/) | Practical discovery API with broad asset coverage; rate limits and commercial rights depend on plan. |
| Crypto derivatives, funding, and liquidations | [CoinGlass](https://www.coinglass.com/) | Focused derivatives dashboards and API; methodology and venue aggregation should be verified. |
| Deep on-chain metrics | [Glassnode](https://glassnode.com/) | Curated network and market metrics; advanced/API access can be expensive. |
| Custom blockchain SQL research | [Dune](https://dune.com/) | Flexible public queries and dashboards; query freshness, credits, and chain schemas vary. |
| DeFi TVL, fees, yields, and protocol data | [DeFiLlama](https://defillama.com/) | Broad open DeFi coverage; validate definitions before combining datasets. |
| Entity and wallet intelligence | [Nansen](https://nansen.ai/) or [Arkham](https://arkhamintelligence.com/) | Labeled wallet/entity workflows; labels are analytical inputs, not ground truth. |
| Technical alerts without building a platform | [TrendSpider](https://trendspider.com/) or [TradingView](https://www.tradingview.com/) | Mature chart-driven alerts; confirm webhook availability and repainting behavior. |
| News events delivered through an API | [Benzinga APIs](https://www.benzinga.com/apis/) or [CryptoPanic](https://cryptopanic.com/) | Choose by asset class; licensing and redistribution constraints are central. |
| Fast exploratory backtesting in Python | [vectorbt](https://vectorbt.dev/) | Excellent for parameter sweeps; vectorized assumptions may differ from event-driven execution. |
| Research-to-live event-driven engine | [NautilusTrader](https://nautilustrader.io/) | Shared simulation/live architecture; integration and operational complexity are higher. |
| Crypto bot with backtest and dry-run | [Freqtrade](https://www.freqtrade.io/) | Strong end-to-end open-source workflow; strategy quality and exchange risks remain yours. |
| Portfolio optimization and constraints | [Riskfolio-Lib](https://riskfolio-lib.readthedocs.io/) or [skfolio](https://skfolio.org/) | Rich allocation and validation tools; estimation error can dominate optimizer output. |
| Performance tearsheets | [QuantStats](https://github.com/ranaroussi/quantstats) | Fast reporting from return series; audit metric definitions before formal reporting. |
| High-volume analytical event storage | [ClickHouse](https://clickhouse.com/) | Strong columnar analytics; not a substitute for a transactional order-state database. |
| Time-series SQL with PostgreSQL compatibility | [TimescaleDB](https://www.timescale.com/) | Familiar PostgreSQL ecosystem; benchmark ingestion, compression, and query patterns. |
| Lightweight durable service messaging | [NATS](https://nats.io/) | Simple low-latency messaging and JetStream; choose semantics and retention deliberately. |
| Embeddable open-source financial charts | [TradingView Lightweight Charts](https://www.tradingview.com/lightweight-charts/) | Compact and purpose-built; you supply and license all market data. |
| Financial ML research platform | [Microsoft Qlib](https://github.com/microsoft/qlib) | Broad research workflow; production data, controls, and execution remain separate concerns. |

## Selection principles

This directory focuses on services and open-source tools with a material role in data acquisition, research, risk monitoring, trade execution, trading automation, or the infrastructure that supports those workflows. I included both retail-accessible tools and enterprise-grade data vendors because production systems often combine them: for example, an execution broker, a market-data provider, an on-chain source, a research engine, and an operational data stack.

A service is not ranked highly merely because it is expensive, popular, or has a large marketing footprint. The highest positions favor robust public documentation, broad and usable coverage, credible developer tooling, and direct relevance to a real trading workflow. A specialized product may appear lower in the overall ranking yet still be the most appropriate choice for a particular task, such as DeFi TVL research, liquidation monitoring, options flow, or macroeconomic calendars.

## Practical integration checklist

Before connecting any service to a live workflow, verify the following items directly with the provider. The list is intentionally operational rather than promotional.

| Check | Why it matters |
| --- | --- |
| **License and redistribution rights** | A market-data API may permit personal use but prohibit display, resale, caching, or redistribution. |
| **Latency and adjustment basis** | Real-time, delayed, end-of-day, split-adjusted, and unadjusted prices answer different questions. |
| **Event time and revision history** | News, macro releases, fundamentals, and on-chain labels can arrive late or be revised; a backtest must use only what was knowable at the time. |
| **Survivorship and universe construction** | A present-day symbol list can silently remove delisted assets and overstate historical strategy performance. |
| **Regional and account eligibility** | Broker, exchange, leverage, derivative, and API capabilities can differ materially by residence and legal entity. |
| **Rate limits and retry behavior** | Stable automation requires documented throttling, idempotency handling, retries, and monitoring. |
| **Ordering and duplicate delivery** | Webhooks and event streams may be delayed, repeated, or received out of order; consumers need stable event IDs and reconciliation. |
| **SDK maintenance and security** | Treat community libraries as code to audit; prefer a maintained official SDK or direct signed HTTP integration for critical workflows. |
| **Testnet or paper trading** | Validate authentication, order semantics, partial fills, and failure modes before using production capital. |

## Disclaimer

This repository is an informational research directory. It is not personalized financial, investment, legal, tax, or trading advice; it does not endorse a provider, predict performance, or guarantee data accuracy. Trading and digital-asset activities can result in substantial losses. Always review official documentation, terms, fees, market-data licenses, and local eligibility requirements before using a service.

## Reference links

All citations point to provider-controlled documentation, product pages, official GitHub organizations, or public pricing pages. Reference links were checked on **27 July 2026**.

[1]: https://www.interactivebrokers.com/campus/ibkr-api-page/ibkr-api-home/ "Interactive Brokers API home"
[2]: https://docs.alpaca.markets/ "Alpaca API documentation"
[3]: https://www.quantconnect.com/docs/v2/ "QuantConnect documentation"
[4]: https://www.mql5.com/en/docs/python_metatrader5 "MetaTrader 5 Python integration documentation"
[5]: https://developer.oanda.com/rest-live-v20/introduction/ "OANDA v20 REST API"
[6]: https://help.ctrader.com/open-api/ "cTrader Open API documentation"
[7]: https://developer.tastytrade.com/ "tastytrade developer documentation"
[8]: https://docs.tradier.com/ "Tradier API documentation"
[9]: https://docs.ccxt.com/ "CCXT documentation"
[10]: https://finnhub.io/docs/api "Finnhub API documentation"
[11]: https://twelvedata.com/docs "Twelve Data documentation"
[12]: https://massive.com/docs "Massive developer documentation"
[13]: https://www.alphavantage.co/documentation/ "Alpha Vantage API documentation"
[14]: https://site.financialmodelingprep.com/developer/docs "Financial Modeling Prep developer documentation"
[15]: https://eodhd.com/financial-apis/ "EODHD financial APIs"
[16]: https://databento.com/docs "Databento documentation"
[17]: https://www.tiingo.com/documentation/ "Tiingo API documentation"
[18]: https://docs.intrinio.com/documentation/api_v2/getting_started "Intrinio API documentation"
[19]: https://www.barchart.com/ondemand/api "Barchart OnDemand API"
[20]: https://docs.data.nasdaq.com/ "Nasdaq Data Link documentation"
[21]: https://docs.tradingeconomics.com/ "Trading Economics API documentation"
[22]: https://docs.apilayer.com/marketstack/docs/api-documentation "Marketstack API documentation"
[23]: https://api.unusualwhales.com/docs "Unusual Whales API documentation"
[24]: https://developers.binance.com/ "Binance developer documentation"
[25]: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/overview "Coinbase Advanced Trade API documentation"
[26]: https://docs.kraken.com/api/ "Kraken API documentation"
[27]: https://bybit-exchange.github.io/docs/v5/intro "Bybit V5 API documentation"
[28]: https://www.okx.com/okx-api "OKX API portal"
[29]: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api "Hyperliquid API documentation"
[30]: https://docs.coingecko.com/ "CoinGecko API documentation"
[31]: https://coinmarketcap.com/api/documentation/ "CoinMarketCap API documentation"
[32]: https://docs.coinglass.com/reference/getting-started-with-your-api "CoinGlass API introduction"
[33]: https://docs.glassnode.com/ "Glassnode documentation"
[34]: https://docs.nansen.ai/ "Nansen documentation"
[35]: https://docs.cryptoquant.com/ "CryptoQuant documentation"
[36]: https://docs.dune.com/api-reference/overview/introduction "Dune API documentation"
[37]: https://docs.coinmetrics.io/api/v4/ "Coin Metrics API v4 documentation"
[38]: https://docs.kaiko.com/ "Kaiko documentation"
[39]: https://docs.messari.io/introduction "Messari API documentation"
[40]: https://academy.santiment.net/sanapi/ "Santiment SANAPI documentation"
[41]: https://api-docs.defillama.com/ "DeFiLlama API documentation"
[42]: https://arkm.com/api/docs "Arkham API documentation"
[43]: https://developer.whale-alert.io/api-account/documentation "Whale Alert API documentation"
[44]: https://lunarcrush.com/en/developers/api "LunarCrush developer API"
[45]: https://docs.coinapi.io/ "CoinAPI documentation"
[46]: https://www.tradingview.com/support/solutions/43000474413-i-need-access-to-your-api-in-order-to-get-data-or-indicator-values/ "TradingView public API policy"
[47]: https://www.koyfin.com/pricing/ "Koyfin pricing"
[48]: https://www.coinquant.ai/pricing "CoinQuant pricing"
[49]: https://www.tradingcursor.com/pricing/ "TradingCursor pricing"
[50]: https://docs.lona.agency/ "LONA documentation"
[51]: https://help.trendspider.com/articles/webhooks "TrendSpider webhooks for alerts"
[52]: https://docs.luxalgo.com/docs/getting-started/introduction "LuxAlgo documentation"
[53]: https://cryptopanic.com/developers/api/ "CryptoPanic API reference"
[54]: https://docs.benzinga.io/ "Benzinga APIs documentation"
[55]: https://www.financialjuice.com/home "FinancialJuice product site"
[56]: https://www.gdeltproject.org/data.html "GDELT data access"
[57]: https://help.signalstack.com/ "SignalStack documentation"
[58]: https://clickhouse.com/docs "ClickHouse documentation"
[59]: https://questdb.com/docs/ "QuestDB documentation"
[60]: https://docs.timescale.com/ "Timescale documentation"
[61]: https://redis.io/docs/latest/ "Redis documentation"
[62]: https://kafka.apache.org/documentation/ "Apache Kafka documentation"
[63]: https://docs.nats.io/ "NATS documentation"
[64]: https://prometheus.io/docs/introduction/overview/ "Prometheus documentation"
[65]: https://grafana.com/docs/grafana/latest/ "Grafana documentation"
[66]: https://nautilustrader.io/docs/latest/ "NautilusTrader documentation"
[67]: https://vectorbt.dev/ "vectorbt documentation"
[68]: https://docs.freqtrade.io/en/latest/backtesting/ "Freqtrade backtesting documentation"
[69]: https://www.backtrader.com/docu/ "Backtrader documentation"
[70]: https://zipline.ml4trading.io/ "Zipline Reloaded documentation"
[71]: https://docs.jesse.trade/ "Jesse documentation"
[72]: https://hummingbot.org/docs/ "Hummingbot documentation"
[73]: https://kernc.github.io/backtesting.py/ "backtesting.py documentation"
[74]: https://github.com/ranaroussi/quantstats "QuantStats official repository"
[75]: https://riskfolio-lib.readthedocs.io/en/latest/ "Riskfolio-Lib documentation"
[76]: https://skfolio.org/user_guide/index.html "skfolio user guide"
[77]: https://pyportfolioopt.readthedocs.io/en/latest/ "PyPortfolioOpt documentation"
[78]: https://github.com/stefan-jansen/empyrical-reloaded "empyrical-reloaded repository"
[79]: https://github.com/stefan-jansen/pyfolio-reloaded "pyfolio-reloaded repository"
[80]: https://github.com/microsoft/qlib/blob/main/docs/index.rst "Microsoft Qlib documentation"
[81]: https://github.com/AI4Finance-Foundation/FinRL-Trading "FinRL-X official repository"
[82]: https://fingpt.io/docs "FinGPT documentation"
[83]: https://github.com/AI4Finance-Foundation/FinRL "FinRL official repository"
[84]: https://www.tensortrade.org/en/latest/ "TensorTrade documentation"
[85]: https://docs.langchain.com/oss/python/langgraph/overview "LangGraph documentation"
[86]: https://dspy.ai/ "DSPy documentation"
[87]: https://ta-lib.org/api/ "TA-Lib core API documentation"
[88]: https://xgboosted.github.io/pandas-ta-classic/ "pandas-ta-classic documentation"
[89]: https://technical-analysis-library-in-python.readthedocs.io/ "Technical Analysis Library in Python documentation"
[90]: https://tsfresh.readthedocs.io/en/stable/ "tsfresh documentation"
[91]: https://docs.featuretools.com/en/stable/ "Featuretools documentation"
[92]: https://mlfinpy.readthedocs.io/ "mlfinpy documentation"
[93]: https://tradingview.github.io/lightweight-charts/ "TradingView Lightweight Charts documentation"
[94]: https://plotly.com/python/ "Plotly Python documentation"
[95]: https://echarts.apache.org/en/index.html "Apache ECharts documentation"
[96]: https://www.highcharts.com/docs/stock/getting-started-stock "Highcharts Stock getting started"
[97]: https://docs.bokeh.org/en/latest/ "Bokeh documentation"
[98]: https://github.com/matplotlib/mplfinance "mplfinance official repository"

---

**Maintained by Manus AI.** Contributions are welcome when they add a material trading service or tool, cite official documentation, disclose whether SDKs are official or community-maintained, and include a clear pricing/status reference.
