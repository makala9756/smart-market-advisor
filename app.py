# app.py

import streamlit as st
import yfinance as yf
import pandas as pd
import pytz
from datetime import datetime, time
from advisor import get_stock_advice
from global_conditions import fetch_global_conditions
from news_fetcher import fetch_news
from recommender import suggest_alternative_stocks

# Set up page
st.set_page_config(page_title="Smart Market Advisor", layout="wide")
st.title("📈 Smart Market Advisor")

# ✅ Function to check if Indian market is open
def is_market_open():
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    current_time = now.time()

    if now.weekday() >= 5:
        return "🔴 Market is CLOSED (Weekend)"
    
    market_start = time(9, 15)
    market_end = time(15, 30)

    if market_start <= current_time <= market_end:
        return "🟢 Market is OPEN"
    elif current_time < market_start:
        return "🕗 Market will OPEN at 9:15 AM IST"
    else:
        return "🔴 Market is CLOSED for today"

# ✅ Show market info and current time
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %p IST")
st.markdown("🕰️ **Indian Stock Market Timings (NSE):** _Mon–Fri, 9:15 AM to 3:30 PM IST_")
st.markdown(f"📅 **Current IST Time:** {current_time}")
st.markdown(f"📢 **Status:** {is_market_open()}")

# ✅ Input
stock_symbol = st.text_input("Enter Stock Symbol (e.g., HDFCBANK.NS, INFY.NS):")

# ✅ Button Click
if st.button("Get Advice") and stock_symbol:
    with st.spinner("📊 Fetching data and analyzing..."):
        data = yf.download(stock_symbol, period="1mo", interval="1d")

        if data.empty:
            st.error("❌ No data found. Please check the stock symbol.")
        else:
            data.reset_index(inplace=True)

            # Flatten columns if needed
            if isinstance(data.columns, pd.MultiIndex) or isinstance(data.columns[0], tuple):
                data.columns = [col[0] for col in data.columns]

            st.success("✅ Stock data fetched successfully!")

            # Check for closing prices
            if "Close" not in data.columns:
                st.error("❌ 'Close' column not found in stock data.")
            else:
                # 📉 Trend chart
                st.subheader(f"{stock_symbol} - 30 Day Price Trend")
                st.line_chart(data.set_index("Date")["Close"])

                # 📰 Fetch news
                company_name = stock_symbol.replace(".NS", "").replace(".BO", "")
                news_list = fetch_news(company_name)
                global_news = fetch_global_conditions()

                # 💡 Recommendation
                st.subheader("💡 Recommendation")
                get_stock_advice(
                    stock_symbol=stock_symbol,
                    stock_data=data,
                    company_news=news_list,
                    global_news=global_news
                )

                # 💹 Other suggestions
                alt_suggestions = suggest_alternative_stocks(stock_symbol)
                if alt_suggestions:
                    st.subheader("📊 Other Top Performing Stocks (Past 7 Days)")
                    for symbol, change in alt_suggestions:
                        st.markdown(f"**{symbol}**: 📈 {change}% gain")
                else:
                    st.info("No strong alternate stock suggestions at the moment.")
