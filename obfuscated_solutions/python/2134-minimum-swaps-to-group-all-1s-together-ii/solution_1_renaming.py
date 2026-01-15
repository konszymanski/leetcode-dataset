class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = arg_ihhe.min_swaps_helper(arg_xdvx, 0)
        var_rgwu = arg_ihhe.min_swaps_helper(arg_xdvx, 1)
        return var_wrnh(var_hqta, var_rgwu)

    def func_osiz(arg_ihhe, arg_ayzf: var_rcsn[var_bacg], arg_wnki: var_bacg
        ) ->var_bacg:
        var_egyk = var_dcmd(arg_ayzf)
        var_llti = [0] * (var_egyk + 1)
        for var_zbxo in var_rdmc(var_egyk - 1, -1, -1):
            var_llti[var_zbxo] = var_llti[var_zbxo + 1]
            if arg_ayzf[var_zbxo] == arg_wnki ^ 1:
                var_llti[var_zbxo] += 1
        var_rjut = var_llti[0]
        var_lsgw = 0
        var_cbvh = var_rjut - var_llti[var_egyk - var_rjut]
        for var_zbxo in var_rdmc(var_rjut):
            if arg_ayzf[var_zbxo] == arg_wnki ^ 1:
                var_lsgw += 1
            var_yjch = var_rjut - var_zbxo - 1
            var_dmio = var_zbxo + 1 - var_lsgw + (var_yjch - var_llti[
                var_egyk - var_yjch])
            var_cbvh = var_wrnh(var_cbvh, var_dmio)
        return var_cbvh
