class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [([var_osiz] * var_hqta) for var_ayzf in var_wnki(var_hqta)]
        var_egyk = None
        var_dcmd = None
        for var_llti in var_wnki(var_hqta):
            var_wrnh[var_hqta - 1][var_llti] = arg_xdvx[var_hqta - 1][var_llti]
            if var_egyk is None or var_wrnh[var_hqta - 1][var_llti
                ] <= var_wrnh[var_hqta - 1][var_egyk]:
                var_dcmd = var_egyk
                var_egyk = var_llti
            elif var_dcmd is None or var_wrnh[var_hqta - 1][var_llti
                ] <= var_wrnh[var_hqta - 1][var_dcmd]:
                var_dcmd = var_llti
        for var_zbxo in var_wnki(var_hqta - 2, -1, -1):
            var_rdmc = None
            var_rjut = None
            for var_llti in var_wnki(var_hqta):
                if var_llti != var_egyk:
                    var_wrnh[var_zbxo][var_llti] = arg_xdvx[var_zbxo][var_llti
                        ] + var_wrnh[var_zbxo + 1][var_egyk]
                else:
                    var_wrnh[var_zbxo][var_llti] = arg_xdvx[var_zbxo][var_llti
                        ] + var_wrnh[var_zbxo + 1][var_dcmd]
                if var_rdmc is None or var_wrnh[var_zbxo][var_llti
                    ] <= var_wrnh[var_zbxo][var_rdmc]:
                    var_rjut = var_rdmc
                    var_rdmc = var_llti
                elif var_rjut is None or var_wrnh[var_zbxo][var_llti
                    ] <= var_wrnh[var_zbxo][var_rjut]:
                    var_rjut = var_llti
            var_egyk = var_rdmc
            var_dcmd = var_rjut
        return var_wrnh[0][var_egyk]
