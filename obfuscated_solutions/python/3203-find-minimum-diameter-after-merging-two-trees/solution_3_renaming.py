class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx) + 1
        var_rgwu = var_hqta(arg_rcsn) + 1
        var_wrnh = arg_ihhe.build_adj_list(var_bacg, arg_xdvx)
        var_osiz = arg_ihhe.build_adj_list(var_rgwu, arg_rcsn)
        var_ayzf = arg_ihhe.find_diameter(var_bacg, var_wrnh)
        var_wnki = arg_ihhe.find_diameter(var_rgwu, var_osiz)
        var_egyk = var_dcmd(var_ayzf / 2) + var_dcmd(var_wnki / 2) + 1
        return var_llti(var_ayzf, var_wnki, var_egyk)

    def func_zbxo(arg_ihhe, arg_rdmc, arg_rjut):
        var_lsgw = [[] for var_cbvh in var_yjch(arg_rdmc)]
        for var_dmio in arg_rjut:
            var_lsgw[var_dmio[0]].append(var_dmio[1])
            var_lsgw[var_dmio[1]].append(var_dmio[0])
        return var_lsgw

    def func_ulfl(arg_ihhe, var_bacg, var_lsgw):
        var_lgvi = var_wvuc()
        var_tufr = [0] * var_bacg
        for var_xhfo in var_yjch(var_bacg):
            var_tufr[var_xhfo] = var_hqta(var_lsgw[var_xhfo])
            if var_tufr[var_xhfo] == 1:
                var_lgvi.append(var_xhfo)
        var_miuw = var_bacg
        var_rhvk = 0
        while var_miuw > 2:
            arg_rdmc = var_hqta(var_lgvi)
            var_miuw -= arg_rdmc
            var_rhvk += 1
            for var_cbvh in var_yjch(arg_rdmc):
                var_yybh = var_lgvi.popleft()
                for var_bzkm in var_lsgw[var_yybh]:
                    var_tufr[var_bzkm] -= 1
                    if var_tufr[var_bzkm] == 1:
                        var_lgvi.append(var_bzkm)
        if var_miuw == 2:
            return 2 * var_rhvk + 1
        return 2 * var_rhvk
