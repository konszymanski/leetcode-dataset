import pandas as pd
def v1_754(
    v2_214: v3_125.v4_859, v5_381: v3_125.v4_859, v6_350: v3_125.v4_859
) -> v3_125.v4_859:
    v7_328 = v5_381.v8_242("order_date.dt.year == 2019").v9_854(
        v2_214,
        v10_204="buyer_id",
        v11_792="user_id",
        v12_858="right",
    )
    v13_658 = v7_328.v14_189(["user_id", "join_date"]).v15_704.v16_532()
    return v13_658.v17_132().v18_130(
        v19_195={"user_id": "buyer_id", "item_id": "orders_in_2019"}
    )
