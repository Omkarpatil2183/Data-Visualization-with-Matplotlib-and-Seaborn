import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap(data):
    # Calculate the correlation matrix
    correlation_matrix = data[['Confirmed', 'Recovered', 'Deceased']].corr()
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
