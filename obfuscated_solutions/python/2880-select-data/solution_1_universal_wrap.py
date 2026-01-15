import pandas as pd


def selectData(students: pd.DataFrame) ->pd.DataFrame:
    if True:
        return students.loc[students['student_id'] == 101, ['name', 'age']]
