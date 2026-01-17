import pandas as pd

def v1_448(v2_384: v3_259.v4_320, v5_881: v3_259.v4_320) -> v3_259.v4_320:
    v6_444 = v2_384.v7_204(v5_881, v8_194='visit_id', v9_489='left')
    v6_444 = v6_444[v6_444.v10_199.v11_467()]
    v12_967 = v6_444.v13_452('customer_id', v14_718=False)['visit_id'].v15_370()
    return v12_967.v16_926(v17_144={'visit_id': 'count_no_trans'})