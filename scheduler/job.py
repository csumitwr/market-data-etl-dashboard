from apscheduler.schedulers.blocking import BlockingScheduler

from ingestion.market_api_client import fetch_market_data
from transformation.market_cleaner import clean_market_data
from storage.database import save_to_database


def get_last_searched_symbol():
    try:
        with open("last_search.txt", "r") as file:
            symbol = file.read().strip()

            if not symbol:
                return "AAPL"

            return symbol

    except FileNotFoundError:
        return "AAPL"


def run_pipeline():
    symbol = get_last_searched_symbol()

    print(f"Refreshing latest searched stock: {symbol}")

    try:
        raw_data = fetch_market_data(symbol)
        cleaned_data = clean_market_data(raw_data, symbol)

        save_to_database(cleaned_data)

        print(f"{symbol} updated successfully")

    except Exception as e:
        print(f"Error updating {symbol}: {e}")


scheduler = BlockingScheduler()

scheduler.add_job(
    run_pipeline,
    "interval",
    minutes=10
)

if __name__ == "__main__":
    print("Scheduler started...")
    scheduler.start()