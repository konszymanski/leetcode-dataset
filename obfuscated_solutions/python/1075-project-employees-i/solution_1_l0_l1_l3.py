import pandas as pd

def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v2_214.v7_328(v5_381, v8_242='employee_id')
    v6_350 = v6_350.v9_854('project_id', v10_204=False)['experience_years'].v11_792()
    return v6_350.v12_858(v13_658={'experience_years': 'average_years'}).round(2)