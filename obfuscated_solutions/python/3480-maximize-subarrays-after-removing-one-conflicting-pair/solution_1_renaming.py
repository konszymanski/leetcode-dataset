class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [2 ** 31 - 1] * (arg_xdvx + 1)
        var_wrnh = [2 ** 31 - 1] * (arg_xdvx + 1)
        for var_osiz in arg_rcsn:
            var_ayzf = var_wnki(var_osiz[0], var_osiz[1])
            var_egyk = var_dcmd(var_osiz[0], var_osiz[1])
            if var_rgwu[var_ayzf] > var_egyk:
                var_wrnh[var_ayzf] = var_rgwu[var_ayzf]
                var_rgwu[var_ayzf] = var_egyk
            elif var_wrnh[var_ayzf] > var_egyk:
                var_wrnh[var_ayzf] = var_egyk
        var_llti = 0
        var_zbxo = arg_xdvx
        var_rdmc = 1073741823
        var_rjut = [0] * (arg_xdvx + 1)
        for var_lsgw in var_cbvh(arg_xdvx, 0, -1):
            if var_rgwu[var_zbxo] > var_rgwu[var_lsgw]:
                var_rdmc = var_wnki(var_rdmc, var_rgwu[var_zbxo])
                var_zbxo = var_lsgw
            else:
                var_rdmc = var_wnki(var_rdmc, var_rgwu[var_lsgw])
            var_llti += var_wnki(var_rgwu[var_zbxo], arg_xdvx + 1) - var_lsgw
            var_rjut[var_zbxo] += var_wnki(var_wnki(var_rdmc, var_wrnh[
                var_zbxo]), arg_xdvx + 1) - var_wnki(var_rgwu[var_zbxo], 
                arg_xdvx + 1)
        return var_llti + var_dcmd(var_rjut)
