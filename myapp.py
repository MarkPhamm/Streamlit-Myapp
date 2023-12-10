import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google using markdown!
\n
         

 Here's the [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
         

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

tickerSymbol = st.text_input('Input a ticker symbol')
if tickerSymbol:
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31')

    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)
    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)
else: 
    st.write("PLease enter a valid ticker symbol")
