import pandas as pd

def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v5_381 = v2_214[v2_214['activity_type'] == 'start']
    v6_350 = v2_214[v2_214['activity_type'] == 'end']
    v7_328 = v6_350.v8_242(v5_381, v9_854=['machine_id', 'process_id'])
    v10_204 = v7_328.v11_792(v12_858=v7_328['timestamp_x'] - v7_328['timestamp_y']).v13_658(['machine_id'], v14_189=False)['processing_time'].v15_704().round(3)
    return v10_204