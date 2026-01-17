import pandas as pd
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v3_125.v7_328(v2_214, v5_381, v8_242='personId', v9_854='left')
    v6_350 = v6_350[['firstName', 'lastName', 'city', 'state']]
    return v6_350
