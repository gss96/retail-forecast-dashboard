
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Sales Dashboard", layout="centered")

st.title("🛍️ Retail Sales Forecasting Dashboard")

@st.cache_data
def load_sales_data():
    return pd.read_csv("Walmart_Store_sales.csv", parse_dates=['Date'])

@st.cache_data
def load_forecast():
    return pd.read_csv("forecast_result.csv", parse_dates=['ds'])

sales_df = load_sales_data()
forecast_df = load_forecast()

st.subheader("📈 Daily Revenue Trend")
daily_revenue = sales_df.groupby("Date")["Weekly_Sales"].sum().reset_index()
fig1 = px.line(daily_revenue, x="Date", y="Weekly_Sales", title="Actual Revenue Over Time")
st.plotly_chart(fig1)

st.subheader("🔮 Forecast for Next 30 Days")
fig2 = px.line(forecast_df, x="ds", y="yhat", title="Forecasted Revenue")
fig2.add_scatter(x=forecast_df['ds'], y=forecast_df['yhat_upper'], mode='lines', name='Upper Bound')
fig2.add_scatter(x=forecast_df['ds'], y=forecast_df['yhat_lower'], mode='lines', name='Lower Bound')
st.plotly_chart(fig2)

st.info("This dashboard uses Streamlit, Prophet, Plotly and SQLite-powered ETL pipeline.")
