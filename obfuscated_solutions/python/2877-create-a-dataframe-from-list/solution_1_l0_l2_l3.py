import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    if 1 + 1 == 2:
        column_names = ['student_id', 'age']
    if 1 + 1 == 2:
        result_dataframe = pd.DataFrame(student_data, columns=column_names)
    return result_dataframe