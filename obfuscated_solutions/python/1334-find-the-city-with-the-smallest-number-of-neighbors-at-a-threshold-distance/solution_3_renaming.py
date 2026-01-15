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
            arg_ihhe.spfa(arg_xdvx, var_wrnh, var_wnki[var_dcmd], var_dcmd)
        return arg_ihhe.get_city_with_fewest_reachable(arg_xdvx, var_wnki,
            arg_bacg)

    def func_rjut(arg_ihhe, arg_xdvx: var_hqta, var_wrnh: var_rgwu[var_rgwu
        [var_yjch]], arg_lsgw: var_rgwu[var_hqta], arg_cbvh: var_hqta):
        var_dmio = var_ulfl([arg_cbvh])
        var_lgvi = [0] * arg_xdvx
        arg_lsgw[:] = [var_egyk('inf')] * arg_xdvx
        arg_lsgw[arg_cbvh] = 0
        while var_dmio:
            var_wvuc = var_dmio.popleft()
            for var_tufr, var_xhfo in var_wrnh[var_wvuc]:
                if arg_lsgw[var_tufr] > arg_lsgw[var_wvuc] + var_xhfo:
                    arg_lsgw[var_tufr] = arg_lsgw[var_wvuc] + var_xhfo
                    var_lgvi[var_tufr] += 1
                    var_dmio.append(var_tufr)
                    if var_lgvi[var_tufr] > arg_xdvx:
                        var_miuw('Negative weight cycle detected')

    def func_rhvk(arg_ihhe, arg_xdvx: var_hqta, var_wnki: var_rgwu[var_rgwu
        [var_hqta]], arg_yybh: var_hqta) ->var_hqta:
        var_bzkm = -1
        var_icgs = arg_xdvx
        for var_dcmd in var_ayzf(arg_xdvx):
            var_wkgu = var_pmuo(1 for var_eieh in var_ayzf(arg_xdvx) if 
                var_dcmd != var_eieh and var_wnki[var_dcmd][var_eieh] <=
                arg_yybh)
            if var_wkgu <= var_icgs:
                var_icgs = var_wkgu
                var_bzkm = var_dcmd
        return var_bzkm
