import pandas as pd
import numpy as np
from sklearn.metrics import euclidean_distances
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_engagement_score(df, engagement_columns, reference_cluster):
    """
    Calculate the engagement score as the Euclidean distance to the less engaged cluster.
    """
    reference_point = df[df['Engagement Cluster'] == reference_cluster][engagement_columns].mean().values
    df['Engagement Score'] = euclidean_distances(df[engagement_columns], [reference_point]).flatten()
    return df

def calculate_experience_score(df, experience_columns, reference_cluster):
    """
    Calculate the experience score as the Euclidean distance to the worst experience cluster.
    """
    reference_point = df[df['Experience Cluster'] == reference_cluster][experience_columns].mean().values
    df['Experience Score'] = euclidean_distances(df[experience_columns], [reference_point]).flatten()
    return df

def calculate_satisfaction_score(df):
    """
    Calculate the satisfaction score as the average of engagement and experience scores.
    """
    df['Satisfaction Score'] = df[['Engagement Score', 'Experience Score']].mean(axis=1)
    return df

def top_satisfied_customers(df, n=10):
    """
    Get the top N satisfied customers.
    """
    return df.nlargest(n, 'Satisfaction Score')[['MSISDN/Number', 'Satisfaction Score']]

def train_regression_model(df, features, target):
    """
    Train a regression model to predict satisfaction score.
    """
    model = LinearRegression()
    X = df[features]
    y = df[target]
    model.fit(X, y)
    return model

def cluster_satisfaction_scores(df, columns, n_clusters=2):
    """
    Perform K-Means clustering on engagement and experience scores.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Satisfaction Cluster'] = kmeans.fit_predict(df[columns])
    return df

def aggregate_cluster_scores(df):
    """
    Aggregate average satisfaction and experience scores per cluster.
    """
    return df.groupby('Satisfaction Cluster')[['Satisfaction Score', 'Experience Score']].mean().reset_index()

def export_to_mysql(df, table_name, connection_string):
    """
    Export the final DataFrame to a MySQL database.
    """
    from sqlalchemy import create_engine
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
