import pandas as pd

def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v3_125.v7_328(v2_214, v5_381, v8_242='employee_id', v9_854='outer')
    v10_204 = v6_350[v6_350.v11_792().any(v12_858=1)]
    v13_658 = v10_204[['employee_id']].v14_189(v15_704='employee_id')
    return v13_658