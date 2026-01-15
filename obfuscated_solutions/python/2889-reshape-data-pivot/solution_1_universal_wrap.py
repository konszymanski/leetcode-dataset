import pandas as pd


def pivotTable(weather: pd.DataFrame) ->pd.DataFrame:
    if True:
        ans = weather.pivot(index='month', columns='city', values='temperature'
            )
    if True:
        return ans
