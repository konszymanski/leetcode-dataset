class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_osiz[var_osiz
        [var_wrnh]], arg_bacg: var_wrnh, arg_hqta: var_wrnh, arg_rgwu: var_wrnh
        ) ->var_osiz[var_osiz[var_wrnh]]:
        var_ayzf = var_wrnh(2000000000.0)
        var_wnki = [[] for var_egyk in var_dcmd(arg_xdvx)]
        for var_llti, var_zbxo, var_rdmc in arg_rcsn:
            if var_rdmc != -1:
                var_wnki[var_llti].append((var_zbxo, var_rdmc))
                var_wnki[var_zbxo].append((var_llti, var_rdmc))
        var_rjut = arg_ihhe._dijkstra(var_wnki, arg_bacg, arg_hqta)
        if var_rjut < arg_rgwu:
            return []
        if var_rjut == arg_rgwu:
            for var_lsgw in arg_rcsn:
                if var_lsgw[2] == -1:
                    var_lsgw[2] = var_ayzf
            return arg_rcsn
        for var_cbvh, (var_llti, var_zbxo, var_rdmc) in var_yjch(arg_rcsn):
            if var_rdmc != -1:
                continue
            arg_rcsn[var_cbvh][2] = 1
            var_wnki[var_llti].append((var_zbxo, 1))
            var_wnki[var_zbxo].append((var_llti, 1))
            var_dmio = arg_ihhe._dijkstra(var_wnki, arg_bacg, arg_hqta)
            if var_dmio <= arg_rgwu:
                arg_rcsn[var_cbvh][2] += arg_rgwu - var_dmio
                for var_ulfl in var_dcmd(var_cbvh + 1, var_lgvi(arg_rcsn)):
                    if arg_rcsn[var_ulfl][2] == -1:
                        arg_rcsn[var_ulfl][2] = var_ayzf
                return arg_rcsn
        return []

    def func_wvuc(arg_ihhe, var_wnki: var_osiz[var_osiz[var_xhfo[var_wrnh,
        var_wrnh]]], arg_tufr: var_wrnh, arg_hqta: var_wrnh) ->var_wrnh:
        var_miuw = [var_rhvk.inf] * var_lgvi(var_wnki)
        var_miuw[arg_tufr] = 0
        var_yybh = [(0, arg_tufr)]
        while var_yybh:
            var_bzkm, var_llti = var_icgs.heappop(var_yybh)
            if var_bzkm > var_miuw[var_llti]:
                continue
            for var_zbxo, var_rdmc in var_wnki[var_llti]:
                if var_bzkm + var_rdmc < var_miuw[var_zbxo]:
                    var_miuw[var_zbxo] = var_bzkm + var_rdmc
                    var_icgs.heappush(var_yybh, (var_miuw[var_zbxo], var_zbxo))
        return var_miuw[arg_hqta]
