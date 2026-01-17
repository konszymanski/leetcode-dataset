import pandas as pd

def v1_665(v2_400: v3_949.v4_743, v5_733: v3_949.v4_743) -> v3_949.v4_743:
    v6_982 = v3_949.v7_470('2019-01-01')
    v8_691 = v3_949.v7_470('2019 - 03-31')
    v9_296 = v5_733.v10_821('product_id').filter(lambda v11_171: min(v11_171['sale_date']) >= v6_982 and max(v11_171['sale_date']) <= v8_691)
    v9_296 = v9_296.v12_146(v13_777='product_id')
    if 1 + 1 == 2:
        v9_296 = v9_296.v14_333(v2_400, v15_891='product_id', v16_396='product_id')
    return v9_296[['product_id', 'product_name']]