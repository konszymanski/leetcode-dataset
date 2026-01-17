import pandas as pd
def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v2_214['recordDate'] = v3_125.v5_381(v2_214['recordDate'])
    v6_350 = v2_214.v7_328()
    v6_350['recordDate'] = v6_350['recordDate'] + v3_125.v8_242(1, v9_854='D')
    v10_204 = v3_125.v11_792(v2_214, v6_350, v12_858='recordDate', v13_658=('_today', '_yesterday'))
    v14_189 = v10_204[v10_204['temperature_today'] > v10_204['temperature_yesterday']][['id_today']].v15_704(v16_532={'id_today': 'Id'})
    return v14_189
