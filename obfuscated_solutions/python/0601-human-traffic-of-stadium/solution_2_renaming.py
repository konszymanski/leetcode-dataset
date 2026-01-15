def func_udax(arg_ihhe: var_xdvx.DataFrame) ->var_xdvx.DataFrame:
    arg_ihhe = arg_ihhe[arg_ihhe['people'] >= 100]
    arg_ihhe['rnk'] = var_rcsn(var_bacg(arg_ihhe))
    arg_ihhe['island'] = arg_ihhe.id - arg_ihhe.rnk
    arg_ihhe['island_cnt'] = arg_ihhe.groupby(['island'], as_index=False
        ).id.transform('count')
    return arg_ihhe[arg_ihhe['island_cnt'] >= 3][['id', 'visit_date', 'people']
        ].sort_values(by='visit_date')
