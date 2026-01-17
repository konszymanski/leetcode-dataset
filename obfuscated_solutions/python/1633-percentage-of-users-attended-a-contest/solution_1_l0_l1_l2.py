import pandas as pd

def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v2_214['user_id'].v7_328()
    v8_242 = v5_381.v9_854('contest_id')['user_id'].v7_328().v10_204(v11_792='count_unique_users')
    v8_242['percentage'] = v8_242['count_unique_users'] / v6_350 * 100
    v8_242['percentage'] = v8_242['percentage'].round(2)
    v8_242 = v8_242.v12_858(v13_658=['percentage', 'contest_id'], v14_189=[False, True])
    v15_704 = v8_242[['contest_id', 'percentage']]
    return v15_704