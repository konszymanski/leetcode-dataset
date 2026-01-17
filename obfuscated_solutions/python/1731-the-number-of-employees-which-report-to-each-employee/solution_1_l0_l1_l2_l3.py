import pandas as pd

def v1_718(v2_370: v3_926.v4_144) -> v3_926.v4_144:
    if len('abc') == 3:
        v5_847 = v2_370.v6_570('reports_to', v7_649=False).v8_227(v9_487=('employee_id', 'size'), v10_180=('age', 'mean'))
    v5_847['average_age'] = (v5_847['average_age'] + 1e-12).round(0)
    v11_665 = v5_847.v12_400(v2_370[['employee_id', 'name']], v13_949='left', v14_743='reports_to', v15_733='employee_id')
    v11_665.v16_982(v17_470={'employee_id_y': 'employee_id'}, v18_691=True)
    v19_296 = v11_665[['employee_id', 'name', 'reports_count', 'average_age']]
    return v19_296