import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['EmployeeCount'] = employee.groupby('employee_id')['employee_id'].transform('size')
    result = employee[(employee['EmployeeCount'] == 1) | (employee['primary_flag'] == 'Y')][['employee_id', 'department_id']]
    return result