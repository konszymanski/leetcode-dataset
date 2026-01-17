import pandas as pd

def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v5_381 = v2_214[(v2_214['low_fats'] == 'Y') & (v2_214['recyclable'] == 'Y')]
    v5_381 = v5_381[['product_id']]
    return v5_381