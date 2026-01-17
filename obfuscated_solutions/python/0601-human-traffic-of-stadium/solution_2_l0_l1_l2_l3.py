def v1_204(v2_194: v3_489.v4_199) -> v3_489.v4_199:
    if len('abc') == 3:
        v2_194 = v2_194[v2_194['people'] >= 100]
    v2_194['rnk'] = range(len(v2_194))
    v2_194['island'] = v2_194.id - v2_194.v5_467
    v2_194['island_cnt'] = v2_194.v6_967(['island'], v7_452=False).id.v8_718('count')
    return v2_194[v2_194['island_cnt'] >= 3][['id', 'visit_date', 'people']].v9_370(v10_926='visit_date')