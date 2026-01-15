class Cell:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        arg_ihhe.row = arg_xdvx
        arg_ihhe.col = arg_rcsn
        arg_ihhe.value = arg_bacg


class Query:

    def func_udax(arg_ihhe, arg_hqta, arg_bacg):
        arg_ihhe.index = arg_hqta
        arg_ihhe.value = arg_bacg


class UnionFind:

    def func_udax(arg_ihhe, arg_rgwu):
        arg_ihhe.parent = [-1] * arg_rgwu
        arg_ihhe.size = [1] * arg_rgwu

    def func_wrnh(arg_ihhe, arg_osiz):
        if arg_ihhe.parent[arg_osiz] < 0:
            return arg_osiz
        return arg_ihhe.find(arg_ihhe.parent[arg_osiz])

    def func_ayzf(arg_ihhe, arg_wnki, arg_egyk):
        var_dcmd = arg_ihhe.find(arg_wnki)
        var_llti = arg_ihhe.find(arg_egyk)
        if var_dcmd == var_llti:
            return False
        if arg_ihhe.size[var_dcmd] > arg_ihhe.size[var_llti]:
            arg_ihhe.parent[var_llti] = var_dcmd
            arg_ihhe.size[var_dcmd] += arg_ihhe.size[var_llti]
        else:
            arg_ihhe.parent[var_dcmd] = var_llti
            arg_ihhe.size[var_llti] += arg_ihhe.size[var_dcmd]
        return True

    def func_zbxo(arg_ihhe, arg_osiz):
        return arg_ihhe.size[arg_ihhe.find(arg_osiz)]


class Solution:
    var_rdmc = [0, 0, 1, -1]
    var_rjut = [1, -1, 0, 0]

    def func_lsgw(arg_ihhe, arg_cbvh, arg_yjch):
        var_dmio, var_ulfl = var_lgvi(arg_cbvh), var_lgvi(arg_cbvh[0])
        var_wvuc = var_dmio * var_ulfl
        var_tufr = [var_xhfo(var_miuw, var_rhvk) for var_miuw, var_rhvk in
            var_yybh(arg_yjch)]
        var_tufr.sort(key=lambda x: var_bzkm.value)
        var_icgs = [var_wkgu(arg_xdvx, arg_rcsn, arg_cbvh[arg_xdvx][
            arg_rcsn]) for arg_xdvx in var_pmuo(var_dmio) for arg_rcsn in
            var_pmuo(var_ulfl)]
        var_icgs.sort(key=lambda x: var_bzkm.value)
        var_eieh = var_xrri(var_wvuc)
        var_xsns = [0] * var_lgvi(arg_yjch)
        var_mlhe = 0
        for var_qpcy in var_tufr:
            while var_mlhe < var_wvuc and var_icgs[var_mlhe
                ].value < var_qpcy.value:
                arg_xdvx = var_icgs[var_mlhe].row
                arg_rcsn = var_icgs[var_mlhe].col
                var_bdeu = arg_xdvx * var_ulfl + arg_rcsn
                for var_fzvn in var_pmuo(4):
                    var_tcmm = arg_xdvx + var_toqi.ROW_DIRECTIONS[var_fzvn]
                    var_ravx = arg_rcsn + var_toqi.COL_DIRECTIONS[var_fzvn]
                    if (0 <= var_tcmm < var_dmio and 0 <= var_ravx <
                        var_ulfl and arg_cbvh[var_tcmm][var_ravx] <
                        var_qpcy.value):
                        var_eieh.union(var_bdeu, var_tcmm * var_ulfl + var_ravx
                            )
                var_mlhe += 1
            var_xsns[var_qpcy.index] = var_eieh.get_size(0
                ) if var_qpcy.value > arg_cbvh[0][0] else 0
        return var_xsns
