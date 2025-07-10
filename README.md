# 📈 Smart Market Advisor

**Smart Market Advisor** is an AI-powered stock suggestion and news analysis tool that provides actionable insights like **Buy/Hold/Sell** recommendations based on:
- Recent stock trends
- Company-specific news
- Global economic indicators

🎯 Built as part of the PromptForge Hackathon  
🚀 Tech Stack: Python, Streamlit, yFinance, Web Scraping (news), Pandas

---

## 🔍 Features

- 📊 Fetch 30-day price trends of any NSE stock (e.g., `TCS.NS`, `HDFCBANK.NS`)
- 📰 Analyze company news and global conditions (no paid APIs used)
- 💡 Suggest Buy / Hold / Sell with duration (e.g., Hold for 3–5 days)
- ✅ Visual trend charts
- 💹 Show top 3 other performing stocks (last 7 days)
- 🕒 Displays Indian Stock Market live status (Open/Closed)

---

## 📦 How to Run Locally

```bash
# Step 1: Clone the repo
git clone https://github.com/makala9756/smart-market-advisor.git
cd smart-market-advisor

# Step 2: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # for Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Streamlit app
streamlit run app.py
