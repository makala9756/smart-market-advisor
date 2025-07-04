# global_conditions.py

import requests
from bs4 import BeautifulSoup

def fetch_global_conditions():
    print("\n🌐 Checking global economic and political news...")

    url = "https://www.google.com/search?q=world+economy+stock+news&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = []

        for item in soup.select("div.BNeawe.vvjwJb.AP7Wnd")[:5]:
            headlines.append(item.get_text())

        if not headlines:
            print("⚠️ No global news found.")
        else:
            print("\n🌍 Global Market Conditions:")
            for i, h in enumerate(headlines, 1):
                print(f"{i}. {h}")

        return headlines

    except Exception as e:
        print("❌ Error fetching global news:", e)
        return []
