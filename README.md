Market Data ETL Dashboard--
This project fetches live stock market data from Yahoo Finance, performs data cleaning and feature engineering, stores the processed data in a local SQL database, exposes the data through a FastAPI backend and visualizes insights through an interactive Streamlit dashboard.
The application supports dynamic stock search, technical indicators, candlestick charts, trend analysis and backend API documentation using Swagger UI.


Why I Chose This as My First Project--
I chose this as my first portfolio project because it combines multiple industry-relevant skills into one practical system. Financial market data is one of the most common real-world use cases for data engineering, backend development, analytics dashboards, and machine learning workflows. By building this project, I wanted to learn how data flows through a complete production-style pipeline:
raw market data → cleaning → storage → API → dashboard visualization
This project helped me understand how real applications are structured beyond just notebooks and isolated scripts. It also allowed me to work on a domain that is widely used in quantitative finance, trading systems, investment analytics, and fintech products.
My goal was to build something that reflects real software engineering practices while also being visually presentable as a portfolio project.


Project Overview--

1. This project is designed as an end-to-end ETL and analytics system for stock market data.
2. The workflow follows this pipeline:
3. Extract live stock market data from Yahoo Finance
4. Transform and clean the raw data
5. Compute technical indicators
6. Store processed data in SQLite
7. Serve data through FastAPI REST endpoints
8. Display analytics in Streamlit
9. This architecture mirrors how data products are built in real-world data teams.


Features--

1. Live Stock Search: Users can search any valid Yahoo Finance stock ticker symbol such as AAPL, TSLA, MSFT, NVDA, GOOGL, INFY.NS , etc. The dashboard dynamically updates based on the selected stock.
2. ETL Pipeline: Built a structured ETL pipeline consisting of ingestion layer, transformation layer, storage layer, scheduling layer, API layer and frontend dashboard.
3. Data Cleaning & Feature Engineering: The transformation pipeline performs operations like date formatting, duplicate removal, null handling, daily return calculation, SMA (Simple Moving Average), EMA (Exponential Moving Average) and RSI (Relative Strength Index).
4. Database Storage: Processed market data is stored inside SQLite for persistent querying and backend serving.
5. REST API Backend: Built using FastAPI with fully documented endpoints.Available endpoints include /, /health, /data, /summary and /live-data. Swagger documentation available at /docs.
6. Interactive Dashboard: Built a Streamlit dashboard Including stock search bar, time period selector, KPI metrics, live market data table, candlestick chart, volume chart, moving average trend charts and technical indicators.


TechStack--

Python, 
Pandas, 
NumPy, 
FastAPI, 
Streamlit, 
SQLite, 
SQLAlchemy, 
Plotly, 
yfinance, 
APScheduler 


How To Run--

Run back-end API: uvicorn api.main:app --reload

Run Streamlit dashboard: streamlit run dashboard/app.py


What I Learned--

Through this project, I learned:
1. ETL pipeline design
2. API development
3. backend/frontend integration
4. SQL-based storage
5. real-time financial data processing
6. dashboard design
7. production-style folder structuring

This project was a major step in moving from notebook-based coding to application-level development.
