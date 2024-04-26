# FE520-Project

{Title: Python package for ticker visualization, ratios, etc.}

Step 1: Get ticker from user (No need for separate function) (check if ticker exists)


Function 2 to n (n = number of financial ratios): previous years financial ratios (check .info() which i used in the other project) (ticker, year)

p/e ratio, beta, etc.

Function 3: log_returns()

Function 4: daily_returns()

Function 5: weekly_log_returns()

Function 6: rolling_volatility()

Function 7: technical_indicators()

### visualize()

{package} provides the visualize() function to view ticker data. 

visualize() function takes the following arguments:

- `ticker`: Ticker for which the visualization needs to be created.
- `start`: The date from which the data needs to be visualized.
- `end`: The date till which the data needs to be visualized.
- `frequency`: The frequency of the data can be either <b>"daily"</b> or <b>weekly</b>. `frequency = "daily"` is the default argument for the function.
- `chart`: The visualization takes two values for chart (`"line"`, `"candle"`). `"line"` is the default argument for the function. `"candle"` is currently unavailable.

#### Example

1. `frequency = "daily"`:

`visualize("AAPL", start = "2012-01-01", end = "2020-01-01")`

`visualize("AAPL", start = "2012-01-01", end = "2020-01-01", frequency = "daily")`

2. `frequency = "weekly"`:

`visualize("AAPL", start = "2012-01-01", end = "2020-01-01", frequency = "weekly")`


#### Author: Aayush Khandekar