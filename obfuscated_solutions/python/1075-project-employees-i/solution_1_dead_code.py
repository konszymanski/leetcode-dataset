import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame
    ) ->pd.DataFrame:
    df = project.merge(employee, on='employee_id')
    udaxi = 32 * 2
    df = df.groupby('project_id', as_index=False)['experience_years'].mean()
    return df.rename(columns={'experience_years': 'average_years'}).round(2)
