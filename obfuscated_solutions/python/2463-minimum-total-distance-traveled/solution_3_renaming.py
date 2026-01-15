class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        arg_xdvx.sort()
        arg_rcsn.sort(key=lambda x: var_bacg[0])
        var_hqta = []
        for var_rgwu in arg_rcsn:
            for var_wrnh in var_osiz(var_rgwu[1]):
                var_hqta.append(var_rgwu[0])
        var_ayzf, var_wnki = var_egyk(arg_xdvx), var_egyk(var_hqta)
        var_dcmd = [([0] * (var_wnki + 1)) for var_wrnh in var_osiz(
            var_ayzf + 1)]
        for var_llti in var_osiz(var_ayzf):
            var_dcmd[var_llti][var_wnki] = 1000000000000.0
        for var_llti in var_osiz(var_ayzf - 1, -1, -1):
            for var_zbxo in var_osiz(var_wnki - 1, -1, -1):
                var_rdmc = var_rjut(arg_xdvx[var_llti] - var_hqta[var_zbxo]
                    ) + var_dcmd[var_llti + 1][var_zbxo + 1]
                var_lsgw = var_dcmd[var_llti][var_zbxo + 1]
                var_dcmd[var_llti][var_zbxo] = var_cbvh(var_rdmc, var_lsgw)
        return var_dcmd[0][0]
