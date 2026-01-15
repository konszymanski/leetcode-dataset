class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [0] * var_wrnh
        var_ayzf = 0
        for var_wnki in var_egyk(var_hqta):
            for var_dcmd in var_egyk(var_wrnh):
                var_llti = 0
                var_zbxo = 0
                if var_wnki + 1 < var_hqta:
                    if var_dcmd - 1 >= 0:
                        var_llti += arg_xdvx[var_wnki + 1][var_dcmd - 1]
                        var_zbxo += 1
                    var_llti += arg_xdvx[var_wnki + 1][var_dcmd]
                    var_zbxo += 1
                    if var_dcmd + 1 < var_wrnh:
                        var_llti += arg_xdvx[var_wnki + 1][var_dcmd + 1]
                        var_zbxo += 1
                if var_dcmd + 1 < var_wrnh:
                    var_llti += arg_xdvx[var_wnki][var_dcmd + 1]
                    var_zbxo += 1
                var_llti += arg_xdvx[var_wnki][var_dcmd]
                var_zbxo += 1
                if var_dcmd - 1 >= 0:
                    var_llti += var_osiz[var_dcmd - 1]
                    var_zbxo += 1
                if var_wnki - 1 >= 0:
                    if var_dcmd - 1 >= 0:
                        var_llti += var_ayzf
                        var_zbxo += 1
                    var_llti += var_osiz[var_dcmd]
                    var_zbxo += 1
                    if var_dcmd + 1 < var_wrnh:
                        var_llti += var_osiz[var_dcmd + 1]
                        var_zbxo += 1
                if var_wnki - 1 >= 0:
                    var_ayzf = var_osiz[var_dcmd]
                var_osiz[var_dcmd] = arg_xdvx[var_wnki][var_dcmd]
                arg_xdvx[var_wnki][var_dcmd] = var_llti // var_zbxo
        return arg_xdvx
