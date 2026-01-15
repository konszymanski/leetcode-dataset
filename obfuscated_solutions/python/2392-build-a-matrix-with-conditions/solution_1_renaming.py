class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_rgwu[var_hqta]]) ->var_rgwu[
        var_rgwu[var_hqta]]:
        var_wrnh = arg_ihhe.topo_sort(arg_rcsn, arg_xdvx)
        var_osiz = arg_ihhe.topo_sort(arg_bacg, arg_xdvx)
        if not var_wrnh or not var_osiz:
            return []
        var_ayzf = {var_wnki: var_egyk for var_egyk, var_wnki in var_dcmd(
            var_osiz)}
        var_llti = [([0] * arg_xdvx) for var_zbxo in var_rdmc(arg_xdvx)]
        for var_egyk, var_rjut in var_dcmd(var_wrnh):
            if var_rjut in var_ayzf:
                var_lsgw = var_ayzf[var_rjut]
                var_llti[var_egyk][var_lsgw] = var_rjut
        return var_llti

    def func_cbvh(arg_ihhe, arg_yjch: var_rgwu[var_rgwu[var_hqta]],
        arg_dmio: var_hqta) ->var_rgwu[var_hqta]:
        var_ulfl = [[] for var_zbxo in var_rdmc(arg_dmio + 1)]
        for var_lgvi, var_wvuc in arg_yjch:
            var_ulfl[var_lgvi].append(var_wvuc)
        var_tufr = [0] * (arg_dmio + 1)
        var_xhfo = []
        arg_ihhe.has_cycle = False
        for var_egyk in var_rdmc(1, arg_dmio + 1):
            if var_tufr[var_egyk] == 0:
                arg_ihhe.dfs(var_egyk, var_ulfl, var_tufr, var_xhfo)
                if arg_ihhe.has_cycle:
                    return []
        return var_xhfo[::-1]

    def func_miuw(arg_ihhe, arg_rhvk: var_hqta, var_ulfl: var_rgwu[var_rgwu
        [var_hqta]], var_tufr: var_rgwu[var_hqta], var_xhfo: var_rgwu[var_hqta]
        ):
        var_tufr[arg_rhvk] = 1
        for var_yybh in var_ulfl[arg_rhvk]:
            if var_tufr[var_yybh] == 0:
                arg_ihhe.dfs(var_yybh, var_ulfl, var_tufr, var_xhfo)
                if arg_ihhe.has_cycle:
                    return
            elif var_tufr[var_yybh] == 1:
                arg_ihhe.has_cycle = True
                return
        var_tufr[arg_rhvk] = 2
        var_xhfo.append(arg_rhvk)
