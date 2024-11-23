import seaborn as sns
import matplotlib.pyplot as plt

def create_line_plot(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x='Date', y='Confirmed', label='Confirmed', color='blue')
    sns.lineplot(data=data, x='Date', y='Recovered', label='Recovered', color='green')
    sns.lineplot(data=data, x='Date', y='Deceased', label='Deceased', color='red')
    plt.title('COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
