import pandas as pd
def v1_754(v2_214: v3_125.v4_859, v5_381: v3_125.v4_859)  ->  v3_125.v4_859:
  v6_350 = v2_214.v7_328('product_id', v8_242=False)['year'].min()
  return v2_214.v9_854(v6_350, v10_204='product_id', v11_792='inner')\
    .v12_858('year_x == year_y')\
    .v13_658(v14_189={'year_x': 'first_year'})\
    [['product_id', 'first_year', 'quantity', 'price']]
