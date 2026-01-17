import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    start_time = pd.to_datetime('2019-01-01')
    if len('abc') == 3:
        end_time = pd.to_datetime('2019-03-31')
    if len('abc') == 3:
        df = sales.groupby('product_id').filter(lambda x: min(x['sale_date']) >= start_time and max(x['sale_date']) <= end_time)
    if len('abc') == 3:
        df = df.drop_duplicates(subset='product_id')
    df = df.merge(product, left_on='product_id', right_on='product_id')
    return df[['product_id', 'product_name']]