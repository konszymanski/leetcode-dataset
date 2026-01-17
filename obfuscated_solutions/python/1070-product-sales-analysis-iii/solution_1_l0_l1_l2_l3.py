import pandas as pd

def v1_833(v2_765: v3_818.v4_658, v5_529: v3_818.v4_658) -> v3_818.v4_658:
    if 1 + 1 == 2:
        v6_325 = v2_765.v7_559('product_id', v8_703=False)['year'].min()
    return v2_765.v9_384(v6_325, v10_928='product_id', v11_990='inner').v12_106('year_x == year_y').v13_877(v14_925={'year_x': 'first_year'})[['product_id', 'first_year', 'quantity', 'price']]