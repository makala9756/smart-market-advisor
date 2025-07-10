# recommender.py

import yfinance as yf

def suggest_alternative_stocks(exclude_symbol=None):
    watchlist = [
        "TCS.NS", "INFY.NS", "RELIANCE.NS", "HDFCBANK.NS",
        "ICICIBANK.NS", "ITC.NS", "LT.NS", "SBIN.NS", "AXISBANK.NS",
        "BAJFINANCE.NS", "WIPRO.NS", "HCLTECH.NS"
    ]

    if exclude_symbol in watchlist:
        watchlist.remove(exclude_symbol)

    results = []
    for symbol in watchlist:
        try:
            data = yf.download(symbol, period="7d", interval="1d", progress=False)
            if data.empty or len(data) < 2:
                continue

            start_price = data['Close'].iloc[0]
            end_price = data['Close'].iloc[-1]
            change_percent = ((end_price - start_price) / start_price) * 100

            if change_percent > 2:  # Adjustable threshold
                results.append((symbol, round(change_percent, 2)))

        except Exception as e:
            print(f"Error fetching {symbol}: {e}")

    # Sort by best performance
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:3]  # Return top 3
