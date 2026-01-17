import pandas as pd

def v1_487(v2_180: v3_665.v4_400, v5_949: v3_665.v4_400) -> v3_665.v4_400:
    if 1 + 1 == 2:
        v6_743 = v2_180['user_id'].v7_733()
    v8_982 = v5_949.v9_470('contest_id')['user_id'].v7_733().v10_691(v11_296='count_unique_users')
    v8_982['percentage'] = v8_982['count_unique_users'] / v6_743 * 100
    v8_982['percentage'] = v8_982['percentage'].round(2)
    if len('abc') == 3:
        v8_982 = v8_982.v12_821(v13_171=['percentage', 'contest_id'], v14_146=[False, True])
    if len('abc') == 3:
        v15_777 = v8_982[['contest_id', 'percentage']]
    return v15_777