from typing import List


class Solution:
    var_udax = var_ihhe(2000000000.0)

    def func_xdvx(arg_rcsn, arg_bacg: var_ihhe, arg_hqta: var_ayzf[var_ayzf
        [var_ihhe]], arg_rgwu: var_ihhe, arg_wrnh: var_ihhe, arg_osiz: var_ihhe
        ) ->var_ayzf[var_ayzf[var_ihhe]]:
        var_wnki = arg_rcsn.run_dijkstra(arg_hqta, arg_bacg, arg_rgwu, arg_wrnh
            )
        if var_wnki < arg_osiz:
            return []
        var_egyk = var_wnki == arg_osiz
        for var_dcmd in arg_hqta:
            if var_dcmd[2] > 0:
                continue
            var_dcmd[2] = arg_rcsn.INF if var_egyk else 1
            if not var_egyk:
                var_llti = arg_rcsn.run_dijkstra(arg_hqta, arg_bacg,
                    arg_rgwu, arg_wrnh)
                if var_llti <= arg_osiz:
                    var_egyk = True
                    var_dcmd[2] += arg_osiz - var_llti
        return arg_hqta if var_egyk else []

    def func_zbxo(arg_rcsn, arg_hqta: var_ayzf[var_ayzf[var_ihhe]],
        arg_bacg: var_ihhe, arg_rgwu: var_ihhe, arg_wrnh: var_ihhe) ->var_ihhe:
        var_rdmc = [([arg_rcsn.INF] * arg_bacg) for var_rjut in var_lsgw(
            arg_bacg)]
        var_cbvh = [arg_rcsn.INF] * arg_bacg
        var_yjch = [False] * arg_bacg
        var_cbvh[arg_rgwu] = 0
        for var_dmio, var_ulfl, var_lgvi in arg_hqta:
            if var_lgvi != -1:
                var_rdmc[var_dmio][var_ulfl] = var_lgvi
                var_rdmc[var_ulfl][var_dmio] = var_lgvi
        for var_rjut in var_lsgw(arg_bacg):
            var_wvuc = -1
            for var_tufr in var_lsgw(arg_bacg):
                if not var_yjch[var_tufr] and (var_wvuc == -1 or var_cbvh[
                    var_tufr] < var_cbvh[var_wvuc]):
                    var_wvuc = var_tufr
            var_yjch[var_wvuc] = True
            for var_xhfo in var_lsgw(arg_bacg):
                var_cbvh[var_xhfo] = var_miuw(var_cbvh[var_xhfo], var_cbvh[
                    var_wvuc] + var_rdmc[var_wvuc][var_xhfo])
        return var_cbvh[arg_wrnh]
