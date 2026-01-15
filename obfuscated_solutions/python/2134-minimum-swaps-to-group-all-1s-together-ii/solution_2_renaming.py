class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = arg_ihhe.min_swaps_helper(arg_xdvx, 0)
        var_rgwu = arg_ihhe.min_swaps_helper(arg_xdvx, 1)
        return var_wrnh(var_hqta, var_rgwu)

    def func_osiz(arg_ihhe, arg_ayzf: var_rcsn[var_bacg], arg_wnki: var_bacg
        ) ->var_bacg:
        var_egyk = var_dcmd(arg_ayzf)
        var_llti = 0
        for var_zbxo in var_rdmc(var_egyk - 1, -1, -1):
            if arg_ayzf[var_zbxo] == arg_wnki:
                var_llti += 1
        if var_llti == 0 or var_llti == var_egyk:
            return 0
        var_rjut = 0
        var_lsgw = 0
        var_cbvh = 0
        var_yjch = 0
        while var_lsgw < var_llti:
            if arg_ayzf[var_lsgw] == arg_wnki:
                var_yjch += 1
            var_lsgw += 1
        var_cbvh = var_dmio(var_cbvh, var_yjch)
        while var_lsgw < var_egyk:
            if arg_ayzf[var_rjut] == arg_wnki:
                var_yjch -= 1
            var_rjut += 1
            if arg_ayzf[var_lsgw] == arg_wnki:
                var_yjch += 1
            var_lsgw += 1
            var_cbvh = var_dmio(var_cbvh, var_yjch)
        return var_llti - var_cbvh
