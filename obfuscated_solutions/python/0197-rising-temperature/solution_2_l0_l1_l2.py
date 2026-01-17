import pandas as pd

def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v2_214['recordDate'] = v3_125.v5_381(v2_214['recordDate'])
    v2_214.v6_350('recordDate', v7_328=True)
    v2_214['PreviousTemperature'] = v2_214['temperature'].v8_242(1)
    v2_214['PreviousRecordDate'] = v2_214['recordDate'].v8_242(1)
    v9_854 = v2_214[(v2_214['temperature'] > v2_214['PreviousTemperature']) & (v2_214['recordDate'] == v2_214['PreviousRecordDate'] + v3_125.v10_204(v11_792=1))][['id']].v12_858(v13_658={'id': 'Id'})
    return v9_854