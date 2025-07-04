# news_fetcher.py

import requests
from bs4 import BeautifulSoup

def fetch_news(company_name):
    print(f"\n📰 Searching for news about {company_name}...")

    query = company_name + " stock news"
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = []

        for item in soup.select("div.BNeawe.vvjwJb.AP7Wnd")[:5]:
            headlines.append(item.get_text())

        if not headlines:
            print("⚠️ No news headlines found.")
        else:
            print("\n🗞️ Top News Headlines:")
            for i, h in enumerate(headlines, 1):
                print(f"{i}. {h}")

        return headlines

    except Exception as e:
        print("❌ Error fetching news:", e)
        return []
