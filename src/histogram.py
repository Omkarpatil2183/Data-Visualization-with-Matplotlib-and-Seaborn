import seaborn as sns
import matplotlib.pyplot as plt

def create_histogram(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Confirmed'], bins=10, kde=True, color='blue')
    plt.title('Distribution of Confirmed COVID-19 Cases')
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
