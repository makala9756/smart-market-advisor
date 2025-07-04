# app.py

import streamlit as st
import yfinance as yf
import pandas as pd
from advisor import get_stock_advice
from global_conditions import fetch_global_conditions
from news_fetcher import fetch_news

st.set_page_config(page_title="Smart Market Advisor", layout="wide")
st.title("📈 Smart Market Advisor")

# Input
stock_symbol = st.text_input("Enter Stock Symbol (e.g., HDFCBANK.NS, INFY.NS):")

# Button Click
if st.button("Get Advice") and stock_symbol:
    with st.spinner("📊 Fetching data and analyzing..."):
        # Fetch stock data
        data = yf.download(stock_symbol, period="1mo", interval="1d")

        # Check if data is valid
        if data.empty:
            st.error("❌ No data found. Please check the stock symbol.")
        else:
            data.reset_index(inplace=True)

            # ✅ Fix: Flatten multi-level columns like ('Close', 'INFY.NS')
            if isinstance(data.columns, pd.MultiIndex) or isinstance(data.columns[0], tuple):
                data.columns = [col[0] for col in data.columns]

            st.success("✅ Stock data fetched successfully!")


            # Ensure 'Close' column is present
            if "Close" not in data.columns:
                st.error("❌ 'Close' column not found in stock data.")
            else:
                # Show trend chart
                st.subheader(f"{stock_symbol} - 30 Day Price Trend")
                st.line_chart(data.set_index("Date")["Close"])

                # Fetch company + global news
                company_name = stock_symbol.replace(".NS", "").replace(".BO", "")
                news_list = fetch_news(company_name)
                global_news = fetch_global_conditions()

                # Show recommendation
                st.subheader("💡 Recommendation")
                get_stock_advice(
                    stock_symbol=stock_symbol,
                    stock_data=data,
                    company_news=news_list,
                    global_news=global_news
                )
