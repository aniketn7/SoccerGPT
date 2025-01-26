import kagglehub
import pandas as pd

path = kagglehub.dataset_download("excel4soccer/espn-soccer-data")
data_file = f"{path}/base_data/players.csv"
df = pd.read_csv(data_file)
print(df.head())