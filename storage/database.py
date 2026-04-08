from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///market_data.db"

engine = create_engine(DATABASE_URL)

def save_to_database(df, table_name= "market_prices"):
    df = df.drop_duplicates(subset= ["date", "symbol"])
    
    df.to_sql(
        table_name,
        con= engine,
        if_exists= "append",
        index= False
    )

if __name__ == "__main__":
    from ingestion.market_api_client import fetch_market_data
    from transformation.market_cleaner import clean_market_data

    raw_data = fetch_market_data("AAPL")
    cleaned_data = clean_market_data(raw_data, "AAPL")

    save_to_database(cleaned_data)

    print("Data saved successfully.")