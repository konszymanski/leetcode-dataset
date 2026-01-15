from queue import PriorityQueue


class Solution:
    var_udax = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_bacg)
        var_wrnh = [0] * var_hqta
        var_osiz = var_rgwu(arg_rcsn)
        var_ayzf = var_rgwu(arg_rcsn[0])
        var_wnki = var_osiz * var_ayzf
        var_egyk = [0] * (var_wnki + 1)
        var_dcmd = [([var_llti('inf')] * var_ayzf) for var_zbxo in var_rdmc
            (var_osiz)]
        var_dcmd[0][0] = arg_rcsn[0][0]
        var_rjut = var_lsgw()
        var_rjut.put((arg_rcsn[0][0], 0, 0))
        var_cbvh = 0
        while not var_rjut.empty():
            var_yjch = var_rjut.get()
            var_egyk[var_cbvh + 1] = var_yjch[0]
            var_cbvh += 1
            for var_dmio in arg_xdvx.DIRECTIONS:
                var_ulfl, var_lgvi = var_yjch[1] + var_dmio[0], var_yjch[2
                    ] + var_dmio[1]
                if (0 <= var_ulfl < var_osiz and 0 <= var_lgvi < var_ayzf and
                    var_dcmd[var_ulfl][var_lgvi] == var_llti('inf')):
                    var_dcmd[var_ulfl][var_lgvi] = var_wvuc(var_yjch[0],
                        arg_rcsn[var_ulfl][var_lgvi])
                    var_rjut.put((var_dcmd[var_ulfl][var_lgvi], var_ulfl,
                        var_lgvi))
        for var_tufr in var_rdmc(var_hqta):
            var_xhfo = arg_bacg[var_tufr]
            var_miuw, var_rhvk = 0, var_wnki
            while var_miuw < var_rhvk:
                var_yybh = var_miuw + (var_rhvk - var_miuw + 1) // 2
                if var_egyk[var_yybh] < var_xhfo:
                    var_miuw = var_yybh
                else:
                    var_rhvk = var_yybh - 1
            var_wrnh[var_tufr] = var_miuw
        return var_wrnh
