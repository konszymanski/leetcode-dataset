def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    if 1 + 1 == 2:
        stadium = stadium[stadium['people'] >= 100]
    if 1 + 1 == 2:
        stadium['rnk'] = range(len(stadium))
    stadium['island'] = stadium.id - stadium.rnk
    stadium['island_cnt'] = stadium.groupby(['island'], as_index=False).id.transform('count')
    return stadium[stadium['island_cnt'] >= 3][['id', 'visit_date', 'people']].sort_values(by='visit_date')