# P123 API Reference (p123api Python Wrapper)

## Table of Contents
1. [Setup & Authentication](#setup)
2. [Data Retrieval](#data-retrieval)
3. [Universe](#universe)
4. [Rank](#rank)
5. [Screen](#screen)
6. [Strategy](#strategy)
7. [Data Series & Stock Factors](#data-series)
8. [AI Factor](#ai-factor)
9. [API Credits & Limits](#credits)

---

## Setup & Authentication <a name="setup"></a>

```bash
pip install --upgrade p123api
```

```python
import p123api

client = p123api.Client(api_id='YOUR_API_ID', api_key='YOUR_API_KEY')

# Or as context manager
with p123api.Client(api_id='YOUR_API_ID', api_key='YOUR_API_KEY') as client:
    result = client.screen_run({...})
```

API keys: Account Settings → DataMiner & API → Create Key. Requires Research subscription.

---

## Data Retrieval <a name="data-retrieval"></a>

### data() — Retrieve point-in-time data for specific tickers (1 credit per 100K data points)

```python
client.data({
    # Identifier (choose one): tickers, FIGI, p123Uids, CIKs, gvkeys (Compustat only)
    'tickers': ['AAPL', 'MSFT', 'GOOG'],
    'formulas': ['PEExclXorTTM', 'ROE%TTM', 'MktCap', 'Close(0)/Close(252)-1'],
    'startDt': '2020-01-01',
    'endDt': '2025-01-01',
    # Optional
    'frequency': 'Every 4 Weeks',  # Every Week, Every N Weeks (2,3,4,6,8,13,26,52)
    'pitMethod': 'Complete',       # Complete | Prelim
    'precision': 4,                # 2 | 3 | 4
    'currency': 'USD',
    'includeNames': True,
    'region': 'United States',     # Canada, North America, Europe, North Atlantic
    'ignoreErrors': True           # ignore invalid tickers
}, True)  # True = Pandas DataFrame, False = JSON
```

**Note**: Requires data license from FactSet or Compustat for full access. Without license, only IBM, MSFT, INTC with 5 years history.

### data_prices() — EOD prices (1 credit per call)

```python
client.data_prices(
    identifier='AAPL',       # string ticker or int P123 ID
    start='2024-01-01',
    end='2025-01-01',        # or None
    to_pandas=True
)
```

### data_universe() — Point-in-time data for a universe (1 credit per 100K data points)

```python
client.data_universe({
    'universe': 'SP500',           # P123 universe name or custom
    'asOfDts': ['2025-03-08', '2025-03-01'],  # use weekend dates
    'formulas': ['PEExclXorTTM', 'ROE%TTM', 'Close(0)/Close(5)'],
    'names': ['PE', 'ROE', '1wk%'],  # optional, must match formula count
    # Optional
    'pitMethod': 'Complete',
    'precision': 4,                 # None for max precision
    'type': 'stock',                # stock | etf
    'includeNames': True,
    'currency': 'USD',
    'figi': 'Country Composite',    # Country Composite | Share Class
    # Normalization (optional)
    'preproc': {
        'scaling': 'rank',          # minmax | rank | normal
        'scope': 'date',            # dataset | date
        'trimPct': 5.0,
        'outliers': True,           # clip outliers
        'naFill': False,            # fill NAs with middle values
        'outlierLimit': 5,          # for normal scaling
        'excludedFormulas': ['Close(0)/Close(5)'],  # exclude from normalization
        'mlTrainingEnd': '2020-01-01'  # end date when scope=dataset
    }
}, to_pandas=True)
```

**Common Universes**:
- US: `SP500`, `SP400`, `SP600`, `SP1500`, `DJIA`, `NASDAQ100`, `Prussell1000`/`2000`/`3000`, `ALLFUND`, `PRIMARYUSA`, `ALLSTOCKS`, `LargeCap`, `MidCap`, `SmallCap`, `MicroCap`, `NanoCap`
- Canada: `ALLFUNDCAN`, `PRIMARYCAN`, `ALLSTOCKSCAN`, `SPTSX`, `SPTSX60`, `TSX`, `TSXV`
- Europe: `ALLFUNDEUR`, `PRIMARYEUR`, `EU200L`, `EU200M`, `EU200S`, `EU600`
- Multi-region: `PRIMARYNOAM`, `PRIMARYNOAT`, `TRADENOAM`, `TRADENOAT`, `TRADEEUR`

See `references/macros-constants.md` for the complete list with descriptions.

---

## Universe <a name="universe"></a>

### universe_update() — Create/update the ApiUniverse

```python
client.universe_update({
    'rules': [
        'MktCap > 500',
        'AvgDailyTot(63) > 200',
        'Close(0) > 5'
    ],
    'type': 'stock',
    'currency': 'USD',
    'startingUniverse': 'Prussell3000'  # optional base universe
})
```

Then use `'universe': 'ApiUniverse'` in other API calls.

---

## Rank <a name="rank"></a>

### rank_ranks() — Retrieve ranks for a universe (1 per 100K data points, min 2)

```python
client.rank_ranks({
    'rankingSystem': 'My Ranking System',  # name or ID
    'asOfDt': '2025-03-08',
    'universe': 'SP500',
    # Optional
    'pitMethod': 'Complete',
    'precision': 2,
    'rankingMethod': 2,                 # 2=NAs Negative, 4=NAs Neutral
    'tickers': 'IBM,MSFT',             # filter specific stocks
    'includeNames': True,
    'includeNaCnt': False,
    'includeFinalStmt': False,
    'nodeDetails': 'composite',         # composite | factor
    'additionalData': ['Close(0)', 'MktCap', 'ZScore(`Pr2SalesQ`,#All)'],
    'currency': 'USD'
}, True)
```

### rank_perf() — Bucket performance test (3 credits)

```python
client.rank_perf({
    'rankingSystem': 'My Ranking System',
    'startDt': '2010-01-01',
    # Optional
    'endDt': '2025-01-01',
    'universe': 'Prussell3000',
    'numBuckets': 10,
    'rebalFreq': 'Every 4 Weeks',
    'slippage': 0.25,
    'benchmark': 'SPY',
    'minPrice': 3,
    'minLiquidity': 5000,
    'outputType': 'ann',        # ann (annualized) | perf (cumulative)
    'transType': 'Long',        # Long | Short
    'rankingMethod': 2,
    'maxNAs': 999,
    'maxReturn': 200
})
```

### rank_update() — Update ApiRankingSystem (1 credit)

```python
client.rank_update({
    'nodes': '''<RankingSystem RankType="Higher">
        <Composite Name="Value" Weight="50" RankType="Higher">
            <StockFactor Weight="100" RankType="Lower" Scope="Universe">
                <Factor>PEExclXorTTM</Factor>
            </StockFactor>
        </Composite>
        <Composite Name="Momentum" Weight="50" RankType="Higher">
            <StockFormula Weight="100" RankType="Higher" Name="12-1M Mom" Description="" Scope="Universe">
                <Formula>Ret%Chg(252, 21)</Formula>
            </StockFormula>
        </Composite>
    </RankingSystem>''',
    'type': 'stock',
    'rankingMethod': 2,
    'id': 12345          # optional; omit to use/create ApiRankingSystem
})
```

---

## Screen <a name="screen"></a>

### screen_run() — Run a screen (2 credits)

```python
# Inline screen definition
client.screen_run({
    'screen': {
        'type': 'stock',
        'universe': 'SP500',
        'maxNumHoldings': 25,    # 0 for all
        'method': 'long',        # long | short | long/short | hedged
        'benchmark': 'SPY',
        'currency': 'USD',
        # Ranking (choose one form):
        'ranking': 'My Ranking System',      # by name
        'ranking': 12345,                     # by ID
        'ranking': {'formula': 'PEExclXorTTM', 'lowerIsBetter': True},  # inline formula
        # Rules
        'rules': [
            {'formula': 'MktCap > 1000'},
            {'formula': 'ROE%TTM > 10'},
            {'formula': 'Close(0) > SMA(200,0)'}
        ]
    },
    'asOfDt': '2025-03-08',
    'pitMethod': 'Complete',
    'precision': 2
}, True)

# Run existing screen by ID
client.screen_run({'screen': 12345}, True)
```

**Note on rule `type` field**: For `method: 'long'` (long-only) screens, rules must **not** include a `type` field — the API rejects it with `"Rule type parameter should not be present"`. The per-rule `type` field (`'long'`, `'short'`, or `'common'`) is only valid for `'long/short'` and `'hedged'` screens, where it specifies which side of the book a rule applies to.

### screen_backtest() — Backtest a screen (5 credits)

```python
client.screen_backtest({
    'screen': {
        'type': 'stock',
        'universe': 'Prussell3000',
        'maxNumHoldings': 25,
        'method': 'long',
        'benchmark': 'SPY',
        'ranking': {'formula': 'PEExclXorTTM', 'lowerIsBetter': True},
        'rules': [
            {'formula': 'MktCap > 500', 'type': 'long'},
            {'formula': 'Close(0) > 5', 'type': 'long'}
        ]
    },
    'startDt': '2010-01-01',
    # Optional
    'endDt': '2025-01-01',
    'transPrice': 1,             # 1=Open, 3=Avg Hi/Low, 4=Close
    'maxPosPct': 0,
    'slippage': 0.25,
    'longWeight': 100,
    'shortWeight': 100,
    'rankTolerance': 0,
    'carryCost': 0,
    'rebalFreq': 'Every 4 Weeks',
    'riskStatsPeriod': 'Monthly'  # Monthly | Weekly | Daily
}, True)
```

### screen_rolling_backtest() — Rolling backtests (5 credits)

```python
client.screen_rolling_backtest({
    'screen': 12345,
    'startDt': '2010-01-01',
    'endDt': '2025-01-01',
    'frequency': 'Every 4 Weeks',
    'holdingPeriod': 182,        # days
    'slippage': 0.25,
    'transPrice': 1
})
```

---

## Strategy <a name="strategy"></a>

### strategy() — Get strategy summary & statistics (1 credit)

```python
client.strategy(strategy_id=12345)
```

### strategy_holdings() — Get current/historical holdings (1 credit)

```python
client.strategy_holdings(
    strategy_id=12345,
    date='2025-03-08',    # None for today
    to_pandas=True
)
```

### strategy_rebalance() — Get rebalance recommendations (1 credit)

```python
client.strategy_rebalance(
    strategy_id=12345,
    params={
        'pitMethod': 'Complete',
        'op': 'Rebal',          # Rebal | Recon | ReconRebal (for Dynamic Weight)
        'reject': [],            # list of P123 IDs to reject
        'figi': 'Share Class'
    }
)
```

### strategy_rebalance_commit() — Commit transactions (1 credit)

```python
client.strategy_rebalance_commit(
    strategy_id=12345,
    params={
        'op': '<op from rebalance>',
        'ranks': '<ranks from rebalance>',
        'trans': [
            {'p123Uid': 1073741824, 'action': 'BUY', 'price': 150.25,
             'shares': 100, 'comm': 1.0, 'slip': 0.1, 'note': 'API order'}
        ]
    }
)
```

### strategy_transactions() — Transaction history (1 credit)

```python
client.strategy_transactions(
    strategy_id=12345,
    start='2025-01-01',
    end='2025-03-08',
    to_pandas=True
)
```

### strategy_transaction_import() — Import transactions (1 credit)

```python
# CSV format: date,ticker,type,shares,price,commission,notes
# Types: BUY, SELL, COVER, SHORT, DIV, SPLIT, CASH
client.strategy_transaction_import(
    strategy_id=12345,
    data='2025-04-28,IBM,BUY,100,123.45,1.0,API import',
    content_type='text/csv',
    update_existing=False,
    make_rebal_dt_curr=False
)

# Or from file
client.strategy_transaction_import(
    strategy_id=12345,
    data=open('transactions.csv'),
    content_type='text/csv'
)
```

### strategy_transaction_delete() — Delete transactions (1 credit)

```python
client.strategy_transaction_delete(strategy_id=12345, items=[tranId1, tranId2])
```

---

## Data Series & Stock Factors <a name="data-series"></a>

### Custom Data Series (time series of values by date)

```python
# Create
result = client.data_series_create_update({
    'name': 'My Custom Series',
    'description': 'VIX daily values'
})
series_id = result['id']

# Upload data (CSV: date,value)
# Note: P123 docs use file=, but the wrapper renamed this param to data=
client.data_series_upload(
    data='series_data.csv',
    series_id=series_id,
    existing_data='overwrite',
    date_format='yyyy-mm-dd',
    decimal_separator='.',
    contains_header_row=True
)

# Delete
client.data_series_delete(series_id=series_id)
```

Use in formulas as: `DataSeries("My Custom Series")` or by ID.

### Custom Stock Factors (values by date × ticker)

```python
# Create
result = client.stock_factor_create_update({
    'name': 'MyMLSignal',
    'description': 'ML prediction scores'
})
factor_id = result['id']

# Upload data (CSV: date,ticker,value)
# Note: P123 docs use file=, but the wrapper renamed this param to data=
client.stock_factor_upload(
    data='factors.csv',
    factor_id=factor_id,
    column_separator='comma',
    existing_data='overwrite',
    date_format='yyyy-mm-dd'
)

# Delete
client.stock_factor_delete(factor_id=factor_id)
```

Use in formulas as: `StockFactor("MyMLSignal")` or by ID.

---

## AI Factor <a name="ai-factor"></a>

P123's AI Factor system trains ML models (LightGBM, XGBoost) on user-defined features to predict stock returns. The API exposes a single prediction endpoint. For comprehensive documentation, see `ai-factor-reference.md`.

### Quick Reference

```python
# Get current predictions
df = client.aifactor_predict(predictor_id=123456, to_pandas=True)

# With features and names
df = client.aifactor_predict(123456, {
    'includeNames': True,
    'includeFeatures': True,
    'precision': 4
}, to_pandas=True)

# Historical (must be Saturday)
df = client.aifactor_predict(123456, {'asOfDt': '2026-03-14'}, to_pandas=True)
```

**Cost:** 20 credits per call. See `ai-factor-reference.md` for full parameter docs, response schema, quota management, and operational gotchas.

---

## API Credits & Limits <a name="credits"></a>

| Operation | Credits |
|-----------|---------|
| data | 1 per 100K data points |
| data_prices | 1 per call |
| data_universe | 1 per 100K data points |
| universe_update | 1 |
| rank_ranks | 1 per 100K points (min 2) |
| rank_perf | 3 |
| rank_update | 1 |
| screen_run | 2 |
| screen_backtest | 5 |
| screen_rolling_backtest | 5 |
| strategy (all ops) | 1 each |
| data_series (all ops) | 1 each |
| stock_factor (all ops) | 1 each |

Error handling:

```python
try:
    result = client.screen_run({...})
except p123api.ClientException as e:
    print(f"API Error: {e}")
```
