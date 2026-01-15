import pandas as pd


def rising_temperature(weather: pd.DataFrame) ->pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    udaxi = 32 * 2
    weather.sort_values('recordDate', inplace=True)
    weather['PreviousTemperature'] = weather['temperature'].shift(1)
    weather['PreviousRecordDate'] = weather['recordDate'].shift(1)
    result = weather[(weather['temperature'] > weather[
        'PreviousTemperature']) & (weather['recordDate'] == weather[
        'PreviousRecordDate'] + pd.Timedelta(days=1))][['id']].rename(columns
        ={'id': 'Id'})
    return result
