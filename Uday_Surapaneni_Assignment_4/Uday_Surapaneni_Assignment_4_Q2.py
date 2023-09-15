#!/usr/bin/env python
# coding: utf-8

#Q2
import pandas as pd
import yfinance as yf
import numpy as np

# 1. Extract close prices of Apple, Google, and Meta from Yahoo Finance for the past 10 years
tickers = ['AAPL', 'GOOGL', 'META']
start_date = '2013-08-19'
end_date = '2023-08-19'

df_apple = yf.download('AAPL', start=start_date, end=end_date)['Close']
df_google = yf.download('GOOGL', start=start_date, end=end_date)['Close']
df_meta = yf.download('META', start=start_date, end=end_date)['Close']

# Store the close prices in a dataframe
df = pd.DataFrame({'Apple': df_apple, 'Google': df_google, 'Meta': df_meta})

# 2. Merge all three dataframes on the Date column
df_merged = pd.concat([df_apple, df_google, df_meta], axis=1)

# 3. Calculate log returns of the close price for each stock
df_returns = np.log(df_merged / df_merged.shift(1))

# 4. Calculate VaR for the portfolio
portfolio_returns = df_returns.sum(axis=1)
VaR_99 = portfolio_returns.quantile(0.01)
VaR_95 = portfolio_returns.quantile(0.05)
VaR_90 = portfolio_returns.quantile(0.1)

# 5. Repeat the above exercise for different holding periods
holding_periods = [1, 2, 5, 10]  # in days
confidence_levels = [0.01, 0.05, 0.1]  # percentiles

results = []
for period in holding_periods:
    returns = portfolio_returns.rolling(period).sum().dropna()
    row = {'Holding Period': f'{period} day'}
    for level in confidence_levels:
        VaR = returns.quantile(level)
        row[f'{int((1-level)*100)} percentile VaR'] = VaR
    results.append(row)

df_results = pd.DataFrame(results)

# 6. Create a summary dataframe to show the comparison of Holding Period vs Confidence level
summary_df = df_results.set_index('Holding Period')
print(summary_df)

