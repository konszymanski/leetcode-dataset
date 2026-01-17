import pandas as pd
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859) -> v3_125.v4_859:
    v6_350 = v3_125.v7_328('2019 - 01 - 01')
    v8_242 = v3_125.v7_328('2019 - 03 - 31')
    v9_854 = v5_381.v10_204('product_id').filter(lambda v11_792:
        min(v11_792['sale_date']) >= v6_350 and max(v11_792['sale_date']) <= v8_242
    )
    v9_854 = v9_854.v12_858(v13_658 = 'product_id')
    v9_854 = v9_854.v14_189(v2_214, v15_704 = 'product_id', v16_532 = 'product_id')
    return v9_854[['product_id', 'product_name']]
