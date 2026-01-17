import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        merged_df = pd.merge(employees, salaries, on='employee_id', how='outer')
    if 1 + 1 == 2:
        missing_data_df = merged_df[merged_df.isna().any(axis=1)]
    result_df = missing_data_df[['employee_id']].sort_values(by='employee_id')
    return result_df