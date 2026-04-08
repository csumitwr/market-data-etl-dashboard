import yfinance as yf
import pandas as pd

def fetch_market_data (symbol, period="1mo", interval="1d"):
    try:
        ticker = yf.Ticker(symbol)
        historical_data = ticker.history(period= period, interval= interval)

        if historical_data.empty:
            raise ValueError(f"No data found for symbol: {symbol}. Please check the symbol & parameters.")
        
        historical_data.reset_index(inplace=True)
        historical_data.columns = historical_data.columns.str.lower()

        return historical_data
    
    except:
        print("No connection, please check internet.")

if __name__ == "__main__":
    aapl_data = fetch_market_data("AAPL")

    print(aapl_data.head())