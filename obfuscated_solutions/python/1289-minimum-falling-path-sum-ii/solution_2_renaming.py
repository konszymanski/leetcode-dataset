class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [([var_osiz] * var_hqta) for var_ayzf in var_wnki(var_hqta)]
        for var_egyk in var_wnki(var_hqta):
            var_wrnh[var_hqta - 1][var_egyk] = arg_xdvx[var_hqta - 1][var_egyk]
        for var_dcmd in var_wnki(var_hqta - 2, -1, -1):
            for var_egyk in var_wnki(var_hqta):
                var_llti = var_osiz
                for var_zbxo in var_wnki(var_hqta):
                    if var_zbxo != var_egyk:
                        var_llti = var_rdmc(var_llti, var_wrnh[var_dcmd + 1
                            ][var_zbxo])
                var_wrnh[var_dcmd][var_egyk] = arg_xdvx[var_dcmd][var_egyk
                    ] + var_llti
        var_rjut = var_osiz
        for var_egyk in var_wnki(var_hqta):
            var_rjut = var_rdmc(var_rjut, var_wrnh[0][var_egyk])
        return var_rjut
