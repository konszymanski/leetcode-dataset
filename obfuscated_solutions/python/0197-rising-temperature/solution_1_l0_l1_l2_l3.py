import pandas as pd

def v1_847(v2_570: v3_649.v4_227) -> v3_649.v4_227:
    v2_570['recordDate'] = v3_649.v5_487(v2_570['recordDate'])
    v6_180 = v2_570.v7_665()
    v6_180['recordDate'] = v6_180['recordDate'] + v3_649.v8_400(1, v9_949='D')
    v10_743 = v3_649.v11_733(v2_570, v6_180, v12_982='recordDate', v13_470=('_today', '_yesterday'))
    v14_691 = v10_743[v10_743['temperature_today'] > v10_743['temperature_yesterday']][['id_today']].v15_296(v16_821={'id_today': 'Id'})
    return v14_691