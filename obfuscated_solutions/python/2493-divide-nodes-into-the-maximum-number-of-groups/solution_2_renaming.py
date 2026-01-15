class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [[] for var_hqta in var_rgwu(arg_xdvx)]
        var_wrnh = [-1] * arg_xdvx
        var_osiz = [0] * arg_xdvx
        for var_ayzf in arg_rcsn:
            var_bacg[var_ayzf[0] - 1].append(var_ayzf[1] - 1)
            var_bacg[var_ayzf[1] - 1].append(var_ayzf[0] - 1)
            arg_ihhe._union(var_ayzf[0] - 1, var_ayzf[1] - 1, var_wrnh,
                var_osiz)
        var_wnki = {}
        for var_egyk in var_rgwu(arg_xdvx):
            var_dcmd = arg_ihhe._get_number_of_groups(var_bacg, var_egyk,
                arg_xdvx)
            if var_dcmd == -1:
                return -1
            var_llti = arg_ihhe._find(var_egyk, var_wrnh)
            var_wnki[var_llti] = var_zbxo(var_wnki.get(var_llti, 0), var_dcmd)
        var_rdmc = var_rjut(var_wnki.values())
        return var_rdmc

    def func_lsgw(arg_ihhe, var_bacg, arg_cbvh, arg_xdvx):
        var_yjch = var_dmio()
        var_ulfl = [-1] * arg_xdvx
        var_yjch.append(arg_cbvh)
        var_ulfl[arg_cbvh] = 0
        var_lgvi = 0
        while var_yjch:
            var_wvuc = var_tufr(var_yjch)
            for var_hqta in var_rgwu(var_wvuc):
                var_xhfo = var_yjch.popleft()
                for var_miuw in var_bacg[var_xhfo]:
                    if var_ulfl[var_miuw] == -1:
                        var_ulfl[var_miuw] = var_lgvi + 1
                        var_yjch.append(var_miuw)
                    elif var_ulfl[var_miuw] == var_lgvi:
                        return -1
            var_lgvi += 1
        return var_lgvi

    def func_rhvk(arg_ihhe, var_egyk, var_wrnh):
        while var_wrnh[var_egyk] != -1:
            var_egyk = var_wrnh[var_egyk]
        return var_egyk

    def func_yybh(arg_ihhe, arg_bzkm, arg_icgs, var_wrnh, var_osiz):
        arg_bzkm = arg_ihhe._find(arg_bzkm, var_wrnh)
        arg_icgs = arg_ihhe._find(arg_icgs, var_wrnh)
        if arg_bzkm == arg_icgs:
            return
        if var_osiz[arg_bzkm] < var_osiz[arg_icgs]:
            arg_bzkm, arg_icgs = arg_icgs, arg_bzkm
        var_wrnh[arg_icgs] = arg_bzkm
        if var_osiz[arg_bzkm] == var_osiz[arg_icgs]:
            var_osiz[arg_bzkm] += 1
