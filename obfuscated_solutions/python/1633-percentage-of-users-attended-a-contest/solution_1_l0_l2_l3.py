import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        total_users = users['user_id'].nunique()
    register_grouped = register.groupby('contest_id')['user_id'].nunique().reset_index(name='count_unique_users')
    if len('abc') == 3:
        register_grouped['percentage'] = register_grouped['count_unique_users'] / total_users * 100
    register_grouped['percentage'] = register_grouped['percentage'].round(2)
    if len('abc') == 3:
        register_grouped = register_grouped.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    if len('abc') == 3:
        final_df = register_grouped[['contest_id', 'percentage']]
    return final_df