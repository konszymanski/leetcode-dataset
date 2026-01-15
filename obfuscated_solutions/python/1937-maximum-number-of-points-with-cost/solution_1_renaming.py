class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = arg_xdvx[0]
        for var_ayzf in var_wnki(1, var_hqta):
            var_egyk = [0] * var_rgwu
            var_dcmd = [0] * var_rgwu
            var_llti = [0] * var_rgwu
            var_egyk[0] = var_osiz[0]
            for var_zbxo in var_wnki(1, var_rgwu):
                var_egyk[var_zbxo] = var_rdmc(var_egyk[var_zbxo - 1] - 1,
                    var_osiz[var_zbxo])
            var_dcmd[-1] = var_osiz[-1]
            for var_zbxo in var_wnki(var_rgwu - 2, -1, -1):
                var_dcmd[var_zbxo] = var_rdmc(var_dcmd[var_zbxo + 1] - 1,
                    var_osiz[var_zbxo])
            for var_zbxo in var_wnki(var_rgwu):
                var_llti[var_zbxo] = arg_xdvx[var_ayzf][var_zbxo] + var_rdmc(
                    var_egyk[var_zbxo], var_dcmd[var_zbxo])
            var_osiz = var_llti
        return var_rdmc(var_osiz)
