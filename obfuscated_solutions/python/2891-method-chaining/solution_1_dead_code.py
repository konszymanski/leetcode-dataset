import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    return animals[animals['weight'] > 100].sort_values(by='weight',
        ascending=False)[['name']]
