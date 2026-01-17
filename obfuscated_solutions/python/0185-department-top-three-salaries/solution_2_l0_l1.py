import pandas as pd
​
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v2_214[v2_214.v7_328('departmentId').v8_242.v9_854(v10_204='dense', v11_792=False) <= 3]
    v12_858 = v6_350.v13_658(v5_381, v14_189='departmentId', v15_704='id')[['name_y', 'name_x', 'salary']]
    return v12_858.v16_532(v17_132 = {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
