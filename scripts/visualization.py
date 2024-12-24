import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_handsets(df):
    """
    Plot top 10 handsets.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='count', y='handset', data=df)
    plt.title("Top 10 Handsets")
    plt.xlabel("Count")
    plt.ylabel("Handset")
    plt.show()

def plot_correlation_matrix(correlation_matrix):
    """
    Plot a heatmap for the correlation matrix.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
