import pandas as pd
file_path = 'C:/2016.csv' 
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month'] = df['Date'].dt.month
monthly_aggregation = df.drop(columns=['Date', 'Unnamed: 1']).groupby('Month').sum()
most_popular_month = monthly_aggregation.sum(axis=1).idxmax()
print(f"Most popular month: {most_popular_month}")