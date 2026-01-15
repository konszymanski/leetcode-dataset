import pandas as pd


def big_countries(world: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]
