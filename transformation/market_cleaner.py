import pandas as pd

def clean_market_data(df, symbol):
    cleaned_df = df.copy()
    
    cleaned_df["symbol"] = symbol
    cleaned_df["date"] = pd.to_datetime(cleaned_df["date"])

    cleaned_df.drop_duplicates(inplace= True)

    cleaned_df["daily_return"] = cleaned_df["close"].pct_change()
    cleaned_df["sma_5"] = cleaned_df["close"].rolling(window= 5). mean()
    cleaned_df["sma_20"] = cleaned_df["close"].rolling(20).mean()
    cleaned_df["ema_20"] = cleaned_df["close"].ewm(span=20).mean()

    delta = cleaned_df["close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    cleaned_df["rsi"] = 100 - (100 / (1 + rs))

    return cleaned_df

if __name__ == "__main__":
    from ingestion.market_api_client import fetch_market_data

    raw_data = fetch_market_data("AAPL")
    cleaned_data = clean_market_data(raw_data, "AAPL")

    print(cleaned_data.head(10))