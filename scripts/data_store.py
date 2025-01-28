import kagglehub
import pandas as pd


def generate_fixture_summary():
    return False

def main():
    # load data and create mappings
    path = kagglehub.dataset_download("excel4soccer/espn-soccer-data")
    teams_data_file = f"{path}/base_data/teams.csv"
    teams_df = pd.read_csv(teams_data_file)
    print(teams_df.head())
    teams_dict = dict(zip(teams_df['teamId'], teams_df['name']))
    print(teams_dict)

if __name__ == "__main__":
    main()