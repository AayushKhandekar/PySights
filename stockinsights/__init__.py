import warnings
import numpy as np
import pandas as pd
import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

# filter warnings
warnings.filterwarnings('ignore') 

valid_frequencies = ["daily", "weekly"]
valid_charts = ["line", "candle"]

def visualize(ticker, start = None, end = None, frequency = "daily", chart = "line"):

    '''Function to visualize ticker data within a specific period. Visualization can be a line plot or a candlestick chart'''

    # input validation
    if not start or not end:
        raise ValueError("Both start date and end date must be provided")
    if frequency not in valid_frequencies:
        raise ValueError(f"Invalid frequency '{frequency}'. Valid options are 'daily' or 'weekly'.")
    if chart not in valid_charts:
        raise ValueError(f"Invalid chart type '{chart}'. Valid options are 'line' or 'candle'.")

    # download data based on frequency
    try:
        data = yf.download(ticker, start=start, end=end)
        if frequency == "weekly":
            data = data.resample('W').last()
    except Exception as e:
        raise RuntimeError(f"Error downloading data for {ticker}: {e}")

    # plot the chart
    try:
        if chart == "line":
            plt.plot(data['Close'], color="black")
            plt.title(f"{ticker} {frequency.capitalize()} {chart} Chart")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.show()
        elif chart == "candle":
            raise NotImplementedError("Candlestick charting is currently unavailable.")
    except Exception as e:
        raise RuntimeError(f"Error during plotting: {e}")

    return None

def visualize_against_sp500(ticker, start = None, end = None, frequency = "daily"):
    
    '''Visualize stock price against S&P 500 index for a specific date range and frequency.'''

    valid_frequencies = ["daily", "weekly"]

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided")
    if frequency not in valid_frequencies:
        raise ValueError("Invalid frequency: expected 'daily' or 'weekly'")

    # download data and plot
    try:
        stock_data = yf.download(ticker, start = start, end = end)
        sp500_data = yf.download("^GSPC", start = start, end = end)
        if frequency == "weekly":
            stock_data = stock_data.resample('W').last()
            sp500_data = sp500_data.resample('W').last()
        
        # plot ticker data against s&p500
        plt.plot(stock_data['Adj Close'], label=ticker, color='blue')
        plt.plot(sp500_data['Adj Close'], label='S&P 500', color='black')
        plt.title(f'{ticker} vs. S&P 500 - {frequency.capitalize()}')
        plt.xlabel('Date')
        plt.ylabel('Adjusted Close Price (USD)')
        plt.legend()
        plt.show()
        
    except Exception as e:
        raise RuntimeError(f"An error occurred during data retrieval or plotting: {e}")

    return None

def log_returns(ticker, start = None, end = None, frequency = "daily"):
    
    '''generate logarithmic returns for a given stock over a specific date range and frequency.'''

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided in 'YYYY-MM-DD' format.")
    if frequency not in valid_frequencies:
        raise ValueError("Invalid frequency: expected 'daily' or 'weekly'.")

    try:
        # download data and generate logarithmic returns
        data = yf.download(ticker, start=start, end=end)        
        if frequency == "weekly":
            data = data.resample('W').last()
        log_returns = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
        
    except Exception as e:
        raise RuntimeError(f"Error calculating log returns: {e}")

    log_returns = pd.DataFrame(log_returns.dropna())

    return log_returns

def daily_returns(ticker, start = None, end = None, frequency = "daily"):

    '''Calculate daily returns (percentage change) for a given stock over a specified period and frequency.'''

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided")
    if frequency not in valid_frequencies:
        raise ValueError("Invalid frequency: expected 'daily' or 'weekly'")

    try:
        # calculate daily returns
        data = yf.download(ticker, start=start, end=end)
        if frequency == "weekly":
            data = data.resample('W').last()
        daily_returns = data['Adj Close'].pct_change()

    except Exception as e:
        raise RuntimeError(f"An error occurred while retrieving data or calculating daily returns: {e}")

    daily_returns = pd.DataFrame(daily_returns.dropna())
    
    return daily_returns

def rolling_volatility(ticker, start = None, end = None, frequency = "daily", window = 20):
    
    '''calculate rolling volatility for a given stock over a specified date range and frequency.'''

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided in 'YYYY-MM-DD' format.")
    if frequency not in valid_frequencies:
        raise ValueError("Invalid frequency: expected 'daily' or 'weekly'.")

    try:
        # data download
        data = yf.download(ticker, start=start, end=end)["Adj Close"]
        if frequency == "weekly":
            data = data.resample('W').last()
       
        # calculate daily returns and rolling volatility
        daily_returns = data.pct_change()
        rolling_volatility = daily_returns.rolling(window = window).std()

    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating rolling volatility: {e}")

    return pd.DataFrame(rolling_volatility)

def sharpe_ratio(ticker, start = None, end = None, risk_free_rate = 0.01, frequency = 'daily'):
    
    '''function to calculate the Sharpe ratio for a given stock over a specific date range and frequency.'''

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided in 'YYYY-MM-DD' format.")
    if frequency not in valid_frequencies:
        raise ValueError("Invalid frequency: expected 'daily' or 'weekly'.")

    try:
        data = yf.download(ticker, start = start, end = end) 
        if frequency == 'daily':
            returns = data['Adj Close'].pct_change()
        elif frequency == 'weekly':
            returns = data.resample('W').last()['Adj Close'].pct_change()

        # considering 252 trading days per year
        excess_returns = returns - (risk_free_rate / 252)  
        std_dev = returns.std()

        # Calculate Sharpe ratio
        sharpe_ratio = np.mean(excess_returns) / std_dev
        
    except Exception as e:
        raise RuntimeError(f"Error calculating Sharpe ratio: {e}")

    return sharpe_ratio

def pe_ratio(ticker, period = "1d"):
    
    '''function to calculate the Price/Earnings (P/E) ratio for a given stock.'''

    # input validatino
    if not ticker:
        raise ValueError("A valid ticker symbol must be provided")
    try:
        # download ticker data
        stock = yf.Ticker(ticker)
        data = stock.history(period = period)
       
        if data.empty:
            raise ValueError("No data available for the given ticker and period.")

        closing_price = data['Close'].iloc[-1]
        ttm_eps = stock.info.get('trailingEps', None)
        
        if ttm_eps is None or ttm_eps == 0:
            raise ValueError("Trailing EPS is invalid or not available")

        # calculate P/E ratio
        pe_ratio = closing_price / ttm_eps
        
    except Exception as e:
        raise RuntimeError(f"Error calculating P/E ratio for {ticker}: {e}")

    return pe_ratio

def ps_ratio(ticker, start = None, end = None):

    '''function to calculate the Price/Sales (P/S) ratio for a given stock over a specified period.'''

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided")
    
    try:
        # Download stock data
        stock = yf.Ticker(ticker)
        stock_data = stock.history(start = start, end = end) 

        if stock_data.empty:
            raise ValueError("No data available for the given ticker and period")

        latest_price = stock_data['Close'].iloc[-1]
        market_cap = stock.info.get('marketCap', None)
        ttm_revenue = stock.info.get('totalRevenue', None)

        if not market_cap or not ttm_revenue:
            raise ValueError("Market capitalization or revenue data is missing.")

        # calculate P/S ratio
        ps_ratio = market_cap / ttm_revenue

    except Exception as e:
        raise RuntimeError(f"Error calculating P/S ratio for {ticker}: {e}")

    return ps_ratio

def macd(ticker, start = None, end = None):

    '''function to calculate and visualize the Moving Average Convergence Divergence (MACD) for a given stock.'''

    # input validation
    if not start or not end:
        raise ValueError("Both start and end dates must be provided")

    try:
        data = yf.download(ticker, start=start, end=end)        
        
        if data.empty:
            raise ValueError("No data available for the given ticker and period")

        # calculate long and short exponential moving average
        short_ema = data['Adj Close'].ewm(span = 12, adjust = False).mean()
        long_ema = data['Adj Close'].ewm(span = 26, adjust = False).mean()
        
        macd_line = short_ema - long_ema
        signal_line = macd_line.ewm(span = 9, adjust = False).mean()

        # plot the MACD and signal line
        plt.plot(data.index, macd_line, label='MACD', color='red')
        plt.plot(data.index, signal_line, label='Signal', color='blue')
        plt.title(f'MACD for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('MACD')
        plt.legend()
        plt.show()

    except Exception as e:
        raise RuntimeError(f"Error calculating or plotting MACD for {ticker}: {e}")

    return None