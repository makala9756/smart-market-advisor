# main.py

from recommender import suggest_alternative_stocks
from visualizer import plot_stock_trend
from advisor import get_stock_advice
from global_conditions import fetch_global_conditions
from news_fetcher import fetch_news
import yfinance as yf
import pandas as pd

def get_user_input():
    print("📈 Welcome to Smart Market Advisor!")
    stock_name = input("Enter the stock symbol (e.g., HDFCBANK.NS, TCS.NS): ")
    return stock_name.strip()

def fetch_stock_trend(stock_symbol, period="1mo"):
    print(f"\n📊 Fetching stock data for {stock_symbol} over the last {period}...")
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(period=period)

    if data.empty:
        print("❌ No stock data found. Please check the symbol and try again.")
        return None

    data = data[['Close']].reset_index()
    print("\n📆 Stock closing prices:")
    print(data.to_string(index=False))

    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    change = end_price - start_price
    print(f"\n📉 Price changed from ₹{start_price:.2f} to ₹{end_price:.2f} (Change: ₹{change:.2f})")

    return data

def main():
    stock_symbol = get_user_input()
    stock_data = fetch_stock_trend(stock_symbol)  # 30-day period

    if stock_data is not None:
        plot_stock_trend(stock_symbol, stock_data)

        company_name = stock_symbol.replace(".NS", "").replace(".BO", "")
        news_list = fetch_news(company_name)
        global_news = fetch_global_conditions()

        get_stock_advice(
            stock_symbol = stock_symbol,
            stock_data   = stock_data,
            company_news = news_list,
            global_news  = global_news
        )

  
     # Suggest other good performers
    suggestions = suggest_alternative_stocks(stock_symbol)
    if suggestions:
       print("\n📢 Top Gaining Stocks in Last 7 Days:")
       for sym, change in suggestions:
          print(f"   {sym}: 📈 +{change}%")
    else:
         print("\n📢 No significantly better-performing stocks found.")



if __name__ == "__main__":
    main()

