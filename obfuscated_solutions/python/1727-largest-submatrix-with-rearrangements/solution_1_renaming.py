class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = 0
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_wrnh):
                if arg_xdvx[var_ayzf][var_egyk] != 0 and var_ayzf > 0:
                    arg_xdvx[var_ayzf][var_egyk] += arg_xdvx[var_ayzf - 1][
                        var_egyk]
            var_dcmd = var_llti(arg_xdvx[var_ayzf], reverse=True)
            for var_zbxo in var_wnki(var_wrnh):
                var_osiz = var_rdmc(var_osiz, var_dcmd[var_zbxo] * (
                    var_zbxo + 1))
        return var_osiz
