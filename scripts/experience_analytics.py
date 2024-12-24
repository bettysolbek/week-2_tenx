import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


def aggregate_experience_metrics(df):
    """
    Aggregate experience metrics per customer.
    """
    experience_metrics = df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',  # Average TCP retransmission
        'Avg RTT DL (ms)': 'mean',  # Average RTT
        'Avg Bearer TP DL (kbps)': 'mean',  # Average throughput
        'Handset Type': 'first'  # Handset type (assumes consistent for each user)
    }).reset_index()

    # Rename columns for clarity
    experience_metrics.rename(columns={
        'TCP DL Retrans. Vol (Bytes)': 'Avg TCP Retrans (Bytes)',
        'Avg RTT DL (ms)': 'Avg RTT (ms)',
        'Avg Bearer TP DL (kbps)': 'Avg Throughput (kbps)',
    }, inplace=True)

    # Handle missing values
    experience_metrics.fillna(experience_metrics.mean(numeric_only=True), inplace=True)

    return experience_metrics


def top_bottom_frequent_values(df, column):
    """
    Compute top 10, bottom 10, and most frequent values for a given column.
    """
    top_10 = df.nlargest(10, column)
    bottom_10 = df.nsmallest(10, column)
    most_frequent = df[column].value_counts().head(10)

    return top_10, bottom_10, most_frequent


def distribution_by_handset(df, metric, title):
    """
    Compute and visualize the distribution of a metric by handset type.
    """
    distribution = df.groupby('Handset Type')[metric].mean().reset_index()

    # Plot distribution
    plt.figure(figsize=(10, 6))
    sns.barplot(x=metric, y='Handset Type', data=distribution.sort_values(metric, ascending=False))
    plt.title(title)
    plt.xlabel(metric)
    plt.ylabel('Handset Type')
    plt.tight_layout()
    plt.show()

    return distribution


def perform_experience_clustering(df, columns, n_clusters=3):
    """
    Perform K-Means clustering on experience metrics.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[columns])

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Experience Cluster'] = kmeans.fit_predict(scaled_data)

    return df, kmeans


def describe_clusters(df, cluster_column):
    """
    Provide a brief description of each cluster.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the clustered data.
    - cluster_column (str): Column name representing the clusters.

    Returns:
    - pd.DataFrame: DataFrame summarizing the mean values for each cluster.
    """
    # Select only numeric columns for aggregation (exclude the cluster_column)
    numeric_df = df.select_dtypes(include='number')
    
    # Drop rows with NaN values or fill them
    numeric_df = numeric_df.dropna()  # Or use numeric_df.fillna(0) if you prefer to fill NaNs

    # Add the cluster column to the numeric data
    numeric_df[cluster_column] = df[cluster_column]

    # Group by the cluster column and calculate the mean
    cluster_description = numeric_df.groupby(cluster_column).mean().reset_index()

    return cluster_description
