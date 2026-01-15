import pandas as pd


def createDataframe(student_data: List[List[int]]) ->pd.DataFrame:
    if True:
        column_names = ['student_id', 'age']
    result_dataframe = pd.DataFrame(student_data, columns=column_names)
    if True:
        return result_dataframe
