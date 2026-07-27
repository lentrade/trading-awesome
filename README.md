# Awesome Trading Services, Market Data APIs & Crypto Analytics

![Trading awesome](https://i.postimg.cc/SstfKwXF/trading-awesome-github.jpg)

> A curated directory of **50+ trading services** for algorithmic traders, quantitative researchers, developers, and active investors. It covers broker and exchange APIs, stock and forex data, cryptocurrency market data, on-chain analytics, derivatives intelligence, charting, backtesting, and no-code trading research.

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

## Selection principles

This directory focuses on services with a material role in data acquisition, research, risk monitoring, trade execution, or trading automation. I included both retail-accessible tools and enterprise-grade data vendors because production workflows often combine them: for example, an execution broker, a market-data provider, an on-chain source, and a research environment.

A service is not ranked highly merely because it is expensive, popular, or has a large marketing footprint. The highest positions favor robust public documentation, broad and usable coverage, credible developer tooling, and direct relevance to a real trading workflow. A specialized product may appear lower in the overall ranking yet still be the most appropriate choice for a particular task, such as DeFi TVL research, liquidation monitoring, options flow, or macroeconomic calendars.

## Practical integration checklist

Before connecting any service to a live workflow, verify the following items directly with the provider. The list is intentionally operational rather than promotional.

| Check | Why it matters |
| --- | --- |
| **License and redistribution rights** | A market-data API may permit personal use but prohibit display, resale, caching, or redistribution. |
| **Latency and adjustment basis** | Real-time, delayed, end-of-day, split-adjusted, and unadjusted prices answer different questions. |
| **Regional and account eligibility** | Broker, exchange, leverage, derivative, and API capabilities can differ materially by residence and legal entity. |
| **Rate limits and retry behavior** | Stable automation requires documented throttling, idempotency handling, retries, and monitoring. |
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

---

**Maintained by Manus AI.** Contributions are welcome when they add a material trading service, cite official documentation, disclose whether SDKs are official or community-maintained, and include a clear pricing/status reference.
