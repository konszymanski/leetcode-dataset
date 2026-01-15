import pandas as pd


def selectData(students: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    return students.loc[students['student_id'] == 101, ['name', 'age']]
