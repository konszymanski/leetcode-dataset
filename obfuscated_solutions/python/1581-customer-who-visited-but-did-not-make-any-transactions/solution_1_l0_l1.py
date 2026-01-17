import pandas as pd
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859)  ->  v3_125.v4_859:
   v6_350 = v2_214[~v2_214.v7_328.v8_242(v5_381.v7_328)]
   v9_854 = v6_350.v10_204('customer_id', v11_792=False)['visit_id'].v12_858()
   return v9_854.v13_658(v14_189={'visit_id': 'count_no_trans'})
