class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_hqta:
        var_wrnh = var_hqta(1000000000.0 + 7)
        var_osiz = [([var_wrnh] * arg_xdvx) for var_ayzf in var_wnki(arg_xdvx)]
        for var_egyk in var_wnki(arg_xdvx):
            var_osiz[var_egyk][var_egyk] = 0
        for var_dcmd, var_llti, var_zbxo in arg_rcsn:
            var_osiz[var_dcmd][var_llti] = var_zbxo
            var_osiz[var_llti][var_dcmd] = var_zbxo
        arg_ihhe.floyd(arg_xdvx, var_osiz)
        return arg_ihhe.get_city_with_fewest_reachable(arg_xdvx, var_osiz,
            arg_bacg)

    def func_rdmc(arg_ihhe, arg_xdvx: var_hqta, var_osiz: var_rgwu[var_rgwu
        [var_hqta]]):
        for var_rjut in var_wnki(arg_xdvx):
            for var_egyk in var_wnki(arg_xdvx):
                for var_lsgw in var_wnki(arg_xdvx):
                    var_osiz[var_egyk][var_lsgw] = var_cbvh(var_osiz[
                        var_egyk][var_lsgw], var_osiz[var_egyk][var_rjut] +
                        var_osiz[var_rjut][var_lsgw])

    def func_yjch(arg_ihhe, arg_xdvx: var_hqta, var_osiz: var_rgwu[var_rgwu
        [var_hqta]], arg_dmio: var_hqta) ->var_hqta:
        var_ulfl = -1
        var_lgvi = arg_xdvx
        for var_egyk in var_wnki(arg_xdvx):
            var_wvuc = var_tufr(1 for var_lsgw in var_wnki(arg_xdvx) if 
                var_egyk != var_lsgw and var_osiz[var_egyk][var_lsgw] <=
                arg_dmio)
            if var_wvuc <= var_lgvi:
                var_lgvi = var_wvuc
                var_ulfl = var_egyk
        return var_ulfl
