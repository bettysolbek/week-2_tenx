import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
    st.title("Experience Analysis")

    # Load Data
    query = "SELECT * FROM xdr_data;"
    connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    df = load_data_using_sqlalchemy(query, connection_string)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    df.groupby("Experience Cluster").mean()[["Avg RTT (ms)", "Avg Throughput (kbps)"]].plot(kind="bar", ax=ax)
    ax.set_title("Experience Metrics by Cluster")
    st.pyplot(fig)
