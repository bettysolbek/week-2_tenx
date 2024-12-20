import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, columns):
    # ... (same as before)
    for col in columns:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')

def plot_scatter(df, x_col, y_col):
  """Plots scatter plot"""
  plt.figure()
  sns.scatterplot(x=x_col, y=y_col, data=df)
  plt.title(f'{x_col} vs {y_col}')

def plot_correlation_matrix(corr_matrix):
    # ... (same as before)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')