import pandas as pd

def v1_818(v2_658: v3_529.v4_325) -> v3_529.v4_325:
    v5_559 = v2_658[(v2_658['low_fats'] == 'Y') & (v2_658['recyclable'] == 'Y')]
    v5_559 = v5_559[['product_id']]
    return v5_559