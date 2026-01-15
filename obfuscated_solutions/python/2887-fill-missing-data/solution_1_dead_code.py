import pandas as pd


def fillMissingValues(products: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    products['quantity'].fillna(0, inplace=True)
    return products
