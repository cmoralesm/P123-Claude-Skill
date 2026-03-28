# Misc

Functions that do not fit into any other category.

## Time Series IDs

Series IDs that can be used as the series parameters in functions, or in the charts section. For example you can retrieve the latest value of the SP500 Index with:<br><br>Close(0,$SP500)<br><br>See the Full Description of each ID for more examples.

### S&P 500 IDs

SP500 Risk Premium (weekly)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#SPRPBlend` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPRPBlend |
| `#SPYieldBlend` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPYieldBlend |
| `#SPEPSCNY` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPEPSCNY |
| `#SPEPSQ` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPEPSQ |
| `#SPEPSTTM` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPEPSTTM |


### Index Tickers - Major

S&P 400 Mid

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `$MID` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$MID |
| `$RUA` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$RUA |
| `$RUI` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$RUI |
| `$RUT` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$RUT |
| `$SML` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SML |
| `$SP500` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SP500 |
| `$SP500EQ` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SP500EQ |
| `$SPALL` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALL |


### Index Tickers - Specialty

Dow Jones

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `$DJIA` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$DJIA |
| `$MIDPG` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$MIDPG |
| `$MIDPV` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$MIDPV |
| `$NASDAQ` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$NASDAQ |
| `$NASDAQ100` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$NASDAQ100 |
| `$SMLPG` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SMLPG |
| `$SMLPV` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SMLPV |
| `$SP500PG` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SP500PG |
| `$SP500PV` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SP500PV |
| `$SPALLCND` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLCND |
| `$SPALLCNS` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLCNS |
| `$SPALLENG` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLENG |
| `$SPALLEUT` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLEUT |
| `$SPALLFIN` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLFIN |
| `$SPALLGLD` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLGLD |
| `$SPALLHEA` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLHEA |
| `$SPALLHEQ` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLHEQ |
| `$SPALLIND` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLIND |
| `$SPALLINT` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLINT |
| `$SPALLMAT` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLMAT |
| `$SPALLPBL` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLPBL |
| `$SPALLPG` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLPG |
| `$SPALLPV` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLPV |
| `$SPALLTCM` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLTCM |
| `$SPALLUTL` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$SPALLUTL |
| `$VIX` | series |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=$VIX |


### Misc IDs

Current benchmark closing prices (daily)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Bench` | series |  |  |
| `#Equity` | series |  |  |
| `#TNX` | series |  |  |


### Price IDs

Stock closing prices (daily)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Close` | series |  |  |
| `#High` | series |  |  |
| `#Low` | series |  |  |
| `#Open` | series |  |  |


## Macro Series IDs (Adjusted)

FRED macro series that are seasonally adjusted.

### Macro - Other Economic Activity

Debt as Percent of GDP (quarterly)

Corresponding FRED id=GFDEGDQ188S

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##DBTGDP` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##DBTGDP |
| `##DOMINV` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##DOMINV |
| `##PCE` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##PCE |
| `##RPCE` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RPCE |
| `##SAVING` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SAVING |
| `##SURPLUS` | series | Annual | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SURPLUS |
| `##USSLIND` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##USSLIND |


### Macro - Delinquency Rate

Delinquency Rate On Credit Card Loans, All Commercial Banks (quarterly)

Corresponding FRED id=DRCCLACBS

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##DELINQCC` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##DELINQCC |
| `##DELINQMORT` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##DELINQMORT |


### Macro - GDP/GNP

Gross National Product (quarterly)

Corresponding FRED id=GNP

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##GNP` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##GNP |
| `##RGDP` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RGDP |


### Macro - Income

Household Debt Service Payments as a Percent of Disposable Personal Income (quarterly)

Corresponding FRED id=TDSP

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##HDEBTSERV` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##HDEBTSERV |
| `##RDISPINC` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RDISPINC |
| `##RINCPERCAP` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RINCPERCAP |
| `##RMINCOME` | series | Annual | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RMINCOME |


### Macro - Labor Force

Civilian Labor Force (monthly)

Corresponding FRED id=CLF16OV

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CIVLABOR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CIVLABOR |
| `##LABORPARTIC` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##LABORPARTIC |
| `##NONFARMEMPL` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##NONFARMEMPL |
| `##POPUL` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##POPUL |
| `##UNWANT` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UNWANT |


### Macro - Manufacturing

Ratio of Total Inventories to Shipments for All Manufacturing Industries (monthly)

Corresponding FRED id=AMTMUS

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##INV2SHIP` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##INV2SHIP |
| `##ORDERSCAP` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##ORDERSCAP |
| `##ORDERSDUR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##ORDERSDUR |
| `##ORDERSUNFILL` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##ORDERSUNFILL |
| `##WAGES` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##WAGES |


### Macro - Money, M1, M2

Monetary Base; Total (monthly)

Corresponding FRED id=BOGMBASE

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##ADJMBASE` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##ADJMBASE |
| `##M1` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##M1 |
| `##M2` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##M2 |
| `##USCURRACCT` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##USCURRACCT |
| `##VELM1` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##VELM1 |
| `##VELM2` | series | Quarterly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##VELM2 |


### Macro - Other Business Activity

Capacity Utilization: Total Industry (monthly)

Corresponding FRED id=TCU

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CAPUTIL` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CAPUTIL |
| `##CONSTR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CONSTR |
| `##HSTARTS` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##HSTARTS |
| `##INDPRO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##INDPRO |
| `##INV2SLS` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##INV2SLS |
| `##INVTOT` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##INVTOT |
| `##SALESRET` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SALESRET |
| `##SALESRETFD` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SALESRETFD |


### Macro - Price Index, CPI, PPI, HPI

CPI All Urban Consumers: All Items (monthly)

Corresponding FRED id=CPIAUCSL

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CPI` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CPI |
| `##HPRICES` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##HPRICES |
| `##PPI` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##PPI |


### Macro - Sentiment

Smoothed U.S. Recession Probabilities (monthly)

Corresponding FRED id=RECPROUSM156N

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##RECPROB` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RECPROB |
| `##UMCSENT` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UMCSENT |
| `##INFLEXP` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##INFLEXP |


### Macro - Unemployment

Continued Claims (Insured Unemployment) (weekly)

Corresponding FRED id=CCSA

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CLAIMSCONTINUE` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CLAIMSCONTINUE |
| `##CLAIMSNEW` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CLAIMSNEW |
| `##UNDURATION` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UNDURATION |
| `##UNRATE` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UNRATE |
| `##UNTEEN` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UNTEEN |
| `##UNTOT` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UNTOT |


### Macro - Vehicle, Automobile

Auto Inventory/Sales Ratio (monthly)

Corresponding FRED id=AISRSA

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##INV2SLSAUTO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##INV2SLSAUTO |
| `##PRODAUTO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##PRODAUTO |
| `##SALESALLVEH` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SALESALLVEH |
| `##SALESAUTO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SALESAUTO |


## Macro Series IDs (Unadjusted)

FRED macro series that are not seasonally adjusted.

### Macro - Currency

Nominal Broad U.S. Dollar Index (daily)

Corresponding FRED id=DTWEXBGS

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##NBDI` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##NBDI |
| `##RBDI` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RBDI |


### Macro - Interbank Rate

3-Month Interbank Rate for Canada (monthly)

Corresponding FRED id=IR3TIB01CAM156N

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CAB3MO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CAB3MO |
| `##EUB3MO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##EUB3MO |
| `##GBB3MO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##GBB3MO |
| `##NOB3MO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##NOB3MO |
| `##PLB3MO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##PLB3MO |
| `##SEB3MO` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SEB3MO |


### Macro - Interest, Mortgage, Prime, TED

90-Day Average SOFR (daily)

Corresponding FRED id=SOFR90DAYAVG

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##SOFR3MO` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##SOFR3MO |
| `##USR10YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##USR10YR |
| `##FEDFUNDS` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##FEDFUNDS |
| `##MORT30Y` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##MORT30Y |
| `##PRIME` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##PRIME |


### Macro - Treasury notes (T-notes)

10-Year Government Bond Yield for Canada (monthly)

Corresponding FRED id=IRLTLT01CAM156N

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CAT10YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CAT10YR |
| `##CHT10YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CHT10YR |
| `##EUT10YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##EUT10YR |
| `##GBT10YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##GBT10YR |
| `##UST6MO` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST6MO |
| `##UST2YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST2YR |
| `##UST3YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST3YR |
| `##UST5YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST5YR |
| `##UST7YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST7YR |
| `##UST10YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST10YR |


### Macro - FX Rates

USD to AUD

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#USDAUD` | series |  |  |
| `#USDBAM` | series |  |  |
| `#USDBGN` | series |  |  |
| `#USDCAD` | series |  |  |
| `#USDCHF` | series |  |  |
| `#USDCZK` | series |  |  |
| `#USDDKK` | series |  |  |
| `#USDEUR` | series |  |  |
| `#USDGBP` | series |  |  |
| `#USDHKD` | series |  |  |
| `#USDHRK` | series |  |  |
| `#USDHUF` | series |  |  |
| `#USDILS` | series |  |  |
| `#USDISK` | series |  |  |
| `#USDJPY` | series |  |  |
| `#USDLVL` | series |  |  |
| `#USDMKD` | series |  |  |
| `#USDMXN` | series |  |  |
| `#USDNOK` | series |  |  |
| `#USDNZD` | series |  |  |
| `#USDPLN` | series |  |  |
| `#USDRON` | series |  |  |
| `#USDRSD` | series |  |  |
| `#USDRUB` | series |  |  |
| `#USDSEK` | series |  |  |
| `#USDSGD` | series |  |  |
| `#USDSKK` | series |  |  |
| `#USDTRY` | series |  |  |
| `#USDUAH` | series |  |  |
| `#USDZAR` | series |  |  |


### Macro - Corporate Bonds

BofA Merrill Lynch US Corporate AAA Effective Yield© (daily)

Corresponding FRED id=BAMLC0A1CAAAEY

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##CORPAAA` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPAAA |
| `##CORPB` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPB |
| `##CORPBB` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPBB |
| `##CORPBBB` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPBBB |
| `##CORPBBBOAS` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPBBBOAS |
| `##CORPBBOAS` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPBBOAS |
| `##CORPJNK` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##CORPJNK |


### Macro - Oil, Gold Price

Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, OK (daily)

Corresponding FRED id=DCOILWTICO

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##OIL` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##OIL |


### Macro - Stress Index

St. Louis Fed Financial Stress Index© (weekly)

Corresponding FRED id=STLFSI4

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##STRESS` | series | Weekly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##STRESS |


### Macro - Treasury bills (T-bills)

1-Month Treasury Constant Maturity Rate (USD) (daily)

Corresponding FRED id=DGS1MO

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##UST1MO` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST1MO |
| `##UST3MO` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST3MO |
| `##UST1YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST1YR |


### Macro - Vacancy Rates

Home Vacancy Rate for the United States (annual)

Corresponding FRED id=USHVAC

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##HVACANCY` | series | Annual | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##HVACANCY |
| `##RVACANCY` | series | Annual | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##RVACANCY |


### Macro - Treasury bonds (T-bonds)

20-Year Treasury Constant Maturity Rate (USD) (daily)

Corresponding FRED id=DGS20

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `##UST20YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST20YR |
| `##UST30YR` | series | Weekday | https://www.portfolio123.com/doc/doc_detail.jsp?factor=##UST30YR |


### Compustat Macro - TO BE DEPRECATED

20-Year Treasury Yield (monthly)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#BOND20YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#BOND20YR |
| `#BOND30YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#BOND30YR |
| `#CABGDP2` | series | Quarterly* | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#CABGDP2 |
| `#CPI` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#CPI |
| `#EMPLOY` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#EMPLOY |
| `#FEDFUNDS` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#FEDFUNDS |
| `#GDP` | series | Quarterly* | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#GDP |
| `#HOUSE` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#HOUSE |
| `#M1` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#M1 |
| `#M2` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#M2 |
| `#NOTE10YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#NOTE10YR |
| `#NOTE2YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#NOTE2YR |
| `#NOTE3YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#NOTE3YR |
| `#NOTE5YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#NOTE5YR |
| `#NOTE7YR` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#NOTE7YR |
| `#POPT` | series | Annual* | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#POPT |
| `#PPI` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#PPI |
| `#PRIME` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#PRIME |
| `#RTLSALES` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#RTLSALES |
| `#TBILL12M` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#TBILL12M |
| `#TBILL3M` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#TBILL3M |
| `#TBILL6M` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#TBILL6M |
| `#UNEMP` | series | Monthly | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#UNEMP |


## Group

Functions that perform calculations on groups of stocks or that identify individual stocks.

### Company Name

Returns 1(TRUE) if the company name is in the list, 0 (FALSE) otherwise. You can also use wildcards * to match any string or ? for any character

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CoName()` | "name" |  |  |


### Stock is in Custom List

Returns 1 if the stock is in your custom list, 0 otherwise. To enter a custom list go to TOOLS->Lists->Custom. Ex: to only buy stocks in your list "MyList" enter the following Buy rule:

InList("MyList")

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `InList()` | "MyListName" |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=InList |


### Unique ID Odd or Even

Returns 1 (TRUE) if the internal ID of the stock or ETF is Even, 0 (FALSE) otherwise. Can be used for data-mining to create two samples from the universe.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EvenID` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EvenID |


### Universe filter

Returns 1 if the stock is in the universe, 0 otherwise. Ex: to only buy S&P 500 stocks enter the following Buy rule:

Universe(SP500)

To see all universes click on 'Full Description'

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Universe()` | uname |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Universe |


## RBICS Codes

RBICS codes that can be used in the RBICS() function.

### Business Services

10 - Business Services

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `BIZSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIZSVCE |
| `BIZSVCESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIZSVCESS |
| `MKTINGPRINTING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MKTINGPRINTING |
| `ADVERTISING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ADVERTISING |
| `PRINTING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRINTING |
| `PROSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PROSVCE |
| `ADMINSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ADMINSVCE |
| `CONSULTING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSULTING |
| `PROSVCEOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PROSVCEOTHER |
| `BIZSUPPORT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIZSUPPORT |
| `FACILSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FACILSVCE |
| `SECURITYSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SECURITYSVCE |
| `WASTEMGMT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WASTEMGMT |
| `WASTECOLLECTION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WASTECOLLECTION |
| `HAZMAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HAZMAT |
| `WASTESVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WASTESVCE |
| `WASTEWATER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WASTEWATER |
| `ENVISVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ENVISVCE |
| `DEMOSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DEMOSVCE |


### Consumer Cyclicals

20 - Consumer Cyclicals

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CYCLICALS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CYCLICALS |
| `CONSUMERGOODS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERGOODS |
| `APPARELPRODUCTS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPARELPRODUCTS |
| `ACCESSORIESMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ACCESSORIESMFR |
| `CLOTHINGMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CLOTHINGMFR |
| `APPARELMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPARELMFR |
| `LEISURE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LEISURE |
| `LEISUREOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LEISUREOTHER |
| `RECREATIONALGOODS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RECREATIONALGOODS |
| `SPORTINGGOODS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SPORTINGGOODS |
| `APPLIANCESFURN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPLIANCESFURN |
| `RETAILMISC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RETAILMISC |
| `AUTORETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTORETAIL |
| `AUTOSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOSVCE |
| `AUTOSALES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOSALES |
| `AUTOPARTSSALESRENT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOPARTSSALESRENT |
| `RETAILOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RETAILOTHER |
| `AUCTION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUCTION |
| `GASSTATION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GASSTATION |
| `OFFICESUPPLY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OFFICESUPPLY |
| `PETS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PETS |
| `RETAILSOFTW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RETAILSOFTW |
| `EVSTATION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EVSTATION |
| `CANNABISRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CANNABISRETAIL |
| `HOMEBUILDMANUF` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEBUILDMANUF |
| `HOMEBUILD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEBUILD |
| `MFRBUILDING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MFRBUILDING |
| `VEHICLESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=VEHICLESS |
| `VEHICLE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=VEHICLE |
| `AUTOPARTSMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOPARTSMFR |
| `AUTOMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOMFR |
| `CONSUMERRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERRETAIL |
| `APPARELRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPARELRETAIL |
| `ACCESSORIESRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ACCESSORIESRETAIL |
| `CLOTHINGACCESSORIESRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CLOTHINGACCESSORIESRETAIL |
| `CLOTHINGRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CLOTHINGRETAIL |
| `SHOES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SHOES |
| `ELECTRONICSENTRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONICSENTRETAIL |
| `ELECTRONICSRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONICSRETAIL |
| `ENTRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ENTRETAIL |
| `ELECTRONICSENTMIXRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONICSENTMIXRETAIL |
| `HOMEIMPROVE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEIMPROVE |
| `BUILDINGMAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BUILDINGMAT |
| `STOREFURNITURE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=STOREFURNITURE |
| `HOMEIMPROV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEIMPROV |


### Consumer Non-Cyclicals

50 - Consumer Non-Cyclicals

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NONCYCLICAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NONCYCLICAL |
| `STAPLESRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=STAPLESRETAIL |
| `FOODDRINKRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOODDRINKRETAIL |
| `STOREFOOD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=STOREFOOD |
| `FOODDRINKRETAILGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOODDRINKRETAILGEN |
| `GROCERY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GROCERY |
| `RETAILDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RETAILDISTRIB |
| `GENMERCH` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GENMERCH |
| `STOREDEPT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=STOREDEPT |
| `STOREDISC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=STOREDISC |
| `MERCHRETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MERCHRETAIL |
| `OFFPRICERETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OFFPRICERETAIL |
| `WAREHOUSECLUB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WAREHOUSECLUB |
| `PERSONALCARERETAIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERSONALCARERETAIL |
| `PERSONALCARERETAILGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERSONALCARERETAILGEN |
| `PERSONALCARERETAILOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERSONALCARERETAILOTHER |
| `PHARMACY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PHARMACY |
| `FOODPRODUCTION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOODPRODUCTION |
| `AGRICULTURE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AGRICULTURE |
| `ANIMAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ANIMAL |
| `CROP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CROP |
| `AGRICDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AGRICDIV |
| `AGRICSUPPORT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AGRICSUPPORT |
| `FOODDRINKMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOODDRINKMFR |
| `BEVERAGE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BEVERAGE |
| `FOOD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOOD |
| `FOODDRINKMFRGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOODDRINKMFRGEN |
| `TOBACCO` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TOBACCO |
| `CIGARETTE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CIGARETTE |
| `TOBACCOMFRGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TOBACCOMFRGEN |
| `TOBACCOPRODUCT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TOBACCOPRODUCT |
| `ECIGARETTE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ECIGARETTE |
| `CANNABIS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CANNABIS |
| `PRODHOUSESUBSECT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRODHOUSESUBSECT |
| `APPLIANCESTOOLS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPLIANCESTOOLS |
| `APPLIANCESTOOLSDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPLIANCESTOOLSDIV |
| `APPLIANCESSMALL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=APPLIANCESSMALL |
| `PRODHOUSEIND` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRODHOUSEIND |
| `BABYMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BABYMFR |
| `PRODHOUSEDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRODHOUSEDIV |
| `HOMEOFFICEFURNMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEOFFICEFURNMFR |
| `PERSONALCAREPRODUCT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERSONALCAREPRODUCT |
| `ABSORBENT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ABSORBENT |
| `COSMETICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COSMETICS |
| `FRAGRANCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FRAGRANCE |
| `PERSONALCAREGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERSONALCAREGEN |
| `HAIRCARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HAIRCARE |
| `CLEANING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CLEANING |
| `SANITARY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SANITARY |
| `SKINCARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SKINCARE |
| `HOUSESVCESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOUSESVCESS |
| `HOUSESVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOUSESVCE |
| `EDUCATION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EDUCATION |
| `PERSONALSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERSONALSVCE |


### Consumer Services

15 - Consumer Services

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CONSUMERSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERSVCE |
| `HOSPITALITYSS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOSPITALITYSS |
| `HOSPITALITY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOSPITALITY |
| `HOTEL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOTEL |
| `ARTSENT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ARTSENT |
| `FOODDRINKSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOODDRINKSVCE |
| `RESTAURANT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RESTAURANT |
| `TRAVEL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRAVEL |
| `MEDIAPUBSS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDIAPUBSS |
| `MEDIAPUB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDIAPUB |
| `BROADCAST` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BROADCAST |
| `ENTERTAINMENT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ENTERTAINMENT |
| `BOOKS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BOOKS |


### Energy

25 - Energy

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ENERGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ENERGY |
| `UPSTREAMENERGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UPSTREAMENERGY |
| `COAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COAL |
| `COALAMER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COALAMER |
| `COALASIA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COALASIA |
| `COALINTL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COALINTL |
| `URANIUMRADIUMVANADIUM.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=URANIUMRADIUMVANADIUM.XX1 |
| `RADIUMVANADIUM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RADIUMVANADIUM |
| `URANIUM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=URANIUM |
| `COALSTREAMING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COALSTREAMING |
| `FOSSILFUEL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOSSILFUEL |
| `FOSSILFUELAMER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOSSILFUELAMER |
| `FOSSILFUELINT.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOSSILFUELINT.XX1 |
| `FOSSILFUELOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOSSILFUELOTHER |
| `OILGASSUPPORT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OILGASSUPPORT |
| `OILGASTRANSPORT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OILGASTRANSPORT |
| `OILGASFIELD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OILGASFIELD |
| `OILGASOPER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OILGASOPER |
| `DOWNMIDSTREAMENERGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DOWNMIDSTREAMENERGY |
| `DOWNSTREAMENERGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DOWNSTREAMENERGY |
| `LPGPROPANE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LPGPROPANE |
| `REFINERIES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REFINERIES |
| `MIDSTREAMENERGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MIDSTREAMENERGY |
| `NATGASPIPELINE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NATGASPIPELINE |
| `PIPELINEOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PIPELINEOTHER |
| `PETROLPIPELINE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PETROLPIPELINE |
| `GATHERPROCESSSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GATHERPROCESSSVCE |
| `OILGASINTEGSS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OILGASINTEGSS |
| `OILGASINTEG` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OILGASINTEG |


### Finance

30 - Finance

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FINANCIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINANCIAL |
| `BANKS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKS |
| `BANKSINTL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSINTL |
| `BANKSAMEREXUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSAMEREXUS |
| `BANKSASIA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSASIA |
| `BANKSEUROPE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSEUROPE |
| `BANKSMULTINAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSMULTINAT |
| `BANKSMORTG` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSMORTG |
| `BANKSUSA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSUSA |
| `BANKSCOMMERCIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSCOMMERCIAL |
| `SAVINGSLOAN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SAVINGSLOAN |
| `CREDITUNIONS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CREDITUNIONS |
| `BANKSINTERNET` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BANKSINTERNET |
| `INSURANCESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSURANCESS |
| `INSURANCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSURANCE |
| `INSBROKER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSBROKER |
| `INSLIFEHEALTH` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSLIFEHEALTH |
| `INSPROPCAS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSPROPCAS |
| `INSRE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSRE |
| `INSDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INSDIV |
| `INVESTSVCESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INVESTSVCESS |
| `INVESTSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INVESTSVCE |
| `ASSETMGMT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ASSETMGMT |
| `INVESTBANK` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INVESTBANK |
| `INVESTHOLDING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INVESTHOLDING |
| `SECURITIES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SECURITIES |
| `INVESTDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INVESTDIV |
| `REALESTATE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REALESTATE |
| `HOMEBUILDMANUF.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEBUILDMANUF.XX1 |
| `HOMEBUILD.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HOMEBUILD.XX1 |
| `MFRBUILDING.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MFRBUILDING.XX1 |
| `REALESTATESVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REALESTATESVCE |
| `REALESTATESVCEOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REALESTATESVCEOTHER |
| `PROPERTY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PROPERTY |
| `REIT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REIT |
| `REITDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REITDIV |
| `REITEQUITY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REITEQUITY |
| `REITMORTG` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=REITMORTG |
| `FINSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINSVCE |
| `FINSPECIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINSPECIAL |
| `FINCOMMSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINCOMMSVCE |
| `FINCONSUMERSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINCONSUMERSVCE |
| `FINSOFTW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINSOFTW |


### Healthcare

35 - Healthcare

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `HEALTHCARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HEALTHCARE |
| `BIOPHARMA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIOPHARMA |
| `BIOPHARMANONSYS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIOPHARMANONSYS |
| `INFECTIOUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INFECTIOUS |
| `ONCOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ONCOLOGY |
| `BIOPHARMAOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIOPHARMAOTHER |
| `ALLERGIES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ALLERGIES |
| `PAINMGMT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PAINMGMT |
| `SURGICAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SURGICAL |
| `TOXICOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TOXICOLOGY |
| `TRANSPLANTATION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRANSPLANTATION |
| `WEIGHTMGMT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WEIGHTMGMT |
| `BIOPHARMADIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIOPHARMADIV |
| `BIOPHARMASYS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIOPHARMASYS |
| `CARDIOVASCULAR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CARDIOVASCULAR |
| `DERMATOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DERMATOLOGY |
| `DIGESTIVE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DIGESTIVE |
| `ENDOCRINOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ENDOCRINOLOGY |
| `HEMATOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HEMATOLOGY |
| `IMMUNOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IMMUNOLOGY |
| `MUSCULOSKELETAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MUSCULOSKELETAL |
| `NEUROLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NEUROLOGY |
| `OBSTETRICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OBSTETRICS |
| `OPHTHALMOLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OPHTHALMOLOGY |
| `RESPIRATORY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RESPIRATORY |
| `UROLOGY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UROLOGY |
| `HCARESVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARESVCE |
| `HCARESUPPORT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARESUPPORT |
| `HPLAN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HPLAN |
| `HCAREADMIN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREADMIN |
| `HCAREDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREDISTRIB |
| `HCARESUPPORTOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARESUPPORTOTHER |
| `PATIENTCARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PATIENTCARE |
| `ACUTECARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ACUTECARE |
| `AMBULANCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AMBULANCE |
| `LTCARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LTCARE |
| `MULTIDELIVCARE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MULTIDELIVCARE |
| `AMBULANCEOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AMBULANCEOTHER |
| `HCAREMISC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREMISC |
| `NUTRITION` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NUTRITION |
| `OUTSOURCEDBIOMED` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OUTSOURCEDBIOMED |
| `OUTSOURCEDDRUG` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OUTSOURCEDDRUG |
| `HCARESCIPRODUCTS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARESCIPRODUCTS |
| `VETERINARY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=VETERINARY |
| `HCARESVCEDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARESVCEDIV |
| `HCAREOUTSOURCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREOUTSOURCE |
| `HCARECONTRACTMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARECONTRACTMFR |
| `HCARECONTRACTRESEARCH` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCARECONTRACTRESEARCH |
| `HCAREDEV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREDEV |
| `HCAREEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREEQUIP |
| `HCAREDIAGNOSTICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HCAREDIAGNOSTICS |
| `DIAGNOSTIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DIAGNOSTIC |
| `DRUGDELIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DRUGDELIV |
| `MEDDEVICESGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDDEVICESGEN |
| `SYSTEMSPECIFIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SYSTEMSPECIFIC |
| `MEDDEVICESDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDDEVICESDIV |
| `MEDDEVICESOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDDEVICESOTHER |
| `MEDSUPPLIES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDSUPPLIES |
| `MEDDEVICESSPECIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDDEVICESSPECIAL |


### Industrials

40 - Industrials

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `INDUSTRIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INDUSTRIAL |
| `INDMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INDMFR |
| `AERODEF` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AERODEF |
| `AEROSPACEEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AEROSPACEEQUIP |
| `DEF` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DEF |
| `AERODEFDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AERODEFDIV |
| `ELECTREQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTREQUIP |
| `COMMELECTRIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMELECTRIC |
| `ELECTREQUIPOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTREQUIPOTHER |
| `POWERGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWERGEN |
| `MACHINE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MACHINE |
| `CONTROLEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONTROLEQUIP |
| `AUTOMATIONEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOMATIONEQUIP |
| `MACHINEPARTS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MACHINEPARTS |
| `CONSTRUCTIONMACHINE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSTRUCTIONMACHINE |
| `MACHINEOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MACHINEOTHER |
| `TOOLS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TOOLS |
| `TRANSPORTEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRANSPORTEQUIP |
| `TRANSPORTEQUIPCML` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRANSPORTEQUIPCML |
| `TRANSPORTEQUIPGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRANSPORTEQUIPGEN |
| `INDSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INDSVCE |
| `TRAINTRUCK` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRAINTRUCK |
| `AIRWATER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AIRWATER |
| `TRAINTRUCKGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRAINTRUCKGEN |
| `TRAINTRUCKOP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TRAINTRUCKOP |
| `INTERMODAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INTERMODAL |
| `DELIVERY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DELIVERY |
| `EXPRESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EXPRESS |
| `DELIVERYGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DELIVERYGEN |
| `LOGISTICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LOGISTICS |
| `INDLDIST` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INDLDIST |
| `EQUIPDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EQUIPDISTRIB |
| `MATDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATDISTRIB |
| `INDLDIVDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INDLDIVDISTRIB |
| `BUILDINGMATDIST` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BUILDINGMATDIST |
| `FACIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FACIL |
| `INFCONSTRSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INFCONSTRSVCE |
| `CONTRACTINGSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONTRACTINGSVCE |
| `PASSENGERTRANS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PASSENGERTRANS |
| `AIRPASSENGER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AIRPASSENGER |
| `PASSENGEROTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PASSENGEROTHER |


### Non-Energy Materials

45 - Non-Energy Materials

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `MATERIALS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATERIALS |
| `CHEM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CHEM |
| `CHEMCOMMOD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CHEMCOMMOD |
| `ORGANICCHEM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ORGANICCHEM |
| `COMMODITYCHEM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMODITYCHEM |
| `CHEMMIX` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CHEMMIX |
| `CHEMSPECIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CHEMSPECIAL |
| `ADDITIVES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ADDITIVES |
| `ADHESIVE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ADHESIVE |
| `AGROCHEM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AGROCHEM |
| `SANITIZE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SANITIZE |
| `CHEMMFROTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CHEMMFROTHER |
| `POLYMER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POLYMER |
| `PLASTIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PLASTIC |
| `PLASTICOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PLASTICOTHER |
| `PLASTICMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PLASTICMFR |
| `MINING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MINING |
| `METAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=METAL |
| `METALPARTS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=METALPARTS |
| `METALOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=METALOTHER |
| `METALPRIMARY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=METALPRIMARY |
| `MINERAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MINERAL |
| `MIXMETALMINERAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MIXMETALMINERAL |
| `ORE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ORE |
| `OREBASE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OREBASE |
| `OREOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OREOTHER |
| `PRECIOUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRECIOUS |
| `MININGOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MININGOTHER |
| `OREMULTI` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OREMULTI |
| `ORENONMETAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ORENONMETAL |
| `MININGSTREAMING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MININGSTREAMING |
| `GASMININGDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GASMININGDIV |
| `MATCONSTR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATCONSTR |
| `ARCHITECTCOMPONENT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ARCHITECTCOMPONENT |
| `MATCONSTRGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATCONSTRGEN |
| `MATCONSTRHEAVY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATCONSTRHEAVY |
| `MFRPROD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MFRPROD |
| `WOODPAPER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WOODPAPER |
| `WOOD` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WOOD |
| `WOODPAPEROTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WOODPAPEROTHER |
| `PAPER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PAPER |
| `PACKAGING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PACKAGING |
| `PACKAGINGMETAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PACKAGINGMETAL |
| `PACKAGINGOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PACKAGINGOTHER |
| `PACKAGINGPAPER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PACKAGINGPAPER |
| `PACKAGINGPLASTIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PACKAGINGPLASTIC |
| `MATOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATOTHER |
| `TEXTILE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TEXTILE |
| `MATDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MATDIV |
| `COMPMAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPMAT |


### Technology

55 - Technology

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `TECH` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECH |
| `ELECTRONIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONIC |
| `COMPONENTS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPONENTS |
| `COMPONENTINTERCONNECT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPONENTINTERCONNECT |
| `COMPONENTMODULE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPONENTMODULE |
| `COMPONENTOPTOELECTRONIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPONENTOPTOELECTRONIC |
| `COMPONENTPASSIVE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPONENTPASSIVE |
| `COMPONENTDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPONENTDIV |
| `ELECTRONICEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONICEQUIP |
| `CONTRACTELECMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONTRACTELECMFR |
| `ELECTRONICEQUIPDIV` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONICEQUIPDIV |
| `INTERCONNECTMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INTERCONNECTMFR |
| `SEMIMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIMFR |
| `SEMIANALOG` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIANALOG |
| `SEMIDISCRETE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIDISCRETE |
| `SEMIGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIGEN |
| `SEMIMEMORY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIMEMORY |
| `SEMIPROCESSOR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIPROCESSOR |
| `SEMIASIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIASIC |
| `SEMISPECIAL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMISPECIAL |
| `ELECTRONICMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ELECTRONICMFR |
| `SEMIEQUIPSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIEQUIPSVCE |
| `SEMIMFREQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIMFREQUIP |
| `SEMIMFRSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SEMIMFRSVCE |
| `HW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HW |
| `COMMERCIALELECTRONICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMERCIALELECTRONICS |
| `COMMERCEEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMERCEEQUIP |
| `SECURITYEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SECURITYEQUIP |
| `FINELECTRONICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FINELECTRONICS |
| `MEDIAELECTRONICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEDIAELECTRONICS |
| `OFFICEEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OFFICEEQUIP |
| `COMMERCIALELECTRONICSMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMERCIALELECTRONICSMFR |
| `PRINTINGELECTRONICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRINTINGELECTRONICS |
| `MEASURE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MEASURE |
| `COMMEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMEQUIP |
| `BIZCOMM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=BIZCOMM |
| `CABLEEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CABLEEQUIP |
| `LANEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LANEQUIP |
| `COMMEQUIPOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMMEQUIPOTHER |
| `SATELLITEEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SATELLITEEQUIP |
| `WANEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WANEQUIP |
| `WIRELESSINFEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WIRELESSINFEQUIP |
| `WIRELESSMOBILEEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WIRELESSMOBILEEQUIP |
| `COMPUTER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPUTER |
| `PERIPHERALS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PERIPHERALS |
| `COMPUTERSYSTEMS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPUTERSYSTEMS |
| `DATASTORAGEHW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DATASTORAGEHW |
| `COMPUTERGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=COMPUTERGEN |
| `HWCOMPONENTS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HWCOMPONENTS |
| `CONSUMERELECTRONICS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERELECTRONICS |
| `AUDIOMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUDIOMFR |
| `AUTOELECTRONICSMFR` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AUTOELECTRONICSMFR |
| `CONSUMERELECTRONICSACCESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERELECTRONICSACCESS |
| `VIDEOEQUIP` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=VIDEOEQUIP |
| `GAMING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GAMING |
| `CONSUMERELECTRONICSGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERELECTRONICSGEN |
| `PHOTO` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PHOTO |
| `VIRTUALREALITY` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=VIRTUALREALITY |
| `WEARABLETECH` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WEARABLETECH |
| `TECHDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHDISTRIB |
| `HWDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HWDISTRIB |
| `TECHDISTRIBOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHDISTRIBOTHER |
| `SOFTWDISTRIB.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWDISTRIB.XX1 |
| `SOFTWTECH` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWTECH |
| `INTERNET` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INTERNET |
| `CONSUMERDATA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CONSUMERDATA |
| `INTERNETMEDIA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INTERNETMEDIA |
| `INTERNETHOSTING` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=INTERNETHOSTING |
| `TECHSUPPORT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHSUPPORT |
| `PRODATA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PRODATA |
| `WEBDATA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WEBDATA |
| `SOFTW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTW |
| `SOFTWDESIGN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWDESIGN |
| `SOFTWENTERPRISE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWENTERPRISE |
| `SOFTWGAMES` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWGAMES |
| `SOFTWHOMEOFFICE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWHOMEOFFICE |
| `SOFTWINDSPECIFIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWINDSPECIFIC |
| `SOFTWINF` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWINF |
| `SOFTWGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWGEN |
| `TECHCONSULTSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHCONSULTSVCE |
| `TECHCONSULTGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHCONSULTGEN |
| `TECHINDSPECIFIC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHINDSPECIFIC |
| `TECHCONSULT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHCONSULT |
| `TECHCONSULTNETW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TECHCONSULTNETW |
| `SOFTWDISTRIB` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SOFTWDISTRIB |


### Telecommunications

60 - Telecommunications

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `TELECOM` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOM |
| `TELECOMSS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMSS |
| `TELECOMGEN` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMGEN |
| `TELECOMOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMOTHER |
| `TELECOMINTL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMINTL |
| `SATELLITESVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SATELLITESVCE |
| `SATELLITEINTL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SATELLITEINTL |
| `TELECOMUSOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMUSOTHER |
| `TELECOMCARRIER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMCARRIER |
| `TELECOMSOFTW` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMSOFTW |
| `TELECOMSOFTWSVCE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMSOFTWSVCE |
| `SATELLITEUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SATELLITEUS |
| `TELECOMAMEREXUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMAMEREXUS |
| `TELECOMASIA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMASIA |
| `TELECOMEUROPE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMEUROPE |
| `TELECOMMIDEAST` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMMIDEAST |
| `TELECOMWIRE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TELECOMWIRE |
| `WIRELESS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WIRELESS |
| `WIRELINE` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WIRELINE |


### Utilities

65 - Utilities

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `UTIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UTIL |
| `UTILSS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UTILSS |
| `ENERGYUTIL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ENERGYUTIL |
| `UTILELEC` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UTILELEC |
| `GAS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GAS |
| `UTILELECGAS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UTILELECGAS |
| `POWER.XX1` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWER.XX1 |
| `POWERMULTINAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWERMULTINAT |
| `POWERUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWERUS |
| `POWERAMEREXUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWERAMEREXUS |
| `POWERASIA` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWERASIA |
| `POWERINTLOTHER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=POWERINTLOTHER |
| `XMSNUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=XMSNUS |
| `XMSNMULTINAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=XMSNMULTINAT |
| `WATER` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WATER |
| `WATERINTL` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WATERINTL |
| `WATERUS` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WATERUS |
| `WATERMULTINAT` | rcode |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WATERMULTINAT |


## Math

Mathematical functions, including logs, absolute values and random numbers.

### Absolute value

Evaluates to the absolute value of expr

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Abs()` | expr |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Abs |


### Base 10 log

Returns the base-10 log of val

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Log10()` | val |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Log10 |


### Calculate Percent Growth

Calculates percent as 100 * ((a - b) / abs(b))

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `%()` | a , b |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=% |


### Constrains to a max and/or a min

Constrains a value to a maximum or a minimum. When returnNA is set to TRUE the function returns NA if expression exceeds the minimum or maximum.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Bound()` | expression, min, max [, returnNA] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Bound |
| `LBound()` | expression, min [, returnNA] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LBound |
| `UBound()` | expression, max [, returnNA] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=UBound |


### Growth Rate Annualized

Calculates the annual growth rate as 100 * (pow(1 + (a - b) / abs(b), 1/years) -1). When years is 1 or unspecified, calculates growth rate as 100 * ((a - b) / abs(b)).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Gr%()` | a , b [, years] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Gr% |


### Modulus Operator

Modulus operation that returns the remainder of val/modulo

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Mod()` | val, modulo |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Mod |


### Natural Log

Returns the natural log of val

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LN()` | val |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LN |


### Negate

Changes the sign of the expression.

Ex:	Negate(5) = -5

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Negate()` | expr |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Negate |


### Power

Returns a number raised to a power

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pow()` | number , power |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pow |


### Random Number

Random: Returns a random number uniformly distributed between 0 and 1

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Random` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Random |


### Replace NA Number (Not Available)

Returns the value of expr1 if it's not NA, otherwise it returns expr2

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IsNA()` | expr1, expr2 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IsNA |


### Replace Negative Number

Returns the value of expr1 if it's not negative, otherwise it returns expr2

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IsNeg()` | expr1, expr2 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IsNeg |


### Replace Negative or NA Number

Returns the value of expr1 if it's not negative and not NA, otherwise it returns expr2

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IsNegOrNA()` | expr1, expr2 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IsNegOrNA |


### Replace Zero Number

Returns the value of expr1 if it's not zero, otherwise it returns expr2

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IsZero()` | expr1, expr2 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IsZero |


### Truncate number

Rounds val toward zero

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Trunc()` | val |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Trunc |


## Regression

Regression functions and statistics

### Linear Regression of XY Values

Operates a regression on a set of XY values.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LinRegXYVals()` | x0, y0, x0, y1, ..., x50, y50 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LinRegXYVals |


### Linear Regressions of Values

Operates a regression on a set of Y values.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LinRegVals()` | y0, y1, ..., y50 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LinRegVals |


## Regression Stats

Statistics for a previously computed regression.

### Coefficient of Determination

Returns the R² for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `R2` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=R2 |


### Correlation Coefficient

Returns the R for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `R` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=R |


### Regression Estimate

Returns the Y estimate for a previously computed XY regression.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EstimateXY()` | X |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EstimateXY |
| `EstimateY()` | offset |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EstimateY |


### Regression Growth

Returns the growth for a previously computed time series regression. The period parameter can be used to annualize the growth

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RegGr%()` | [period=1] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RegGr% |


### Regression Samples (Observations)

Returns the number of samples for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Samples` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Samples |


### Regression Surprise

Returns the surprise of the estimated Y vs actual for a previously computed regression. Note that offset depends on the regression. Please see the Full Description

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SurpriseY()` | offset |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SurpriseY |


### Slope Confidence %

Confidence is defined as 100 * (1-SlopePVal) for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SlopeConf%` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SlopeConf% |


### Slope of the regression

Returns the Slope for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Slope` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Slope |


### Slope p-value

Returns the P-value of the slope for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SlopePVal` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SlopePVal |


### Slope Standard Error

Returns the Slope Standard Error for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SlopeSE` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SlopeSE |


### Slope t-statistic

Returns the t Stat of the slope for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SlopeTStat` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SlopeTStat |


### Standard Error of the Y Estimate (Sy.x)

Returns the SE of the Y estimate for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SE` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SE |


### Y Intercept

Returns the Y-Intercept for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Intercept` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Intercept |


### Y Intercept Standard Error

Returns the Y-Intercept Standard Error for a previously computed regression

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `InterceptSE` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=InterceptSE |


## Set

Functions that perform mathematical functions on finite data sets.

### Average of a set of values

Returns the average value in list. Up to 20 parameters are allowed and NAs are discarded

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Avg()` | x1, x2[, .., x20] |  |  |


### Calculate the max/min in a set

Returns the largest value in list. Up to 20 parameters are allowed and NAs are discarded

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Max()` | x1, x2[, .., x20] |  |  |
| `Min()` | x1, x2[, .., x20] |  |  |


### Check if an expression is in a set

Returns TRUE (1) if 'expression' is found in the list of parameters. For example, to screen for stocks in one of three industries you can write:

InSet(Industry,ADVERT,CASINO,HOTELS)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `InSet()` | expression, x1[, ..x20]] |  |  |


### Count higher/lower values in a set

Returns the number of times xi > xi+1. For example to find companies that price increased at least 2 out of 3 days enter:

Higher(Close(0),Close(1),Close(2),Close(3))>=2

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Higher()` | x1, x2[, .., x20] |  |  |
| `Lower()` | x1, x2[, .., x20] |  |  |


### Median of a set of values

Returns the median value in list. Up to 20 parameters are allowed and NAs are discarded

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Median()` | x1, x2[, .., x20] |  |  |


### Standard deviation of a set of values

Returns the Relative Standard Deviation (SD divided by the mean) of the parameters.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RelStdDev()` | x1, x2[, .., x20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RelStdDev |
| `StdDev()` | x1, x2[, .., x20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=StdDev |


## Utility

Functions that perform logical evaluations, provide timing information or setting variables.

### As-Of Date

Returns the current trading day as a number in the following format YYYYMMDD

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `AsOfDate` |  |  |  |


### Date

Returns the number of bars since the given date. Date is a number in this format YYYYMMDD.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `BarsSince()` | date |  |  |
| `DaysDiff()` | from, to |  |  |
| `DaysSince()` | date |  |  |
| `PrevBarDaysAgo` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PrevBarDaysAgo |
| `Year` |  |  |  |
| `Month` |  |  |  |
| `MonthDay` |  |  |  |
| `WeekDay` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WeekDay |


### Foreign exchange rate

FXRate gives you the foreign exchange rate used to convert the currency of the stock (or ETF) to the currency in the screen/ranking system/simulation.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FXRate` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FXRate |


### Holiday

Returns TRUE (1) if weekday is a holiday, FALSE (0) otherwise. Use negative values to check for upcoming holidays. (Note: It doesn't support checking future dates.)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Holiday()` | weekday | Weekday |  |


### Trading day in month

Returns 1 (TRUE) if the as-of date is the nth trading day of the month. Negative offsets are evaluated relative to end of month (e.g. -2 is the second-to-last trading day of the month). In multi-country regions, country code must be specified. MonthBars is intended to be used in strategies, not screens or ranking systems.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `MonthBars()` | bars[, "cid"] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MonthBars |


### Set Variable

Sets the variable @myvar to the expression and returns TRUE. You can use the variable in subsequent rules.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SetVar()` | @myvar, expression |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SetVar |


### Between

Returns TRUE (1) if value is between min and max (inclusive), FALSE(0) otherwise

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Between()` | value, min, max |  |  |


### Evaluate condition and return one of two values

Executes expr1 if the condition evaluates to non-zero, or expr2 otherwise. See Full Description for examples of the many uses of Eval()

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Eval()` | condition, expr1, expr2 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Eval |


### GetSeries

Use this function in functions that have a 'series' parameter. You can use any stock, ETF, index ticker, or a custom series. If you use a stock ticker, your function may stop working if the ticker changes.

See Full Description for the list of index tickers and examples.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `GetSeries()` | "ticker/series" |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GetSeries |


## Constants

Identification codes of data points and series accessible across many functions.

### Dividend Date

Announce date

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnnDate` | div_dt |  |  |
| `#ExDate` | div_dt |  |  |
| `#PayDate` | div_dt |  |  |


### Dividend Type

Any kind of dividend

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AllDiv` | div_type |  |  |
| `#Regular` | div_type |  |  |
| `#Special` | div_type |  |  |


### Formula Functions Include NA Parameter

Exclude NA values

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#ExclNA` | incl_na |  |  |
| `#InclNA` | incl_na |  |  |
| `#NANeutral` | incl_na |  |  |


### Numerical Constants

Returns 62, the approximate number of bars in 3 months

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Month3` | period_bar | 3 Months |  |
| `#Month6` | period_bar | 6 Months |  |
| `NA` |  |  |  |
| `TRUE` | zeroIsNA, excl_zero, ex_zero, ex_adrs, cnt_flag |  |  |
| `FALSE` | zeroIsNA, excl_zero, ex_zero, ex_adrs, cnt_flag |  |  |
| `#Year` | period_bar | 1 Year |  |
| `#Year2` | period_bar | 2 Years |  |
| `#Month` | period_bar | 1 Month |  |
| `#Week` | period_bar | 1 Week |  |


### Streak

Increasing values streak

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Increasing` | streak |  |  |
| `#NotIncreasing` | streak |  |  |
| `#NotPositive` | streak |  |  |
| `#Positive` | streak |  |  |


### Actual Item (actual_item)

Capital Expenditure

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#CAPX` | actual_item |  |  |
| `#EBIT` | actual_item |  |  |
| `#EBITDA` | actual_item |  |  |
| `#EPS` | actual_item |  |  |
| `#EPS_GAAP` | actual_item |  |  |
| `#FCF` | actual_item |  |  |
| `#FFO` | actual_item |  |  |
| `#NET` | actual_item |  |  |
| `#PTI` | actual_item |  |  |
| `#SALES` | actual_item |  |  |
| `#SHS_REPURCH` | actual_item |  |  |
| `#SOE` | actual_item |  |  |


### Consensus Estimate (cons_item)

CapEx Next Twelve Months

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#CAPXNTM` | cons_item |  |  |
| `#CAPXQ` | cons_item |  |  |
| `#CAPXY` | cons_item |  |  |
| `#EBITDANTM` | cons_item |  |  |
| `#EBITDAQ` | cons_item |  |  |
| `#EBITDAY` | cons_item |  |  |
| `#EPSNTM` | cons_item |  |  |
| `#EPSQ` | cons_item |  |  |
| `#EPSY` | cons_item |  |  |
| `#FCFNTM` | cons_item |  |  |
| `#FCFQ` | cons_item |  |  |
| `#FCFY` | cons_item |  |  |
| `#LTG` | cons_item |  |  |
| `#PT` | cons_item |  |  |
| `#SALENTM` | cons_item |  |  |
| `#SALEQ` | cons_item |  |  |
| `#SALEY` | cons_item |  |  |


### Consensus Recommendation (rec_stat)

Average of all Recommendation

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AvgRec` | rec_stat |  |  |
| `#BuyCnt` | rec_stat |  |  |
| `#HoldCnt` | rec_stat |  |  |
| `#OverCnt` | rec_stat |  |  |
| `#RecCnt` | rec_stat |  |  |
| `#SellCnt` | rec_stat |  |  |
| `#UnderCnt` | rec_stat |  |  |


### Corporate Actions (ca_retvalue)

Number of actions that matched or 0

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#ACTIONCNT` | ca_retvalue |  |  |
| `#ACTIONTYPE` | ca_retvalue |  |  |
| `#ANNCEDAYS` | ca_retvalue |  |  |
| `#CLOSEDAYS` | ca_retvalue |  |  |
| `#TRUEFALSE` | ca_retvalue |  |  |


### Corporate Actions (ca_status)

Approval

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#APPROVAL` | ca_status |  |  |
| `#COMPLETION` | ca_status |  |  |
| `#MEETING` | ca_status |  |  |
| `#OTHER` | ca_status |  |  |
| `#REJECTION` | ca_status |  |  |
| `#STATUSANY` | ca_status |  |  |
| `#STATUSFAIL` | ca_status |  |  |
| `#STATUSNA` | ca_status |  |  |
| `#STATUSOK` | ca_status |  |  |
| `#TERMINATION` | ca_status |  |  |


### Corporate Actions (ca_type)

Buy Offer

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#BUYOFF` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#BUYOFF |
| `#LIQUIDATION` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#LIQUIDATION |
| `#MANDA` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#MANDA |
| `#MANDAEXSPIN` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#MANDAEXSPIN |
| `#MERGER` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#MERGER |
| `#MERGEREL` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#MERGEREL |
| `#NEWOFFER` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#NEWOFFER |
| `#SPINOFF` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPINOFF |
| `#SPLIT` | ca_type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=#SPLIT |


### Filing Period

Annual

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ANN` | type |  |  |
| `QTR` | type |  |  |
| `TTM` | type |  |  |


### N/A during preliminaries

Fallback to previous period

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FALLBACK` | NAHandling |  |  |
| `KEEPNA` | NAHandling |  |  |
| `ZERONA` | NAHandling |  |  |


### Country IDs

Albania

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ALB` | cid | Albania |  |
| `DZA` | cid | Algeria |  |
| `AND` | cid | Andorra |  |
| `ATG` | cid | Antigua And Barbuda |  |
| `ARG` | cid | Argentina |  |
| `ARM` | cid | Armenia |  |
| `AUS` | cid | Australia |  |
| `AUT` | cid | Austria |  |
| `BHS` | cid | Bahamas |  |
| `BHR` | cid | Bahrain |  |
| `BGD` | cid | Bangladesh |  |
| `BRB` | cid | Barbados |  |
| `BLR` | cid | Belarus |  |
| `BEL` | cid | Belgium |  |
| `BLZ` | cid | Belize |  |
| `BMU` | cid | Bermuda |  |
| `BOL` | cid | Bolivia |  |
| `BIH` | cid | Bosnia and Herzegovina |  |
| `BWA` | cid | Botswana |  |
| `BRA` | cid | Brazil |  |
| `BGR` | cid | Bulgaria |  |
| `KHM` | cid | Cambodia |  |
| `CAN` | cid | Canada |  |
| `CYM` | cid | Cayman Islands |  |
| `CHL` | cid | Chile |  |
| `CHN` | cid | China |  |
| `COL` | cid | Colombia |  |
| `CRI` | cid | Costa Rica |  |
| `CIV` | cid | Cote d'Ivoire |  |
| `HRV` | cid | Croatia (hrvatska) |  |
| `CUW` | cid | Curacao |  |
| `CYP` | cid | Cyprus |  |
| `CZE` | cid | Czech Republic |  |
| `DNK` | cid | Denmark |  |
| `DOM` | cid | Dominican Republic |  |
| `ECU` | cid | Ecuador |  |
| `EGY` | cid | Egypt |  |
| `EST` | cid | Estonia |  |
| `FRO` | cid | Faroe Islands |  |
| `FIN` | cid | Finland |  |
| `FRA` | cid | France |  |
| `DEU` | cid | Germany |  |
| `GHA` | cid | Ghana |  |
| `GIB` | cid | Gibraltar |  |
| `GRC` | cid | Greece |  |
| `GLP` | cid | Guadeloupe |  |
| `GGY` | cid | Guernsey |  |
| `VAT` | cid | Holy See |  |
| `HKG` | cid | Hong Kong |  |
| `HUN` | cid | Hungary |  |
| `ISL` | cid | Iceland |  |
| `IND` | cid | India |  |
| `IDN` | cid | Indonesia |  |
| `IRN` | cid | Iran |  |
| `IRQ` | cid | Iraq |  |
| `IRL` | cid | Ireland |  |
| `IMN` | cid | Isle of Man |  |
| `ISR` | cid | Israel |  |
| `ITA` | cid | Italy |  |
| `JAM` | cid | Jamaica |  |
| `JPN` | cid | Japan |  |
| `JEY` | cid | Jersey |  |
| `JOR` | cid | Jordan |  |
| `KAZ` | cid | Kazakhstan |  |
| `KEN` | cid | Kenya |  |
| `KWT` | cid | Kuwait |  |
| `LAO` | cid | Laos |  |
| `LVA` | cid | Latvia |  |
| `LBN` | cid | Lebanon |  |
| `LIE` | cid | Liechtenstein |  |
| `LTU` | cid | Lithuania |  |
| `LUX` | cid | Luxembourg |  |
| `MKD` | cid | Macedonia |  |
| `MWI` | cid | Malawi |  |
| `MYS` | cid | Malaysia |  |
| `MLT` | cid | Malta |  |
| `MUS` | cid | Mauritius |  |
| `MYT` | cid | Mayotte |  |
| `MEX` | cid | Mexico |  |
| `MDA` | cid | Moldova |  |
| `MCO` | cid | Monaco |  |
| `MNG` | cid | Mongolia |  |
| `MNE` | cid | Montenegro |  |
| `MSR` | cid | Montserrat |  |
| `MAR` | cid | Morocco |  |
| `NAM` | cid | Namibia |  |
| `NPL` | cid | Nepal |  |
| `NLD` | cid | Netherlands |  |
| `NZL` | cid | New Zealand |  |
| `NGA` | cid | Nigeria |  |
| `NOR` | cid | Norway |  |
| `OMN` | cid | Oman |  |
| `PAK` | cid | Pakistan |  |
| `PAN` | cid | Panama |  |
| `PNG` | cid | Papua New Guinea |  |
| `PER` | cid | Peru |  |
| `PHL` | cid | Philippines |  |
| `POL` | cid | Poland |  |
| `PRT` | cid | Portugal |  |
| `QAT` | cid | Qatar |  |
| `ROU` | cid | Romania |  |
| `RUS` | cid | Russia |  |
| `RWA` | cid | Rwanda |  |
| `VCT` | cid | Saint Vincent and Grenadines |  |
| `SMR` | cid | San Marino |  |
| `SAU` | cid | Saudi Arabia |  |
| `SRB` | cid | Serbia |  |
| `SGP` | cid | Singapore |  |
| `SVK` | cid | Slovakia |  |
| `SVN` | cid | Slovenia |  |
| `ZAF` | cid | South Africa |  |
| `KOR` | cid | South Korea |  |
| `ESP` | cid | Spain |  |
| `LKA` | cid | Sri Lanka |  |
| `SPM` | cid | St. Pierre and Miquelon |  |
| `SJM` | cid | Svalbard and Jan Mayen |  |
| `SWZ` | cid | Swaziland |  |
| `SWE` | cid | Sweden |  |
| `CHE` | cid | Switzerland |  |
| `SYR` | cid | Syria |  |
| `TWN` | cid | Taiwan |  |
| `TZA` | cid | Tanzania United Republic Of |  |
| `THA` | cid | Thailand |  |
| `TTO` | cid | Trinidad and Tobago |  |
| `TUN` | cid | Tunisia |  |
| `TUR` | cid | Turkey |  |
| `TCA` | cid | Turks and Caicos Islands |  |
| `UGA` | cid | Uganda |  |
| `UKR` | cid | Ukraine |  |
| `ARE` | cid | United Arab Emirates |  |
| `GBR` | cid | United Kingdom |  |
| `USA` | cid | United States |  |
| `URY` | cid | Uruguay |  |
| `VEN` | cid | Venezuela |  |
| `VNM` | cid | Viet Nam |  |
| `VGB` | cid | Virgin Islands (British) |  |
| `VIR` | cid | Virgin Islands (u.s.) |  |
| `ZMB` | cid | Zambia |  |
| `ZWE` | cid | Zimbabwe |  |


### Universe IDs

All Fundamentals

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ALLFUND` | uname |  |  |
| `ALLSTOCKS` | uname |  |  |


### Universe IDs - Major USA

Dow Jones Industrial Average

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `DJIA` | uname |  |  |
| `NOOTC` | uname |  |  |
| `Prussell1000` | uname |  |  |
| `Prussell2000` | uname |  |  |
| `Prussell3000` | uname |  |  |
| `SP1500` | uname |  |  |
| `SP500` | uname |  |  |


### Universe IDs - Other USA

American Depositary Receipt

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `$ADR` | uname |  |  |
| `LargeCap` | uname |  |  |
| `MasterLP` | uname |  |  |
| `MicroCap` | uname |  |  |
| `MidCap` | uname |  |  |
| `NASD` | uname |  |  |
| `NASDAQ100` | uname |  |  |
| `NYSE` | uname |  |  |
| `NYSEMKT` | uname |  |  |
| `OTC` | uname |  |  |
| `SmallCap` | uname |  |  |
| `SP400` | uname |  |  |
| `SP600` | uname |  |  |


### Formula Functions Sort Parameter

Sort ascending

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#ASC` | sort |  |  |
| `#DESC` | sort |  |  |


### Formula Functions Sort Style Parameter

Neutral

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Neutral` | sort_style |  |  |
| `#Top` | sort_style |  |  |


### Formula Functions Scope Parameter

Operate within selected universe

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#All` | scope |  |  |
| `#Industry` | scope |  |  |
| `#Sector` | scope |  |  |
| `#SubIndustry` | scope |  |  |
| `#SubSector` | scope |  |  |
| `#SP500` | scope |  |  |
| `#Previous` | scope |  |  |
| `#GroupVar` | scope |  |  |
| `#Family` | scope |  |  |
| `#AssetClass` | scope |  |  |
| `#Region` | scope |  |  |
| `#Country` | scope |  |  |
| `#Method` | scope |  |  |
| `#Style` | scope |  |  |
| `#Size` | scope |  |  |
| `#ETFSector` | scope |  |  |


### Aggregate Method Parameter

Average the values (default, recommended)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Avg` | method |  |  |
| `#CapAvg` | method |  |  |


### Aggregate Outlier Handler Parameter

Excludes outliers from the aggregation (default)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#Exclude` | outlier_handl |  |  |
| `#Winsor` | outlier_handl |  |  |


## Operators

Logical and mathematical operators in common use across the site.

### Boolean operators

Expr1 And Expr2: Evaluates to 1 when both Expr1 and Expr2 are non zero.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `And` |  |  |  |
| `Or` |  |  |  |


### Logical operators

Logical Operators:
=	Equals
!=	Not Equals

!	Negate
>	Greater
<	Less
>=	Greater or equal
<=	Less or equal

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `= != ! < > >= <=` |  |  |  |


### Math operators

Mathematical Operators:
+	Sum
-	Subtract
*	Multiply
/	Divide
^	Power (x^y is x raised to the power of y)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `+ - * / ^` |  |  |  |


### Precedence operators

Precedence Operators:
Use parentheses to change the order operations are calculated. For example:

( 10 + 5 ) / 5 = 3
10 + 5 / 5 = 11

When in doubt, always use parentheses.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `( )` |  |  |  |


### Rule comments

Allows you to add comments to a rule. Everything after // is ignored. Example:

Close(0)>5 // this is a comment

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `//` |  |  |  |


### Show/Set Variable operator

Following rule "@myvar:expression" sets a variable @myvar to expression, returns the expression, and displays @myvar in the screen report

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `:` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=: |

