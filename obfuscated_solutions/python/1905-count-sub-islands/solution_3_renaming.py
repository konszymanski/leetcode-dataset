class Solution:
    var_udax = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        return arg_hqta[arg_rcsn][arg_bacg] == 1


    class UnionFind:

        def func_rgwu(arg_xdvx, arg_wrnh):
            arg_xdvx.parent = var_osiz(var_ayzf(arg_wrnh))
            arg_xdvx.rank = [0] * arg_wrnh

        def func_wnki(arg_xdvx, arg_egyk):
            if arg_xdvx.parent[arg_egyk] != arg_egyk:
                arg_xdvx.parent[arg_egyk] = arg_xdvx.find(arg_xdvx.parent[
                    arg_egyk])
            return arg_xdvx.parent[arg_egyk]

        def func_dcmd(arg_xdvx, arg_egyk, arg_llti):
            var_zbxo = arg_xdvx.find(arg_egyk)
            var_rdmc = arg_xdvx.find(arg_llti)
            if var_zbxo != var_rdmc:
                if arg_xdvx.rank[var_zbxo] > arg_xdvx.rank[var_rdmc]:
                    arg_xdvx.parent[var_rdmc] = var_zbxo
                elif arg_xdvx.rank[var_zbxo] < arg_xdvx.rank[var_rdmc]:
                    arg_xdvx.parent[var_zbxo] = var_rdmc
                else:
                    arg_xdvx.parent[var_rdmc] = var_zbxo
                    arg_xdvx.rank[var_zbxo] += 1

    def func_rjut(arg_xdvx, arg_rcsn, arg_bacg, arg_lsgw):
        return arg_rcsn * arg_lsgw + arg_bacg

    def func_cbvh(arg_xdvx, arg_yjch: var_ulfl[var_ulfl[var_lgvi]],
        arg_dmio: var_ulfl[var_ulfl[var_lgvi]]) ->var_lgvi:
        var_wvuc = var_tufr(arg_dmio)
        arg_lsgw = var_tufr(arg_dmio[0])
        var_xhfo = arg_xdvx.UnionFind(var_wvuc * arg_lsgw)
        for arg_rcsn in var_ayzf(var_wvuc):
            for arg_bacg in var_ayzf(arg_lsgw):
                if arg_xdvx.is_cell_land(arg_rcsn, arg_bacg, arg_dmio):
                    for var_miuw in arg_xdvx.directions:
                        var_rhvk = arg_rcsn + var_miuw[0]
                        var_yybh = arg_bacg + var_miuw[1]
                        if (0 <= var_rhvk < var_wvuc and 0 <= var_yybh <
                            arg_lsgw and arg_xdvx.is_cell_land(var_rhvk,
                            var_yybh, arg_dmio)):
                            var_xhfo.union_sets(arg_xdvx.convert_to_index(
                                arg_rcsn, arg_bacg, arg_lsgw), arg_xdvx.
                                convert_to_index(var_rhvk, var_yybh, arg_lsgw))
        var_bzkm = [True] * (var_wvuc * arg_lsgw)
        for arg_rcsn in var_ayzf(var_wvuc):
            for arg_bacg in var_ayzf(arg_lsgw):
                if arg_xdvx.is_cell_land(arg_rcsn, arg_bacg, arg_dmio
                    ) and not arg_xdvx.is_cell_land(arg_rcsn, arg_bacg,
                    arg_yjch):
                    var_icgs = var_xhfo.find(arg_xdvx.convert_to_index(
                        arg_rcsn, arg_bacg, arg_lsgw))
                    var_bzkm[var_icgs] = False
        var_wkgu = 0
        for arg_rcsn in var_ayzf(var_wvuc):
            for arg_bacg in var_ayzf(arg_lsgw):
                if arg_xdvx.is_cell_land(arg_rcsn, arg_bacg, arg_dmio):
                    var_icgs = var_xhfo.find(arg_xdvx.convert_to_index(
                        arg_rcsn, arg_bacg, arg_lsgw))
                    if var_bzkm[var_icgs]:
                        var_wkgu += 1
                        var_bzkm[var_icgs] = False
        return var_wkgu
