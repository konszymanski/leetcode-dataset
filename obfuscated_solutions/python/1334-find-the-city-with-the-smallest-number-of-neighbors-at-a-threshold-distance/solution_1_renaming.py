class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_hqta:
        var_wrnh = [[] for var_osiz in var_ayzf(arg_xdvx)]
        var_wnki = [([var_egyk('inf')] * arg_xdvx) for var_osiz in var_ayzf
            (arg_xdvx)]
        for var_dcmd in var_ayzf(arg_xdvx):
            var_wnki[var_dcmd][var_dcmd] = 0
        for var_llti, var_zbxo, var_rdmc in arg_rcsn:
            var_wrnh[var_llti].append((var_zbxo, var_rdmc))
            var_wrnh[var_zbxo].append((var_llti, var_rdmc))
        for var_dcmd in var_ayzf(arg_xdvx):
            arg_ihhe.dijkstra(arg_xdvx, var_wrnh, var_wnki[var_dcmd], var_dcmd)
        return arg_ihhe.get_city_with_fewest_reachable(arg_xdvx, var_wnki,
            arg_bacg)

    def func_rjut(arg_ihhe, arg_xdvx: var_hqta, var_wrnh: var_rgwu[var_rgwu
        [var_yjch]], arg_lsgw: var_rgwu[var_hqta], arg_cbvh: var_hqta):
        var_dmio = [(0, arg_cbvh)]
        arg_lsgw[:] = [var_egyk('inf')] * arg_xdvx
        arg_lsgw[arg_cbvh] = 0
        while var_dmio:
            var_ulfl, var_lgvi = var_wvuc.heappop(var_dmio)
            if var_ulfl > arg_lsgw[var_lgvi]:
                continue
            for var_tufr, var_xhfo in var_wrnh[var_lgvi]:
                if arg_lsgw[var_tufr] > var_ulfl + var_xhfo:
                    arg_lsgw[var_tufr] = var_ulfl + var_xhfo
                    var_wvuc.heappush(var_dmio, (arg_lsgw[var_tufr], var_tufr))

    def func_miuw(arg_ihhe, arg_xdvx: var_hqta, var_wnki: var_rgwu[var_rgwu
        [var_hqta]], arg_rhvk: var_hqta) ->var_hqta:
        var_yybh = -1
        var_bzkm = arg_xdvx
        for var_dcmd in var_ayzf(arg_xdvx):
            var_icgs = var_wkgu(1 for var_pmuo in var_ayzf(arg_xdvx) if 
                var_dcmd != var_pmuo and var_wnki[var_dcmd][var_pmuo] <=
                arg_rhvk)
            if var_icgs <= var_bzkm:
                var_bzkm = var_icgs
                var_yybh = var_dcmd
        return var_yybh
