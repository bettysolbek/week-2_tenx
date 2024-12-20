import pandas as pd
import numpy as np

def handle_missing_values(df, strategy='mean'):
    # ... (same as before)
    if strategy == 'mean':
      return df.fillna(df.mean(numeric_only=True))
    elif strategy == 'median':
        return df.fillna(df.median(numeric_only=True))
    # Add other strategies as needed
    return df

def treat_outliers(df):
    # ... (same as before)
    for col in df.select_dtypes(include=np.number):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        upper_bound = Q3 + 1.5 * IQR
        lower_bound = Q1 - 1.5 * IQR
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
    return df

def segment_users(df, column, n_bins=10):
    # ... (same as before)
    df['decile'] = pd.qcut(df[column], q=n_bins, labels=False, duplicates='drop')
    return df