# visualizer.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_stock_trend(stock_symbol, stock_data):
    dates = stock_data['Date']
    closing_prices = stock_data['Close']

    plt.figure(figsize=(10, 5))
    plt.plot(dates, closing_prices, marker='o', linestyle='-', color='blue', label='Close Price')
    plt.title(f"{stock_symbol} - Last 30 Days Trend", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Close Price (INR)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()

    # Format x-axis to show fewer ticks
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))

    # Show last price as annotation
    last_date = dates.iloc[-1]
    last_price = closing_prices.iloc[-1]
    plt.annotate(f"{last_price:.2f}", xy=(last_date, last_price),
                 xytext=(last_date, last_price + 10),
                 arrowprops=dict(facecolor='green', shrink=0.05),
                 fontsize=10, ha='center')

    plt.show()
