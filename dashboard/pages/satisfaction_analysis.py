import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.data_loading import load_data_using_sqlalchemy
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def display():
    st.title("Satisfaction Analysis")

    # Load Data
    query = "SELECT * FROM xdr_data;"
    connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    df = load_data_using_sqlalchemy(query, connection_string)

    # Plotting
    fig = px.scatter(
        df, x="Engagement Score", y="Experience Score", color="Satisfaction Cluster",
        title="Satisfaction Clusters"
    )
    st.plotly_chart(fig)

    # Top Customers
    st.subheader("Top Satisfied Customers")
    top_customers = df.nlargest(10, 'Satisfaction Score')
    st.dataframe(top_customers)
