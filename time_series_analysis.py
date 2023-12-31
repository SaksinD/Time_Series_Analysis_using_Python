# -*- coding: utf-8 -*-
"""Time_Series_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BJHt97SYmQEB4t1fLr5ty-9Kbf03CoOp

## **Time Series Analysis**
* Whenever we are analyzing a dataset recorded over a time interval, we are doing Time Series Analysis.
* The time interval of a time series data can be weekly, monthly, daily, or even hourly time intervals, but the process of analyzing our data will remain the same in most of the problems

* Let’s start the task of Time Series Analysis using Python by importing the necessary Python libraries and a time series dataset:
"""

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta

# Get the current date
today = date.today()

# Format the current date as a string in the format 'YYYY-MM-DD'
d1 = today.strftime("%Y-%m-%d")
end_date = d1

# Calculate a date 720 days (approximately 2 years) ago from today's date
d2 = date.today() - timedelta(days=720)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

# Use the yfinance library to download historical stock data for 'AAPL'
data = yf.download('TSLA',
                   start=start_date,
                   end=end_date,
                   progress=False)

# Print the first few rows of the downloaded data
print(data.head())

"""Yahoo Finance is one of the most popular websites to collect stock price data. You need to visit the website, enter the company’s name or stock symbol, and you can easily download the dataset. But if you want to get the latest dataset every time you are running your code, you need to use the yfinance API. yfinance is an API provided by Yahoo Finance to collect the latest stock price data.

* In the above code, I have used the yfinance API to extract the latest stock price data.
* Now let’s visualize a line plot to see the trends in stock prices of Tesla lnc:
"""

import yfinance as yf

# Create a ticker object for the stock you're interested in
ticker_symbol = "TSLA"  # Example stock symbol for TESLA.
stock = yf.Ticker(ticker_symbol)

# Fetch historical data for the stock
historical_data = stock.history(period="1y")  # Fetch data for the past year

# Print the fetched historical data
print(historical_data)

import plotly.express as px
figure = px.line(data, x = data.index,
                 y = "Close",
                 title = "Time Series Analysis (Line Plot)")
figure.show()

"""* A line plot is one of the best visualization tools while working on Time series analysis. In the below code, I am visualizing the trends in the close prices of Tesla lnc. If you place the cursor on the line, you will see the Close price on the exact date of the data point on which your cursor is :

* Now let’s visualize a candlestick chart to see the trends in the open, high, low, and close prices of Tesla lnc.
"""

import plotly.graph_objects as go
figure = go.Figure(data=[go.Candlestick(x = data.index,
                                        open = data["Open"],
                                        high = data["High"],
                                        low = data["Low"],
                                        close = data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart)",
                     xaxis_rangeslider_visible = False)
figure.show()

"""* A candlestick chart is always helpful in the time series analysis of a financial instrument.
* The red lines of this chart indicate a fall in prices, and the green lines indicate an increase in prices.
* If you place the cursor on any point in the above candlestick chart, you will see all the prices of Apple (open, high, low, and close) on the date where your cursor is:

* Now let’s visualize a bar plot to visualize the trends of close prices over the period:
"""

figure = px.bar(data, x = data.index,
                y = "Close",
                title = "Time Series Analysis (Bar Plot)" )
figure.show()

"""* The bar plot above shows an increase in stock prices in the long term scenario.
* The line chart and candlestick chart show you increase and decrease of the price, but if you want to see the price increase and decrease in the long term, you should always prefer a bar chart.

* If we want to analyze stock prices between the period of two specific dates, then below is how we can do it:
"""

figure = px.line(data, x = data.index,
                 y = 'Close',
                 range_x = ['2022-07-01','2022-12-31'],
                 title = "Time Series Analysis (Custom Date Range)")
figure.show()

"""* One of the best ways to analyze a time series data is to create an interactive visualization where we can manually select the time interval in the output visualization itself.
* One way to do it is to add a slider below our visualization and buttons to control time intervals above our visualization.
* Below is how we can create an interactive candlestick chart where we can select time intervals in the output itself:
"""

figure = go.Figure(data = [go.Candlestick(x = data.index,
                                        open = data["Open"],
                                        high = data["High"],
                                        low = data["Low"],
                                        close = data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart with Buttons and Slider)")

figure.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
            dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
            dict(step = "all")
        ])
    )
)
figure.show()