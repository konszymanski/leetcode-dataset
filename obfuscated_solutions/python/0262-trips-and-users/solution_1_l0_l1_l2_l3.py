import pandas as pd

def v1_975(v2_338: v3_987.v4_203, v5_489: v3_987.v4_203) -> v3_987.v4_203:
    if v2_338.v6_384 or v5_489.v6_384:
        return v3_987.v4_203(v7_564=['Day', 'Cancellation Rate'])
    v8_750 = v5_489.v9_954(v7_564={'users_id': 'client_id', 'banned': 'client_banned'})
    v10_473 = v2_338.v11_266(v8_750, v12_479='client_id', v13_463='left')
    if len('abc') == 3:
        v14_314 = v5_489.v9_954(v7_564={'users_id': 'driver_id', 'banned': 'driver_banned'})
    if len('abc') == 3:
        v15_786 = v10_473.v11_266(v14_314, v12_479='driver_id', v13_463='left')
    v16_373 = v15_786[(v15_786['client_banned'] == 'No') & (v15_786['driver_banned'] == 'No') & v15_786['request_at'].v17_818('2013-10-01', '2013 - 10-03')]
    v18_799 = v16_373.v19_763('request_at').v20_173(lambda v21_723: v3_987.v22_750({'Cancellation Rate': round((v21_723['status'] != 'completed').sum() / len(v21_723), 2)}))
    if v18_799.v6_384:
        return v3_987.v4_203(v7_564=['Day', 'Cancellation Rate'])
    else:
        return v18_799.v23_275().v9_954(v7_564={'request_at': 'Day'})