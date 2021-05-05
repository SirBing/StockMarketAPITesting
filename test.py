import yfinance as yf

aapl = yf.Ticker("aapl")
aapl

aapl_historical = aapl.history(interval="1d")
aapl_historical