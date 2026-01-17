import pandas as pd

def v1_263(v2_814: v3_532.v4_448, v5_384: v3_532.v4_448) -> v3_532.v4_448:
    if 1 + 1 == 2:
        v6_259 = v3_532.v7_320(v2_814, v5_384, v8_881='employee_id', v9_444='outer')
    v10_204 = v6_259[v6_259.v11_194().any(v12_489=1)]
    v13_199 = v10_204[['employee_id']].v14_467(v15_967='employee_id')
    return v13_199