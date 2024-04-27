# FE520-Project

{Title: Python package for ticker visualization, ratios, etc.}


Function 7: technical_indicators()

### 1. visualize()

{package} provides the visualize() function to view ticker data. 

1. visualize() function takes the following arguments:

- `ticker`: Ticker for which the visualization needs to be created.
- `start`: The date from which the data needs to be visualized.
- `end`: The date till which the data needs to be visualized.
- `frequency`: The frequency of the data can be either <b>"daily"</b> or <b>weekly</b>. `frequency = "daily"` is the default argument for the function.
- `chart`: The visualization takes two values for chart (`"line"`, `"candle"`). `"line"` is the default argument for the function. `"candle"` is currently unavailable.

#### 1.1. Example

1. `frequency = "daily"`:

`visualize("AAPL", start = "2012-01-01", end = "2020-01-01")`

`visualize("AAPL", start = "2012-01-01", end = "2020-01-01", frequency = "daily")`

2. `frequency = "weekly"`:

`visualize("AAPL", start = "2012-01-01", end = "2020-01-01", frequency = "weekly")`

### 2. log_returns()

log_returns() functions returns the calculated log returns of the dataframe and returns the dataframe.

- `ticker`: Ticker for which the visualization needs to be created.
- `start`: The date from which the data needs to be visualized.
- `end`: The date till which the data needs to be visualized.
- `frequency`: The frequency of the data can be either <b>"daily"</b> or <b>weekly</b>. `frequency = "daily"` is the default argument for the function.

#### 2.1. Example

1. `log_returns("AAPL", start = "2012-01-01", end = "2022-01-01")`
   
2. `log_returns("AAPL", start = "2012-01-01", end = "2022-01-01", frequency = "weekly")`

### 3. daily_returns()

### 4.rolling_volatility()

#### 4.1 Example

1. `rolling_volatility("AAPL", start = "2012-01-01", end = "2022-01-01", frequency = "weekly", window = 3)`

### 5. visualize_against_sp500()

#### Example

5.1 `visualize_against_sp500("MSFT", start = "2020-01-01", end = "2022-01-01", frequency = "daily")`

#### Author: Aayush Khandekar