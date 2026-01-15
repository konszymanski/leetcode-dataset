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
        var_lgvi, var_cbvh = arg_ihhe.find_farthest_node(var_bacg, var_lsgw, 0)
        var_cbvh, var_wvuc = arg_ihhe.find_farthest_node(var_bacg, var_lsgw,
            var_lgvi)
        return var_wvuc

    def func_tufr(arg_ihhe, var_bacg, var_lsgw, arg_xhfo):
        var_miuw = var_rhvk([arg_xhfo])
        var_yybh = [False] * var_bacg
        var_yybh[arg_xhfo] = True
        var_bzkm = 0
        var_lgvi = arg_xhfo
        while var_miuw:
            for var_cbvh in var_yjch(var_hqta(var_miuw)):
                var_icgs = var_miuw.popleft()
                var_lgvi = var_icgs
                for var_wkgu in var_lsgw[var_icgs]:
                    if not var_yybh[var_wkgu]:
                        var_yybh[var_wkgu] = True
                        var_miuw.append(var_wkgu)
            if var_miuw:
                var_bzkm += 1
        return var_lgvi, var_bzkm
