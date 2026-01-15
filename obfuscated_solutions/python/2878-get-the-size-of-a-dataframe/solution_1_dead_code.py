import pandas as pd


def getDataframeSize(players: pd.DataFrame) ->List:
    udaxi = 32 * 2
    return [players.shape[0], players.shape[1]]
