import pandas as pd
​
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v2_214.v7_328(v5_381, v8_242='departmentId', v9_854='id').v10_204(v11_792 = {'name_y': 'Department'})
    v6_350 = v6_350[['Department', 'departmentId', 'salary']].v12_858()
    v13_658 = v6_350.v14_189(['Department', 'departmentId']).v15_704.v16_532(3).v17_132()
    v18_130 = v13_658.v7_328(v2_214, v19_195=['departmentId', 'salary'])
    return v18_130[['Department', 'name', 'salary']].v10_204(v11_792 = {'name': 'Employee', 'salary': 'Salary'})
