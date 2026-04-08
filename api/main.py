from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from fastapi.encoders import jsonable_encoder
from ingestion.market_api_client import fetch_market_data
from transformation.market_cleaner import clean_market_data

import pandas as pd

app = FastAPI(
    title= "Market Data API",
    description= "API for serving stored stock market data",
    version= "1.0.0"
)


DATABASE_URL = "sqlite:///market_data.db"
engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {
        "message": "Market Data API is running successfully",
        "status": "healthy"
        }

@app.get("/data")
def get_market_data(limit: int = 10):
    try:
        query = f"SELECT * FROM market_prices LIMIT {limit}"
        df = pd.read_sql(query, engine)

        df = df.fillna(0)

        records = df.to_dict(orient="records")

        return {
            "rows_returned": len(records),
            "data": records
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/summary")
def get_summary():
    try:
        query = """
        SELECT
            symbol,
            COUNT(*) as total_records,
            AVG(close) as avg_close,
            MIN(close) as min_close,
            MAX(close) as max_close
        FROM market_prices
        GROUP BY symbol
        """

        df = pd.read_sql(query, engine)

        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/live-data")
def get_live_data(symbol: str, period: str = "1mo"):
    try:
        raw_data = fetch_market_data(symbol, period=period)
        cleaned_data = clean_market_data(raw_data, symbol)

        cleaned_data = cleaned_data.fillna(0)

        return {
            "symbol": symbol,
            "rows_returned": len(cleaned_data),
            "data": cleaned_data.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/health")
def health_check():
    try:
        query = "SELECT COUNT(*) as total_rows FROM market_prices"
        df = pd.read_sql(query, engine)

        return {
            "status": "healthy",
            "database_connected": True,
            "total_rows": int(df["total_rows"][0])
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database_connected": False,
            "error": str(e)
        }