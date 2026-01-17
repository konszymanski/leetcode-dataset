import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        students = students.astype({'grade': int})
    return students