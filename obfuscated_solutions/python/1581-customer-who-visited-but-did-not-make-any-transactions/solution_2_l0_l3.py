import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        visits_no_trans = visits.merge(transactions, on='visit_id', how='left')
    visits_no_trans = visits_no_trans[visits_no_trans.transaction_id.isna()]
    df = visits_no_trans.groupby('customer_id', as_index=False)['visit_id'].count()
    return df.rename(columns={'visit_id': 'count_no_trans'})