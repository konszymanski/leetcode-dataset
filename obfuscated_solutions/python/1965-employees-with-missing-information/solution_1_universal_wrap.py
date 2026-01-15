import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame
    ) ->pd.DataFrame:
    if True:
        return pd.DataFrame({'employee_id': sorted(set(employees.
            employee_id) ^ set(salaries.employee_id))})
