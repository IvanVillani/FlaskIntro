import pandas as pd

def get_pokemon_data():
    return pd.read_csv('/Users/I544091/Projects/python/flaskIntro/resources/pokemon_data.csv')

if __name__ == '__main__':
    print(get_pokemon_data())