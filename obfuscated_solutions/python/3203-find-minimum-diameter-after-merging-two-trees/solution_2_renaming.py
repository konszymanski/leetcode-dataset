class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx) + 1
        var_osiz = var_wrnh(arg_rcsn) + 1
        var_ayzf = arg_ihhe.build_adj_list(var_rgwu, arg_xdvx)
        var_wnki = arg_ihhe.build_adj_list(var_osiz, arg_rcsn)
        var_egyk, var_dcmd = arg_ihhe.find_diameter(var_ayzf, 0, -1)
        var_llti, var_dcmd = arg_ihhe.find_diameter(var_wnki, 0, -1)
        var_zbxo = var_rdmc(var_egyk / 2) + var_rdmc(var_llti / 2) + 1
        return var_rjut(var_egyk, var_llti, var_zbxo)

    def func_lsgw(arg_ihhe, arg_cbvh: var_hqta, arg_yjch: var_bacg[var_bacg
        [var_hqta]]) ->var_bacg[var_bacg[var_hqta]]:
        var_dmio = [[] for var_dcmd in var_ulfl(arg_cbvh)]
        for var_lgvi in arg_yjch:
            var_dmio[var_lgvi[0]].append(var_lgvi[1])
            var_dmio[var_lgvi[1]].append(var_lgvi[0])
        return var_dmio

    def func_wvuc(arg_ihhe, var_dmio: var_bacg[var_bacg[var_hqta]],
        arg_tufr: var_hqta, arg_xhfo: var_hqta) ->var_pmuo[var_hqta, var_hqta]:
        var_miuw = var_rhvk = 0
        var_yybh = 0
        for var_bzkm in var_dmio[arg_tufr]:
            if var_bzkm == arg_xhfo:
                continue
            var_icgs, var_wkgu = arg_ihhe.find_diameter(var_dmio, var_bzkm,
                arg_tufr)
            var_wkgu += 1
            var_yybh = var_rjut(var_yybh, var_icgs)
            if var_wkgu > var_miuw:
                var_rhvk = var_miuw
                var_miuw = var_wkgu
            elif var_wkgu > var_rhvk:
                var_rhvk = var_wkgu
        var_yybh = var_rjut(var_yybh, var_miuw + var_rhvk)
        return var_yybh, var_miuw
