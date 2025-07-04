import csv
from datetime import datetime
import os

def log_advice(stock_symbol, action, duration, percent_change, news_score):
    filename = "advisor_log.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header if file is new
        if not file_exists:
            writer.writerow([
                "Timestamp", "Stock", "Action", "Duration",
                "Percent Change", "News Score"
            ])

        # Clean any special characters from duration
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            stock_symbol,
            action,
            duration.replace("–", "-").replace("\u202f", " "),
            f"{percent_change:.2f}",
            news_score
        ])
