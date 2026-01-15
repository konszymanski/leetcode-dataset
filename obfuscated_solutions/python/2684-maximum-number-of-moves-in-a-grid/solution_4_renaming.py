class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = [([0] * 2) for var_ayzf in var_wnki(var_hqta)]
        for var_egyk in var_wnki(var_hqta):
            var_osiz[var_egyk][0] = 1
        var_dcmd = 0
        for var_llti in var_wnki(1, var_rgwu):
            for var_egyk in var_wnki(var_hqta):
                if arg_xdvx[var_egyk][var_llti] > arg_xdvx[var_egyk][
                    var_llti - 1] and var_osiz[var_egyk][0] > 0:
                    var_osiz[var_egyk][1] = var_zbxo(var_osiz[var_egyk][1],
                        var_osiz[var_egyk][0] + 1)
                if var_egyk - 1 >= 0 and arg_xdvx[var_egyk][var_llti
                    ] > arg_xdvx[var_egyk - 1][var_llti - 1] and var_osiz[
                    var_egyk - 1][0] > 0:
                    var_osiz[var_egyk][1] = var_zbxo(var_osiz[var_egyk][1],
                        var_osiz[var_egyk - 1][0] + 1)
                if var_egyk + 1 < var_hqta and arg_xdvx[var_egyk][var_llti
                    ] > arg_xdvx[var_egyk + 1][var_llti - 1] and var_osiz[
                    var_egyk + 1][0] > 0:
                    var_osiz[var_egyk][1] = var_zbxo(var_osiz[var_egyk][1],
                        var_osiz[var_egyk + 1][0] + 1)
                var_dcmd = var_zbxo(var_dcmd, var_osiz[var_egyk][1] - 1)
            for var_rdmc in var_wnki(var_hqta):
                var_osiz[var_rdmc][0] = var_osiz[var_rdmc][1]
                var_osiz[var_rdmc][1] = 0
        return var_dcmd
