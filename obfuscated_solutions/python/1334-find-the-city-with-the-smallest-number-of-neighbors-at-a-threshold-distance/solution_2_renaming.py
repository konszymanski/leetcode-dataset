class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_hqta:
        var_wrnh = var_hqta(1000000000.0) + 7
        var_osiz = [([var_wrnh] * arg_xdvx) for var_ayzf in var_wnki(arg_xdvx)]
        for var_egyk in var_wnki(arg_xdvx):
            arg_ihhe.bellmanFord(arg_xdvx, arg_rcsn, var_osiz[var_egyk],
                var_egyk)
        return arg_ihhe.getCityWithFewestReachable(arg_xdvx, var_osiz, arg_bacg
            )

    def func_dcmd(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_llti: var_rgwu[var_hqta], arg_zbxo: var_hqta) ->None:
        arg_llti[:] = [var_rdmc('inf')] * arg_xdvx
        arg_llti[arg_zbxo] = 0
        for var_ayzf in var_wnki(arg_xdvx - 1):
            var_rjut = False
            for var_lsgw, var_cbvh, var_yjch in arg_rcsn:
                if arg_llti[var_lsgw] != var_rdmc('inf') and arg_llti[var_lsgw
                    ] + var_yjch < arg_llti[var_cbvh]:
                    arg_llti[var_cbvh] = arg_llti[var_lsgw] + var_yjch
                    var_rjut = True
                if arg_llti[var_cbvh] != var_rdmc('inf') and arg_llti[var_cbvh
                    ] + var_yjch < arg_llti[var_lsgw]:
                    arg_llti[var_lsgw] = arg_llti[var_cbvh] + var_yjch
                    var_rjut = True
            if not var_rjut:
                break

    def func_dmio(arg_ihhe, arg_xdvx: var_hqta, var_osiz: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_hqta:
        var_ulfl = -1
        var_lgvi = arg_xdvx
        for var_egyk in var_wnki(arg_xdvx):
            var_wvuc = 0
            for var_tufr in var_wnki(arg_xdvx):
                if var_egyk == var_tufr:
                    continue
                if var_osiz[var_egyk][var_tufr] <= arg_bacg:
                    var_wvuc += 1
            if var_wvuc <= var_lgvi:
                var_lgvi = var_wvuc
                var_ulfl = var_egyk
        return var_ulfl
