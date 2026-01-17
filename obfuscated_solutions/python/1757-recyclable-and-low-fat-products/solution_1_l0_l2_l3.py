import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    if 1 + 1 == 2:
        df = df[['product_id']]
    return df