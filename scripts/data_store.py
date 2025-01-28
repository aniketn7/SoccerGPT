import kagglehub
import pandas as pd






def generate_fixture_summary():
    return False

def main():
    # load data and create mappings
    path = kagglehub.dataset_download("excel4soccer/espn-soccer-data")
    teams_data_file = f"{path}/base_data/teams.csv"
    df = pd.read_csv(teams_data_file)
    print(df.head())

if __name__ == "__main__":
    main()