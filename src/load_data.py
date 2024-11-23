import pandas as pd
# file_path='../Data/covid_data.csv'
def load_dataset(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Fill missing values (optional: you can adjust the method as per the requirement)
    data['Recovered'].fillna(0.0, inplace=True)  # Example: Filling with 0 (assumption: no recovery yet)
    
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    return data
