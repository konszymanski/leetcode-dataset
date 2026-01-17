import pandas as pd
​
def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v2_214['timestamp'] = v2_214.v5_381(lambda v6_350: v6_350.v7_328 *  - 1 if v6_350.v8_242 == 'start' else v6_350.v7_328, v9_854=1)
    v10_204 = v2_214.v11_792(['machine_id', 'process_id'], v12_858=False)['timestamp'].sum()
    v13_658 = v10_204.v11_792(['machine_id'], v12_858=False)['timestamp'].v14_189().round(3).v15_704(v16_532 = {'timestamp': 'processing_time'})
    return v13_658
