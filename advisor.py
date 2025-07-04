# advisor.py

from logger import log_advice
import streamlit as st

def get_stock_advice(stock_symbol, stock_data, company_news, global_news):
    # Step 1: Extract closing prices
    try:
        closing_prices = stock_data["Close"].tolist()
    except Exception:
        st.error("❌ Error reading stock closing prices.")
        return

    if not closing_prices or len(closing_prices) < 2:
        st.warning("Not enough data to generate advice.")
        return

    start_price = closing_prices[0]
    end_price = closing_prices[-1]
    percent_change = ((end_price - start_price) / start_price) * 100

    # Step 2: Basic rule-based advice
    if percent_change > 3:
        action = "Sell"
        duration = "Today or next 2 days"
    elif percent_change < -3:
        action = "Buy"
        duration = "Hold 7–10 days"
    else:
        action = "Hold"
        duration = "3–5 days"

    # Step 3: News score (very simple)
    news_score = 0
    if company_news:
        for item in company_news:
            title = item.get("title", "").lower()
            if any(word in title for word in ["profit", "growth", "record", "acquisition", "approval"]):
                news_score += 1
            elif any(word in title for word in ["loss", "lawsuit", "fire", "layoff", "strike"]):
                news_score -= 1

    if global_news:
        for item in global_news:
            title = item.lower()
            if any(word in title for word in ["war", "inflation", "recession", "crash"]):
                news_score -= 1
            elif any(word in title for word in ["stable", "recovery", "peace"]):
                news_score += 1

    # Step 4: Adjust advice slightly
    if action == "Hold" and news_score < 0:
        duration = "1–3 days"

    # Step 5: Show advice in Streamlit
    st.markdown(f"### 📌 Suggested Action for `{stock_symbol}`")
    st.markdown(f"- **Action**: `{action}`")
    st.markdown(f"- **Hold Duration**: `{duration}`")
    st.markdown(f"- **30-Day Change**: `{percent_change:.2f}%`")
    st.markdown(f"- **News Sentiment Score**: `{news_score}`")

    # Step 6: Save to CSV
    log_advice(stock_symbol, action, duration, percent_change, news_score)
