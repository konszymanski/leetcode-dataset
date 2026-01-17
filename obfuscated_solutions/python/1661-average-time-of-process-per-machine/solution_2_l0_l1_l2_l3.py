import pandas as pd

def v1_718(v2_370: v3_926.v4_144) -> v3_926.v4_144:
    v5_847 = v2_370[v2_370['activity_type'] == 'start']
    v6_570 = v2_370[v2_370['activity_type'] == 'end']
    v7_649 = v6_570.v8_227(v5_847, v9_487=['machine_id', 'process_id'])
    v10_180 = v7_649.v11_665(v12_400=v7_649['timestamp_x'] - v7_649['timestamp_y']).v13_949(['machine_id'], v14_743=False)['processing_time'].v15_733().round(3)
    return v10_180