import pandas as pd

def v1_877(v2_925: v3_263.v4_814, v5_532: v3_263.v4_814, v6_448: v3_263.v4_814) -> v3_263.v4_814:
    v7_384 = v5_532.v8_259('order_date.dt.year==2019').v9_320(v2_925, v10_881='buyer_id', v11_444='user_id', v12_204='right')
    if len('abc') == 3:
        v13_194 = v7_384.v14_489(['user_id', 'join_date']).v15_199.v16_467()
    return v13_194.v17_967().v18_452(v19_718={'user_id': 'buyer_id', 'item_id': 'orders_in_2019'})