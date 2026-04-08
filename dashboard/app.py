import requests
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Page setup
st.set_page_config(
    page_title="Market Data Dashboard",
    layout="wide"
)

st.title("Market Data Dashboard")
st.subheader("Live Stock Price Analytics Dashboard")


# Search box
ticker = st.text_input(
    "Enter Stock Ticker (Yahoo Finance symbol)",
    value="AAPL"
)

period = st.selectbox(
    "Select Time Period",
    ["1mo", "3mo", "6mo", "1y", "5y"],
    index=0
)


# Fetch data from FastAPI
try:
    response = requests.get(
        f"http://127.0.0.1:8000/live-data?symbol={ticker}&period={period}"
    )

    response.raise_for_status()


    # Save last searched ticker
    with open("last_search.txt", "w") as file:
        file.write(ticker)

    data = response.json()["data"]

    df = pd.DataFrame(data)


    # Convert date column
    df["date"] = pd.to_datetime(df["date"], utc=True)
    df["date"] = df["date"].dt.tz_localize(None)

    st.success(f"Connected to FastAPI backend | Live data for {ticker}")

    
    # KPI metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", len(df))
    col2.metric("Average Close", round(df["close"].mean(), 2))
    col3.metric("Latest Close", round(df["close"].iloc[-1], 2))

    
    # Show data table
    st.subheader("Live Market Data")
    st.dataframe(df)

    
    # Closing price trend    
    st.subheader("Closing Price Trend")

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["date"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
                name=ticker
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)

    fig_volume = go.Figure()

    fig_volume.add_trace(
        go.Bar(
            x=df["date"],
            y=df["volume"],
            name="Volume"
        )
    )

    st.plotly_chart(fig_volume, use_container_width=True)

    # SMA Trend
    st.subheader("SMA 5 Trend")

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["sma_5"],
            mode="lines",
            name=f"{ticker} SMA 5"
        )
    )

    st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"Error fetching data: {e}")