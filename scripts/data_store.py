import kagglehub
import pandas as pd


def generate_fixture_summary():
    return False
    

def get_teams_dict(path):
    teams_data_file = f"{path}/base_data/teams.csv"
    teams_df = pd.read_csv(teams_data_file)
    teams_dict = dict(zip(teams_df['teamId'], teams_df['name']))
    return teams_dict


def main():
    # load data and create mappings
    # path = kagglehub.dataset_download("excel4soccer/espn-soccer-data")
    path = "/Users/aniketn/.cache/kagglehub/datasets/excel4soccer/espn-soccer-data/versions/70"

    mega_dict = {}
    teams_dict = get_teams_dict(path)
    


if __name__ == "__main__":
    main()



# tasks here
# create one large json where the key is the fixture id, and it has a bunch of attributes corresponding to that fixture
# for this first create a get function for every column/data corresponding to a fixture (as done already for teams_dict)
# then create the mega_dict
# eventually turn each json entry into a large summary string (can use jinja templating for this)
