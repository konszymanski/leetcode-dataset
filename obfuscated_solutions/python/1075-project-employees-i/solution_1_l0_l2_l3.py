import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        df = project.merge(employee, on='employee_id')
    df = df.groupby('project_id', as_index=False)['experience_years'].mean()
    return df.rename(columns={'experience_years': 'average_years'}).round(2)