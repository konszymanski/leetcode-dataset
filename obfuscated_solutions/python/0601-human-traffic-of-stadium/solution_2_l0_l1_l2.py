def v1_754(v2_214: v3_125.v4_859) -> v3_125.v4_859:
    v2_214 = v2_214[v2_214['people'] >= 100]
    v2_214['rnk'] = range(len(v2_214))
    v2_214['island'] = v2_214.id - v2_214.v5_381
    v2_214['island_cnt'] = v2_214.v6_350(['island'], v7_328=False).id.v8_242('count')
    return v2_214[v2_214['island_cnt'] >= 3][['id', 'visit_date', 'people']].v9_854(v10_204='visit_date')