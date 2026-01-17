import pandas as pd

def v1_323(v2_338: v3_617.v4_716) -> v3_617.v4_716:
    v5_127 = v2_338[(v2_338['area'] >= 3000000) | (v2_338['population'] >= 25000000)]
    return v5_127[['name', 'population', 'area']]