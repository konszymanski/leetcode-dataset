class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [False] * (var_rcsn + 1)
        for var_osiz in arg_xdvx:
            var_wrnh[var_osiz] = True
        if var_hqta == 1:
            return True
        if var_wrnh[1]:
            return False
        var_ayzf = [0] * (var_rcsn + 1)
        for var_wnki in var_egyk(2, var_rcsn + 1):
            if var_ayzf[var_wnki] == 0:
                for var_dcmd in var_egyk(var_wnki, var_rcsn + 1, var_wnki):
                    var_ayzf[var_dcmd] = var_wnki
        var_llti = var_zbxo(2 * var_rcsn + 1)
        for var_osiz in arg_xdvx:
            var_rdmc = var_osiz
            while var_rdmc > 1:
                var_rjut = var_ayzf[var_rdmc]
                var_lsgw = var_rjut + var_rcsn
                if var_llti.find(var_lsgw) != var_llti.find(var_osiz):
                    var_llti.merge(var_lsgw, var_osiz)
                while var_rdmc % var_rjut == 0:
                    var_rdmc //= var_rjut
        var_cbvh = 0
        for var_yjch in var_egyk(2, var_rcsn + 1):
            if var_wrnh[var_yjch] and var_llti.find(var_yjch) == var_yjch:
                var_cbvh += 1
        return var_cbvh == 1


class DSU:

    def func_dmio(arg_ihhe, var_hqta):
        arg_ihhe.dsu = var_ulfl(var_egyk(var_hqta + 1))
        arg_ihhe.size = [1] * (var_hqta + 1)

    def func_lgvi(arg_ihhe, var_osiz):
        return var_osiz if arg_ihhe.dsu[var_osiz
            ] == var_osiz else arg_ihhe.find(arg_ihhe.dsu[var_osiz])

    def func_wvuc(arg_ihhe, var_osiz, arg_tufr):
        var_xhfo = arg_ihhe.find(var_osiz)
        var_miuw = arg_ihhe.find(arg_tufr)
        if var_xhfo == var_miuw:
            return
        if arg_ihhe.size[var_xhfo] > arg_ihhe.size[var_miuw]:
            var_xhfo, var_miuw = var_miuw, var_xhfo
        arg_ihhe.dsu[var_xhfo] = var_miuw
        arg_ihhe.size[var_miuw] += arg_ihhe.size[var_xhfo]
