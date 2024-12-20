import pandas as pd
from sklearn.decomposition import PCA

def perform_eda(df):
    # ... (same as before)
    descriptive_stats = df.describe()
    # Add more EDA calculations as needed
    return {'descriptive_stats': descriptive_stats}

def correlation_analysis(df):
    # ... (same as before)
    return df.corr(numeric_only=True)

def perform_pca(df, n_components=2):
    # ... (same as before)
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(df)
    explained_variance_ratio = pca.explained_variance_ratio_
    return {'principal_components': principal_components, 'explained_variance_ratio': explained_variance_ratio}