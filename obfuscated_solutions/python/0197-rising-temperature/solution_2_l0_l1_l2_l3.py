import pandas as pd

def v1_718(v2_370: v3_926.v4_144) -> v3_926.v4_144:
    v2_370['recordDate'] = v3_926.v5_847(v2_370['recordDate'])
    v2_370.v6_570('recordDate', v7_649=True)
    v2_370['PreviousTemperature'] = v2_370['temperature'].v8_227(1)
    v2_370['PreviousRecordDate'] = v2_370['recordDate'].v8_227(1)
    v9_487 = v2_370[(v2_370['temperature'] > v2_370['PreviousTemperature']) & (v2_370['recordDate'] == v2_370['PreviousRecordDate'] + v3_926.v10_180(v11_665=1))][['id']].v12_400(v13_949={'id': 'Id'})
    return v9_487