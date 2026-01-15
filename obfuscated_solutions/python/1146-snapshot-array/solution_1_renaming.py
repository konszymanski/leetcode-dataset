class SnapshotArray:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.id = 0
        arg_ihhe.history_records = [[[0, 0]] for var_bacg in var_hqta(arg_xdvx)
            ]

    def func_rgwu(arg_ihhe, arg_wrnh: var_rcsn, arg_osiz: var_rcsn) ->None:
        arg_ihhe.history_records[arg_wrnh].append([arg_ihhe.id, arg_osiz])

    def func_ayzf(arg_ihhe) ->var_rcsn:
        arg_ihhe.id += 1
        return arg_ihhe.id - 1

    def func_wnki(arg_ihhe, arg_wrnh: var_rcsn, arg_egyk: var_rcsn) ->var_rcsn:
        var_dcmd = var_llti.bisect_right(arg_ihhe.history_records[arg_wrnh],
            [arg_egyk, 10 ** 9])
        return arg_ihhe.history_records[arg_wrnh][var_dcmd - 1][1]
