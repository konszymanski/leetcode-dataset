import pandas as pd

def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v2_214.v7_328(v5_381, v8_242='visit_id', v9_854='left')
    v6_350 = v6_350[v6_350.v10_204.v11_792()]
    v12_858 = v6_350.v13_658('customer_id', v14_189=False)['visit_id'].v15_704()
    return v12_858.v16_532(v17_132={'visit_id': 'count_no_trans'})