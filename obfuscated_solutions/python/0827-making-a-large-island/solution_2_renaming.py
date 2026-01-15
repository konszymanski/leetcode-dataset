class DisjointSet:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn):
        arg_ihhe.parent = [var_bacg for var_bacg in var_hqta(arg_xdvx)]
        arg_ihhe.island_size = [1] * arg_xdvx

    def func_rgwu(arg_ihhe, arg_wrnh: var_rcsn) ->var_rcsn:
        if arg_ihhe.parent[arg_wrnh] == arg_wrnh:
            return arg_wrnh
        arg_ihhe.parent[arg_wrnh] = arg_ihhe.find_root(arg_ihhe.parent[
            arg_wrnh])
        return arg_ihhe.parent[arg_wrnh]

    def func_osiz(arg_ihhe, arg_ayzf: var_rcsn, arg_wnki: var_rcsn):
        var_egyk = arg_ihhe.find_root(arg_ayzf)
        var_dcmd = arg_ihhe.find_root(arg_wnki)
        if var_egyk == var_dcmd:
            return
        if arg_ihhe.island_size[var_egyk] < arg_ihhe.island_size[var_dcmd]:
            arg_ihhe.parent[var_egyk] = var_dcmd
            arg_ihhe.island_size[var_dcmd] += arg_ihhe.island_size[var_egyk]
        else:
            arg_ihhe.parent[var_dcmd] = var_egyk
            arg_ihhe.island_size[var_egyk] += arg_ihhe.island_size[var_dcmd]


class Solution:

    def func_llti(arg_ihhe, arg_zbxo: var_rdmc[var_rdmc[var_rcsn]]) ->var_rcsn:
        var_rjut = var_lsgw(arg_zbxo)
        var_cbvh = var_lsgw(arg_zbxo[0])
        var_yjch = var_dmio(var_rjut * var_cbvh)
        var_ulfl = [1, -1, 0, 0]
        var_lgvi = [0, 0, 1, -1]
        for var_wvuc in var_hqta(var_rjut):
            for var_tufr in var_hqta(var_cbvh):
                if arg_zbxo[var_wvuc][var_tufr] == 1:
                    var_xhfo = var_cbvh * var_wvuc + var_tufr
                    for var_miuw in var_hqta(4):
                        var_rhvk = var_wvuc + var_ulfl[var_miuw]
                        var_yybh = var_tufr + var_lgvi[var_miuw]
                        if (0 <= var_rhvk < var_rjut and 0 <= var_yybh <
                            var_cbvh and arg_zbxo[var_rhvk][var_yybh] == 1):
                            var_bzkm = var_cbvh * var_rhvk + var_yybh
                            var_yjch.union_nodes(var_xhfo, var_bzkm)
        var_icgs = 0
        var_wkgu = False
        var_pmuo = var_eieh()
        for var_wvuc in var_hqta(var_rjut):
            for var_tufr in var_hqta(var_cbvh):
                if arg_zbxo[var_wvuc][var_tufr] == 0:
                    var_wkgu = True
                    var_xrri = 1
                    for var_miuw in var_hqta(4):
                        var_rhvk = var_wvuc + var_ulfl[var_miuw]
                        var_yybh = var_tufr + var_lgvi[var_miuw]
                        if (0 <= var_rhvk < var_rjut and 0 <= var_yybh <
                            var_cbvh and arg_zbxo[var_rhvk][var_yybh] == 1):
                            var_bzkm = var_cbvh * var_rhvk + var_yybh
                            var_xsns = var_yjch.find_root(var_bzkm)
                            var_pmuo.add(var_xsns)
                    for var_xsns in var_pmuo:
                        var_xrri += var_yjch.island_size[var_xsns]
                    var_pmuo.clear()
                    var_icgs = var_mlhe(var_icgs, var_xrri)
        if not var_wkgu:
            return var_rjut * var_cbvh
        return var_icgs
