import pandas as pd


def pivotTable(weather: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    ans = weather.pivot(index='month', columns='city', values='temperature')
    return ans
