class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu, var_wrnh, var_osiz = var_ayzf(arg_xdvx), var_ayzf(
            arg_xdvx[0]), 0, 0
        var_wnki = [(0) for var_egyk in var_dcmd(var_rgwu + 1)]
        for var_llti in var_dcmd(1, var_hqta + 1):
            for var_zbxo in var_dcmd(1, var_rgwu + 1):
                if arg_xdvx[var_llti - 1][var_zbxo - 1] == 1:
                    var_rdmc = var_wnki[var_zbxo]
                    var_wnki[var_zbxo] = 1 + var_rjut(var_osiz, var_rjut(
                        var_wnki[var_zbxo - 1], var_wnki[var_zbxo]))
                    var_osiz = var_rdmc
                    var_wrnh += var_wnki[var_zbxo]
                else:
                    var_wnki[var_zbxo] = 0
        return var_wrnh
