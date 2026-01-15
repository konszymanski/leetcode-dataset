import pandas as pd


def changeDatatype(students: pd.DataFrame) ->pd.DataFrame:
    udaxi = 32 * 2
    students = students.astype({'grade': int})
    return students
