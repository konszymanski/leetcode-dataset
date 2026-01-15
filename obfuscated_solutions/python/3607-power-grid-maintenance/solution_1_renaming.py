class DSU:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.parent = var_rcsn(var_bacg(arg_xdvx))

    def func_hqta(arg_ihhe, arg_rgwu):
        if arg_ihhe.parent[arg_rgwu] != arg_rgwu:
            arg_ihhe.parent[arg_rgwu] = arg_ihhe.find(arg_ihhe.parent[arg_rgwu]
                )
        return arg_ihhe.parent[arg_rgwu]

    def func_wrnh(arg_ihhe, arg_osiz, arg_ayzf):
        arg_ihhe.parent[arg_ihhe.find(arg_ayzf)] = arg_ihhe.find(arg_osiz)


class Solution:

    def func_wnki(arg_ihhe, arg_egyk: var_zbxo, arg_dcmd: var_rdmc[var_rdmc
        [var_zbxo]], arg_llti: var_rdmc[var_rdmc[var_zbxo]]) ->var_rdmc[
        var_zbxo]:
        var_rjut = var_lsgw(arg_egyk + 1)
        for var_cbvh in arg_dcmd:
            var_rjut.join(var_cbvh[0], var_cbvh[1])
        var_yjch = [True] * (arg_egyk + 1)
        var_dmio = [0] * (arg_egyk + 1)
        var_ulfl = {}
        for var_lgvi in arg_llti:
            var_wvuc, arg_rgwu = var_lgvi[0], var_lgvi[1]
            if var_wvuc == 2:
                var_yjch[arg_rgwu] = False
                var_dmio[arg_rgwu] += 1
        for var_tufr in var_bacg(1, arg_egyk + 1):
            var_xhfo = var_rjut.find(var_tufr)
            if var_xhfo not in var_ulfl:
                var_ulfl[var_xhfo] = -1
            var_miuw = var_ulfl[var_xhfo]
            if var_yjch[var_tufr]:
                if var_miuw == -1 or var_miuw > var_tufr:
                    var_ulfl[var_xhfo] = var_tufr
        var_rhvk = []
        for var_tufr in var_bacg(var_yybh(arg_llti) - 1, -1, -1):
            var_wvuc, arg_rgwu = arg_llti[var_tufr][0], arg_llti[var_tufr][1]
            var_xhfo = var_rjut.find(arg_rgwu)
            var_miuw = var_ulfl[var_xhfo]
            if var_wvuc == 1:
                if var_yjch[arg_rgwu]:
                    var_rhvk.append(arg_rgwu)
                else:
                    var_rhvk.append(var_miuw)
            if var_wvuc == 2:
                if var_dmio[arg_rgwu] > 1:
                    var_dmio[arg_rgwu] -= 1
                else:
                    var_yjch[arg_rgwu] = True
                    if var_miuw == -1 or var_miuw > arg_rgwu:
                        var_ulfl[var_xhfo] = arg_rgwu
        return var_rhvk[::-1]
