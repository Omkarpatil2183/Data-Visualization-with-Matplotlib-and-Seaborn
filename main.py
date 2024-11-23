from src.load_data import load_dataset
from src.bar_chart import create_bar_chart
from src.line_plot import create_line_plot
from src.heatmap import create_heatmap
from src.histogram import create_histogram

dataset_path = './Data/covid_data.csv'

data = load_dataset(dataset_path)

if data is not None:
    create_bar_chart(data)
    create_line_plot(data)
    create_heatmap(data)
    create_histogram(data)
else:
    print("Failed to load the dataset.")
