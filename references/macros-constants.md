# P123 Macros, Constants & Universe Reference

## Table of Contents
1. [Numeric Constants](#constants)
2. [Price & Portfolio IDs](#price-ids)
3. [Universe IDs](#universes)
4. [Macro Constants (FRED Data)](#macros)
5. [S&P 500 Aggregate IDs](#sp500)
6. [FX Rates](#fx)
7. [Streak Constants](#streak)

---

## Numeric Constants <a name="constants"></a>

| Constant | Value | Description |
|----------|-------|-------------|
| `#Week` | 5 | Trading days in a week |
| `#Month` | 21 | Trading days in a month |
| `#Month3` | 62 | Trading days in 3 months |
| `#Month6` | 125 | Trading days in 6 months |
| `#Year` | 251 | Trading days in a year |
| `#Year2` | 501 | Trading days in 2 years |
| `TRUE` | 1 | Boolean true |
| `FALSE` | 0 | Boolean false |
| `NA` | — | Missing value |
| `FALLBACK` | — | Fall back to previous period (NA handling) |
| `KEEPNA` | — | Keep NA values |
| `ZERONA` | — | Set NA values to 0 |

---

## Price & Portfolio IDs <a name="price-ids"></a>

| ID | Description |
|----|-------------|
| `#Close` | Stock closing prices |
| `#Open` | Stock opening prices |
| `#High` | Stock high prices |
| `#Low` | Stock low prices |
| `#Bench` | Current benchmark closing prices |
| `#Equity` | Portfolio/strategy total value |
| `#TNX` | 10Y Treasury coupon on $1000 (÷10 for yield) |
| `#Industry` | Industry index |
| `#Sector` | Sector index |
| `$TICKER` | Any ticker (e.g., `$SPY`, `$QQQ`, `$IWM`) |

**Usage**: `Close(0, #Bench)`, `SMA(50, 0, $SPY)`, `Close(0, #Industry)`

---

## Universe IDs <a name="universes"></a>

### Major USA
| ID | Description |
|----|-------------|
| `SP500` | S&P 500 (iShares IVV) |
| `SP400` | S&P 400 MidCap (iShares IJH) |
| `SP600` | S&P 600 SmallCap (iShares IJR) |
| `SP1500` | S&P 1500 Composite |
| `Prussell1000` | Russell 1000 |
| `Prussell2000` | Russell 2000 |
| `Prussell3000` | Russell 3000 |
| `DJIA` | Dow Jones Industrial Average |
| `NASDAQ100` | Nasdaq 100 |

### Other USA
| ID | Description |
|----|-------------|
| `LargeCap` | Large Cap stocks |
| `MidCap` | Mid Cap stocks |
| `SmallCap` | Small Cap stocks |
| `MicroCap` | Micro Cap stocks |
| `NanoCap` | Nano Cap stocks |
| `NYSE` | NYSE-listed only |
| `NASD` | NASDAQ-listed only |
| `NYSEMKT` | NYSE MKT (formerly AMEX) |
| `OTC` | Over The Counter |
| `NOOTC` | No OTC (exclude OTC stocks) |
| `$ADR` | American Depositary Receipts |
| `MasterLP` | Master Limited Partnerships |
| `TRADEUSA` | Easy to Trade US (liquidity-filtered) |

### USA — All Listings
| ID | Description |
|----|-------------|
| `ALLFUND` | United States — all stocks with fundamentals (incl. Foreign Primary) |
| `PRIMARYUSA` | United States (Primary listings only) |
| `ALLSTOCKS` | United States — all listed stocks |

### Canada
| ID | Description |
|----|-------------|
| `ALLFUNDCAN` | Canada — all stocks with fundamentals (incl. Foreign Primary) |
| `PRIMARYCAN` | Canada (Primary listings only) |
| `ALLSTOCKSCAN` | Canada — all listed stocks |
| `ALLFUNDCDRCAD` | Canada (incl. Foreign Primary and CDRs) |
| `CanadaTrust` | Canadian trusts |
| `CDR` | Canadian Depositary Receipts |
| `SPTSX` | S&P/TSX Composite |
| `SPTSX60` | S&P/TSX 60 |
| `TSX` | Toronto Stock Exchange |
| `TSXV` | TSX Venture Exchange |

### Europe
| ID | Description |
|----|-------------|
| `ALLFUNDEUR` | Europe — all stocks with fundamentals (incl. Foreign Primary) |
| `PRIMARYEUR` | Europe (Primary listings only) |
| `EU200L` | Europe 200 Large Cap |
| `EU200M` | Europe 200 Mid Cap |
| `EU200S` | Europe 200 Small Cap |
| `EU600` | Europe 600 |

### Multi-region
| ID | Description |
|----|-------------|
| `PRIMARYNOAM` | North America (Primary listings) |
| `PRIMARYNOAT` | North Atlantic (Primary listings) |
| `TRADENOAM` | Easy to Trade North America (liquidity-filtered) |
| `TRADENOAT` | Easy to Trade North Atlantic (liquidity-filtered) |
| `TRADEEUR` | Easy to Trade Europe (liquidity-filtered) |

### Special
| ID | Description |
|----|-------------|
| `ApiUniverse` | Custom universe created via API |

---

## Macro Constants (FRED Data) <a name="macros"></a>

All macro constants use `##` prefix and map to FRED series.

### Interest Rates & Bonds

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##FEDFUNDS` | DFF | Federal Funds Rate | Daily |
| `##PRIME` | MPRIME | Prime Loan Rate | Monthly |
| `##MORT30Y` | MORTGAGE30US | 30-Year Fixed Mortgage | Weekly |
| `##SOFR3MO` | SOFR90DAYAVG | 90-Day Avg SOFR | Daily |

### Treasury Bills (T-Bills)

| Constant | FRED ID | Freq |
|----------|---------|------|
| `##UST1MO` | DGS1MO | Daily |
| `##UST3MO` | DGS3MO | Daily |
| `##UST1YR` | DGS1 | Daily |

### Treasury Notes (T-Notes)

| Constant | FRED ID | Freq |
|----------|---------|------|
| `##UST2YR` | DGS2 | Daily |
| `##UST3YR` | DGS3 | Daily |
| `##UST5YR` | DGS5 | Daily |
| `##UST6MO` | DGS6MO | Daily |
| `##UST7YR` | DGS7 | Daily |

### Treasury Bonds (T-Bonds)

| Constant | FRED ID | Freq |
|----------|---------|------|
| `##UST10YR` | DGS10 | Daily |
| `##UST20YR` | DGS20 | Daily |
| `##UST30YR` | DGS30 | Daily |
| `##USR10YR` | ⚠️ P123 maps to RTWEXBGS (Real Broad Dollar Index) — likely a P123 documentation error; not actually 10Y real rate | Monthly |

### International Government Bonds

| Constant | FRED ID | Description |
|----------|---------|-------------|
| `##CAT10YR` | IRLTLT01CAM156N | Canada 10Y |
| `##GBT10YR` | IRLTLT01GBM156N | UK 10Y |
| `##EUT10YR` | IRLTLT01EZM156N | Eurozone 10Y |
| `##CHT10YR` | IRLTLT01CHM156N | Switzerland 10Y |

### International Interbank Rates

| Constant | FRED ID | Description |
|----------|---------|-------------|
| `##CAB3MO` | IR3TIB01CAM156N | Canada 3M |
| `##EUB3MO` | IR3TIB01EZM156N | Eurozone 3M |
| `##GBB3MO` | IR3TIB01GBM156N | UK 3M |

### Corporate Bonds & Spreads

| Constant | FRED ID | Description |
|----------|---------|-------------|
| `##CORPAAA` | BAMLC0A1CAAAEY | US Corp AAA Yield |
| `##CORPBBB` | BAMLC0A4CBBBEY | US Corp BBB Yield |
| `##CORPBB` | BAMLH0A1HYBBEY | High Yield BB |
| `##CORPB` | BAMLH0A2HYBEY | High Yield B |
| `##CORPJNK` | BAMLH0A3HYCEY | CCC or Below Yield |
| `##CORPBBBOAS` | BAMLC0A4CBBB | BBB OAS |
| `##CORPBBOAS` | BAMLH0A0HYM2 | HY Master II OAS |

### Inflation & Prices

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##CPI` | CPIAUCSL | CPI All Urban | Monthly |
| `##PPI` | WPSFD49207 | PPI Finished Goods | Monthly |
| `##HPRICES` | CSUSHPINSA | Case-Shiller 20-City HPI | Monthly |
| `##INFLEXP` | MICH | UMich Inflation Expectation | Monthly |

### GDP & Economic Activity

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##RGDP` | GDPC1 | Real GDP | Quarterly |
| `##GNP` | GNP | Gross National Product | Quarterly |
| `##INDPRO` | INDPRO | Industrial Production | Monthly |
| `##CAPUTIL` | TCU | Capacity Utilization | Monthly |
| `##PCE` | PCE | Personal Consumption Expenditures | Monthly |
| `##RPCE` | PCEC96 | Real PCE | Monthly |
| `##DBTGDP` | GFDEGDQ188S | Debt/GDP | Quarterly |
| `##USSLIND` | USALOLITONOSTSAM | US Leading Index | Monthly |

### Employment & Labor

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##UNRATE` | UNRATE | Unemployment Rate | Monthly |
| `##UNTOT` | U6RATE | Total Unemployed (U6) | Monthly |
| `##UNTEEN` | LNS14000012 | Youth Unemployment | Monthly |
| `##CLAIMSNEW` | ICSA | Initial Claims | Weekly |
| `##CLAIMSCONTINUE` | CCSA | Continued Claims | Weekly |
| `##NONFARMEMPL` | PAYEMS | Total Nonfarm Payrolls | Monthly |
| `##CIVLABOR` | CLF16OV | Civilian Labor Force | Monthly |
| `##LABORPARTIC` | CIVPART | Labor Force Participation | Monthly |

### Money Supply

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##M1` | M1SL | M1 Money Stock | Monthly |
| `##M2` | M2SL | M2 Money Stock | Monthly |
| `##VELM1` | M1V | Velocity of M1 | Quarterly |
| `##VELM2` | M2V | Velocity of M2 | Quarterly |
| `##ADJMBASE` | BOGMBASE | Monetary Base | Monthly |

### Sentiment & Stress

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##UMCSENT` | UMCSENT | UMich Consumer Sentiment | Monthly |
| `##RECPROB` | RECPROUSM156N | Recession Probability | Monthly |
| `##STRESS` | STLFSI4 | STL Fed Financial Stress | Weekly |

### Manufacturing & Business

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##ORDERSDUR` | DGORDER | Durable Goods Orders | Monthly |
| `##ORDERSCAP` | NEWORDER | Nondefense Capital Goods Orders | Monthly |
| `##INV2SHIP` | AMTMUS | Inventories/Shipments (Mfg) | Monthly |
| `##INV2SLS` | ISRATIO | Total Inventories/Sales | Monthly |
| `##HSTARTS` | HOUST | Housing Starts | Monthly |
| `##CONSTR` | TTLCONS | Total Construction Spending | Monthly |

### Income & Savings

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##RDISPINC` | DSPIC96 | Real Disposable Income | Monthly |
| `##SAVING` | PSAVERT | Personal Saving Rate | Monthly |
| `##RMINCOME` | MEHOINUSA672N | Real Median Income | Annual |
| `##HDEBTSERV` | TDSP | Household Debt Service % | Quarterly |

### Oil & Commodities

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##OIL` | DCOILWTICO | WTI Crude Oil | Daily |

### Dollar Index

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##NBDI` | DTWEXBGS | Nominal Broad Dollar Index | Daily |
| `##RBDI` | RTWEXBGS | Real Broad Dollar Index | Monthly |

### Retail & Vehicles

| Constant | FRED ID | Description | Freq |
|----------|---------|-------------|------|
| `##SALESRET` | RSXFS | Retail Sales ex Food Services | Monthly |
| `##SALESALLVEH` | TOTALSA | Total Vehicle Sales | Monthly |
| `##SALESAUTO` | ALTSALES | Light Vehicle Sales | Monthly |

**Usage in formulas**:
```
// Yield curve spread (10Y - 2Y)
##UST10YR - ##UST2YR

// Risk premium above fed funds
EarnYield - ##FEDFUNDS / 100

// Fed funds rate in SMA
SMA(21, 0, ##FEDFUNDS)

// Oil price moving average
SMA(50, 0, ##OIL) > SMA(200, 0, ##OIL)
```

---

## S&P 500 Aggregate IDs <a name="sp500"></a>

| Constant | Description | Freq |
|----------|-------------|------|
| `#SPEPSTTM` | S&P 500 EPS TTM | Weekly |
| `#SPEPSCY` | S&P 500 EPS Current Year estimate | Weekly |
| `#SPEPSNY` | S&P 500 EPS Next Year estimate | Weekly |
| `#SPEPSQ` | S&P 500 EPS Blend Q | Weekly |
| `#SPEPSCNY` | S&P 500 EPS Blend Y (time-weighted CY/NY) | Weekly |
| `#SPYield` | S&P 500 Earnings Yield | Weekly |
| `#SPYieldBlend` | S&P 500 Earnings Yield (blended) | Weekly |
| `#SPRP` | S&P 500 Risk Premium | Weekly |
| `#SPRPBlend` | S&P 500 Risk Premium (blended) | Weekly |

```
// S&P 500 forward PE
Close(0, $SPY) / #SPEPSCNY

// Equity risk premium vs 10Y Treasury
#SPRP
```

---

## FX Rates <a name="fx"></a>

All use `#USD` prefix + 3-letter currency code:

`#USDEUR`, `#USDGBP`, `#USDJPY`, `#USDCHF`, `#USDCAD`, `#USDAUD`, `#USDNZD`, `#USDMXN`, `#USDNOK`, `#USDSEK`, `#USDPLN`, `#USDTRY`, `#USDZAR`, `#USDHKD`, `#USDSGD`, `#USDILS`, `#USDHUF`, `#USDCZK`, `#USDDKK`, `#USDRON`, `#USDRUB`, `#USDRSD`, `#USDBGN`, `#USDBAM`, `#USDHRK`, `#USDISK`, `#USDLVL`, `#USDMKD`, `#USDSKK`, `#USDUAH`

```
// EUR/USD moving average
SMA(50, 0, #USDEUR)
```

---

## Streak Constants <a name="streak"></a>

| Constant | Description |
|----------|-------------|
| `#Positive` | Positive values streak |
| `#NotPositive` | Non-positive values streak |
| `#Increasing` | Increasing values streak |
| `#NotIncreasing` | Non-increasing values streak |

Used with `LoopStreak()` function (see advanced-functions.md):
```
LoopStreak("Close(0) - Close(CTR)", 20, 1, 1, #Positive)   // consecutive price increases
LoopStreak("SalesGr%PYQ", 12, 0, 1, #Positive)             // quarters of positive YoY sales growth
```
