import seaborn as sns
import matplotlib.pyplot as plt

def create_bar_chart(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data['Date'], y=data['Confirmed'], color='blue')
    plt.title('Confirmed COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
