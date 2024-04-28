# FE520-Project

{Title: Python package for ticker visualization, ratios, etc.}

# visualize(ticker, start = None, end = None, frequency = "daily", chart = "line")

The `visualize` function downloads and visualizes stock data for a given ticker symbol over a specified period. It supports line plots and can be extended to candlestick charts. The frequency of the data can be specified as daily or weekly.

## Parameters

- `ticker` (str): The ticker symbol for the stock to be visualized. Examples include "AAPL" for Apple or "TSLA" for Tesla.
- `start` (str): The start date for the data retrieval in 'YYYY-MM-DD' format.
- `end` (str): The end date for the data retrieval in 'YYYY-MM-DD' format.
- `frequency` (str, optional): The frequency of the data. Valid options are "daily" or "weekly". Default value is "daily".
- `chart` (str, optional): The type of chart to visualize. Valid options are "line" or "candle". Default value is "line".

## Raises

- `ValueError`: If the `start` or `end` dates are not provided, or if `frequency` or `chart` has an invalid value.
- `RuntimeError`: If there is an error while downloading stock data or during plotting.
- `NotImplementedError`: If the candlestick charting is attempted, but not implemented.

## Usage

```python
# Example 1: Visualize Apple stock data as a daily line plot from January 2021 to December 2021
visualize("AAPL", start="2021-01-01", end="2021-12-31")

# Example 2: Visualize Tesla stock data as a weekly line plot from January 2021 to December 2021
visualize("TSLA", start="2021-01-01", end="2021-12-31", frequency="weekly")

# Example 3: Attempting to use a candlestick chart raises NotImplementedError
try:
    visualize("AAPL", start="2021-01-01", end="2021-12-31", chart="candle")
except NotImplementedError as e:
    print(e)
```

# visualize_against_sp500(ticker, start = None, end = None, frequency = "daily")

The `visualize_against_sp500` function visualizes a given stock's adjusted closing price against the S&P 500 index over a specified date range. It supports daily and weekly frequencies.

## Parameters

- `ticker` (str): The stock ticker symbol to visualize, such as "AAPL" for Apple or "MSFT" for Microsoft.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is also required.
- `frequency` (str, optional): The frequency of the data. It can be either "daily" or "weekly". Defaults to "daily".

## Raises

- `ValueError`: If `start` or `end` is not provided, or if `frequency` has an invalid value.
- `RuntimeError`: If an error occurs during data retrieval or plotting.

## Usage


```python

#Example 1: Visualize Apple stock against the S&P 500 on a daily frequency
visualize_against_sp500("AAPL", start="2022-01-01", end="2022-12-31")

# Example 2: Visualize Microsoft stock against the S&P 500 on a weekly frequency
visualize_against_sp500("MSFT", start="2022-01-01", end="2022-12-31", frequency="weekly")

# Example 3: Handle missing start or end dates
try:
    visualize_against_sp500("GOOGL", start=None, end="2022-12-31")
except ValueError as e:
    print(f"Error: {e}")

```

# log_returns(ticker, start = None, end = None, frequency = "daily")

The `log_returns` function calculates the logarithmic returns for a specified stock over a given date range and frequency. It uses daily or weekly data to compute the log returns, allowing for financial analysis and other time series operations.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "GOOGL" for Google.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is also required.
- `frequency` (str, optional): The frequency of the data. It can be either "daily" or "weekly". Default value is "daily".

## Returns

- A `pandas.DataFrame` containing the logarithmic returns for the specified stock. The data will be without NaN values.

## Raises

- `ValueError`: If the `start` or `end` dates are not provided, or if the `frequency` is invalid.
- `RuntimeError`: If there is an error during data retrieval or calculation.

## Usage

```python
# Example 1: Calculate daily log returns for Apple stock in 2021
log_returns = log_returns("AAPL", start="2021-01-01", end="2021-12-31")
print(log_returns.head())  # Display the first few rows of the log returns

# Example 2: Calculate weekly log returns for Microsoft stock in 2022
log_returns = log_returns("MSFT", start="2022-01-01", end="2022-12-31", frequency="weekly")
print(log_returns.describe())  # Get summary statistics for the log returns

# Example 3: Handle missing or incorrect input parameters
try:
    log_returns("TSLA", start=None, end="2021-12-31")
except ValueError as e:
    print(f"Error: {e}")
```

# daily_returns(ticker, start = None, end = None, frequency = "daily")

The `daily_returns` function calculates the daily returns (percentage change) for a given stock over a specified date range and frequency. It uses daily or weekly adjusted closing prices to compute the returns.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "TSLA" for Tesla.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is also required.
- `frequency` (str, optional): The frequency of the data. Options are "daily" or "weekly". Defaults to "daily".

## Returns

- A `pandas.DataFrame` containing the daily returns (percentage change) for the specified stock. The DataFrame does not contain NaN values.

## Raises

- `ValueError`: If the `start` or `end` dates are not provided, or if the `frequency` has an invalid value.
- `RuntimeError`: If there is an error during data retrieval or calculation.

## Usage


```python
# Example 1: Calculate daily returns for Apple stock in 2021
daily_returns = daily_returns("AAPL", start="2021-01-01", end="2021-12-31")
print(daily_returns.head())  # Display the first few rows of the daily returns

# Example 2: Calculate weekly returns for Microsoft stock in 2022
daily_returns = daily_returns("MSFT", start="2022-01-01", end="2022-12-31", frequency="weekly")
print(daily_returns.describe())  # Get summary statistics for the daily returns

# Example 3: Handle invalid start or end dates
try:
    daily_returns("GOOGL", start=None, end="2022-12-31")
except ValueError as e:
    print(f"Error: {e}")
```

# rolling_volatility(ticker, start = None, end = None, frequency = "daily", window = 20)

The `rolling_volatility` function calculates the rolling standard deviation (volatility) of daily returns for a given stock over a specified period and frequency. It supports daily and weekly frequencies, with a customizable window size for the rolling calculation.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "TSLA" for Tesla.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `frequency` (str, optional): The frequency of the data. Options are "daily" or "weekly". Defaults to "daily".
- `window` (int, optional): The window size for the rolling standard deviation. Defaults to 20.

## Returns

- A `pandas.DataFrame` containing the rolling volatility. The output DataFrame does not contain NaN values.

## Raises

- `ValueError`: If the `start` or `end` dates are not provided, or if `frequency` has an invalid value.
- `RuntimeError`: If there is an error during data retrieval or calculation.

## Usage

```python
# Example 1: Calculate 20-day rolling volatility for Apple stock in 2021
rolling_volatility = rolling_volatility("AAPL", start="2021-01-01", end="2021-12-31")
print(rolling_volatility.head())  # Display the first few rows of the rolling volatility

# Example 2: Calculate 20-week rolling volatility for Tesla stock in 2022
rolling_volatility = rolling_volatility("TSLA", start="2022-01-01", end="2022-12-31", frequency="weekly")
print(rolling_volatility.describe())  # Get summary statistics for the rolling volatility

# Example 3: Handle invalid frequency
try:
    rolling_volatility("MSFT", start="2021-01-01", end="2021-12-31", frequency="monthly")
except ValueError as e:
    print(f"Error: {e}")
```

# sharpe_ratio(ticker, start = None, end = None, risk_free_rate = 0.01, frequency = 'daily')

The `sharpe_ratio` function calculates the Sharpe ratio for a given stock over a specified date range and frequency. It measures the risk-adjusted return of an investment, comparing the expected excess return to the standard deviation of returns.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "MSFT" for Microsoft.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is also required.
- `risk_free_rate` (float, optional): The annualized risk-free rate. Defaults to 0.01 (1%).
- `frequency` (str, optional): The frequency of the data. Options are "daily" or "weekly". Defaults to "daily".

## Returns

- A single float value representing the Sharpe ratio for the specified stock and date range.

## Raises

- `ValueError`: If `start` or `end` is not provided, or if `frequency` is not one of the expected values.
- `RuntimeError`: If there is an error during data retrieval or Sharpe ratio calculation.

## Usage

```python
# Example 1: Calculate the daily Sharpe ratio for Apple stock in 2021
sharpe_ratio = sharpe_ratio("AAPL", start="2021-01-01", end="2021-12-31")
print(f"Sharpe Ratio for AAPL in 2021: {sharpe_ratio:.2f}")

# Example 2: Calculate the weekly Sharpe ratio for Microsoft stock in 2022
sharpe_ratio = sharpe_ratio("MSFT", start="2022-01-01", end="2022-12-31", frequency='weekly')
print(f"Sharpe Ratio for MSFT in 2022 (Weekly): {sharpe_ratio:.2f}")

# Example 3: Handle invalid frequency input
try:
    sharpe_ratio("TSLA", start="2021-01-01", end="2021-12-31", frequency='monthly')
except ValueError as e:
    print(f"Error: {e}")
```

# pe_ratio(ticker, period = "1d")

The `pe_ratio` function calculates the Price/Earnings (P/E) ratio for a given stock. The P/E ratio is a measure of the stock's price relative to its earnings per share.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "GOOGL" for Google. This parameter is required.
- `period` (str, optional): The period to consider for the stock price. Defaults to "1d".

## Returns

- A float representing the P/E ratio for the given stock and period.

## Raises

- `ValueError`: If the `ticker` is not provided, if no data is available for the specified period, or if trailing EPS is invalid.
- `RuntimeError`: If there is an error during data retrieval or P/E ratio calculation.

## Usage

```python
# Example 1: Calculate the P/E ratio for Apple stock
pe_ratio = pe_ratio("AAPL")
print(f"P/E Ratio for AAPL: {pe_ratio:.2f}")

# Example 2: Calculate the P/E ratio for Tesla with custom period
pe_ratio = pe_ratio("TSLA", period="5d")
print(f"P/E Ratio for TSLA (5-day period): {pe_ratio:.2f}")

# Example 3: Handle invalid ticker input
try:
    pe_ratio("")
except ValueError as e:
    print(f"Error: {e}")
```

# ps_ratio(ticker, start = None, end = None)

The `ps_ratio` function calculates the Price/Sales (P/S) ratio for a given stock over a specified period. The P/S ratio measures the stock's price relative to its revenue.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "TSLA" for Tesla. This parameter is required.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.

## Returns

- A float representing the Price/Sales (P/S) ratio for the given stock.

## Raises

- `ValueError`: If `start` or `end` dates are not provided, if there's no data for the specified period, or if market capitalization or revenue data is missing.
- `RuntimeError`: If there's an error during data retrieval or P/S ratio calculation.

## Usage

```python
# Example 1: Calculate the P/S ratio for Apple stock in 2021
ps_ratio = ps_ratio("AAPL", start="2021-01-01", end="2021-12-31")
print(f"P/S Ratio for AAPL in 2021: {ps_ratio:.2f}")

# Example 2: Handle missing revenue data
try:
    ps_ratio("INVALID", start="2021-01-01", end="2021-12-31")
except ValueError as e:
    print(f"Error: {e}")
```

# macd(ticker, start=None, end=None)

The `macd` function calculates and visualizes the Moving Average Convergence Divergence (MACD) for a given stock over a specified period. It plots the MACD line and the Signal line.

## Parameters

- `ticker` (str): The stock ticker symbol to retrieve data for, such as "AAPL" for Apple or "MSFT" for Microsoft. This parameter is required.
- `start` (str): The start date for data retrieval in 'YYYY-MM-DD' format. This parameter is required.
- `end` (str): The end date for data retrieval in 'YYYY-MM-DD' format. This parameter is also required.

## Raises

- `ValueError`: If the `start` or `end` dates are not provided or if there's no data for the specified period.
- `RuntimeError`: If there's an error during data retrieval, calculation, or plotting.

## Usage

```python
# Example 1: Calculate and visualize the MACD for Apple stock in 2021
macd("AAPL", start="2021-01-01", end="2021-12-31")

# Example 2: Handle missing start or end dates
try:
    macd("AAPL", start=None, end="2021-12-31")
except ValueError as e:
    print(f"Error: {e}")
```

# Author: Aayush Khandekar