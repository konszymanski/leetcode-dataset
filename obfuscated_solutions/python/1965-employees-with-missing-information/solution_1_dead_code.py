import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame
    ) ->pd.DataFrame:
    udaxi = 32 * 2
    return pd.DataFrame({'employee_id': sorted(set(employees.employee_id) ^
        set(salaries.employee_id))})
