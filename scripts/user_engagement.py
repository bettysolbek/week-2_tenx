import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def aggregate_user_metrics(df):
    """
    Aggregate engagement metrics per user (MSISDN).
    """
    user_engagement = df.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum',  # Total session duration
        'Total DL (Bytes)': 'sum',  # Total download
        'Total UL (Bytes)': 'sum',  # Total upload
    }).reset_index()

    # Add total traffic and convert duration to seconds
    user_engagement['Total Traffic (Bytes)'] = user_engagement['Total DL (Bytes)'] + user_engagement['Total UL (Bytes)']
    user_engagement['Session Duration (s)'] = user_engagement['Dur. (ms)'] / 1000
    return user_engagement


def normalize_metrics(df, columns):
    """
    Normalize specified columns using MinMaxScaler.
    """
    scaler = MinMaxScaler()
    df_normalized = df.copy()
    df_normalized[columns] = scaler.fit_transform(df[columns])
    return df_normalized


def determine_optimal_clusters(df, columns, max_clusters=10):
    """
    Use the elbow method to determine the optimal number of clusters.
    """
    inertia = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df[columns])
        inertia.append(kmeans.inertia_)

    # Plot the elbow method results
    plt.plot(range(1, max_clusters + 1), inertia, marker='o')
    plt.title("Elbow Method for Optimal K")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")
    plt.show()


def cluster_users(df, columns, n_clusters=3):
    """
    Cluster users into engagement groups using K-Means.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Engagement Cluster'] = kmeans.fit_predict(df[columns])
    return df


def calculate_cluster_metrics(df, group_column, metrics):
    """
    Calculate metrics for each cluster.
    """
    cluster_metrics = df.groupby(group_column).agg({
        metrics[0]: ['min', 'max', 'mean', 'sum'],
        metrics[1]: ['min', 'max', 'mean', 'sum'],
    }).reset_index()
    return cluster_metrics


def aggregate_application_usage(df, application_columns):
    """
    Aggregate user total traffic per application.
    """
    application_traffic = df.groupby('MSISDN/Number')[application_columns].sum().reset_index()
    return application_traffic


def plot_top_applications(application_traffic, top_n=3):
    """
    Plot the top N most used applications.
    """
    top_users = application_traffic.set_index('MSISDN/Number').stack().reset_index()
    top_users.columns = ['MSISDN/Number', 'Application', 'Traffic']
    top_users = top_users.sort_values(by='Traffic', ascending=False).groupby('Application').head(top_n)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Application', y='Traffic', data=top_users, ci=None)
    plt.title("Top Applications by Traffic")
    plt.xlabel("Application")
    plt.ylabel("Traffic (Bytes)")
    plt.show()
