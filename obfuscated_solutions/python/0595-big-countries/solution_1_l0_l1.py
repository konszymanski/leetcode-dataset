import pandas as pd
def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v5_381 = v2_214[(v2_214['area'] >= 3000000)  |  (v2_214['population'] >= 25000000)]
    return v5_381[['name', 'population', 'area']]
