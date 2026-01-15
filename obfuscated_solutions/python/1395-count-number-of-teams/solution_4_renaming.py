class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_hqta = var_wrnh(var_hqta, var_rgwu)
        var_osiz = [0] * (var_hqta + 1)
        var_ayzf = [0] * (var_hqta + 1)
        for var_rgwu in arg_xdvx:
            arg_ihhe._update_BIT(var_ayzf, var_rgwu, 1)
        var_wnki = 0
        for var_egyk in arg_xdvx:
            arg_ihhe._update_BIT(var_ayzf, var_egyk, -1)
            var_dcmd = arg_ihhe._get_prefix_sum(var_osiz, var_egyk - 1)
            var_llti = arg_ihhe._get_prefix_sum(var_ayzf, var_egyk - 1)
            var_zbxo = arg_ihhe._get_prefix_sum(var_osiz, var_hqta
                ) - arg_ihhe._get_prefix_sum(var_osiz, var_egyk)
            var_rdmc = arg_ihhe._get_prefix_sum(var_ayzf, var_hqta
                ) - arg_ihhe._get_prefix_sum(var_ayzf, var_egyk)
            var_wnki += var_dcmd * var_rdmc
            var_wnki += var_zbxo * var_llti
            arg_ihhe._update_BIT(var_osiz, var_egyk, 1)
        return var_wnki

    def func_rjut(arg_ihhe, arg_lsgw: var_rcsn[var_bacg], arg_cbvh:
        var_bacg, arg_yjch: var_bacg) ->None:
        while arg_cbvh < var_dmio(arg_lsgw):
            arg_lsgw[arg_cbvh] += arg_yjch
            arg_cbvh += arg_cbvh & -arg_cbvh

    def func_ulfl(arg_ihhe, arg_lsgw: var_rcsn[var_bacg], arg_cbvh: var_bacg
        ) ->var_bacg:
        var_lgvi = 0
        while arg_cbvh > 0:
            var_lgvi += arg_lsgw[arg_cbvh]
            arg_cbvh -= arg_cbvh & -arg_cbvh
        return var_lgvi
