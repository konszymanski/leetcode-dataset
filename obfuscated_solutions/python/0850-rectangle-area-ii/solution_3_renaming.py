class Node:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_rgwu[var_hqta]) ->None:
        arg_ihhe.start, arg_ihhe.end = arg_xdvx, arg_rcsn
        arg_ihhe.total = arg_ihhe.count = 0
        arg_ihhe._left = arg_ihhe._right = None
        arg_ihhe.X = arg_bacg

    @var_osiz
    def func_wrnh(arg_ihhe):
        return (arg_ihhe.start + arg_ihhe.end) // 2

    @var_osiz
    def func_ayzf(arg_ihhe):
        arg_ihhe._left = arg_ihhe._left or var_wnki(arg_ihhe.start,
            arg_ihhe.mid, arg_ihhe.X)
        return arg_ihhe._left

    @var_osiz
    def func_egyk(arg_ihhe):
        arg_ihhe._right = arg_ihhe._right or var_wnki(arg_ihhe.mid,
            arg_ihhe.end, arg_ihhe.X)
        return arg_ihhe._right

    def func_dcmd(arg_ihhe, arg_llti: var_hqta, arg_zbxo: var_hqta,
        arg_rdmc: var_hqta) ->var_hqta:
        if arg_llti >= arg_zbxo:
            return 0
        if arg_ihhe.start == arg_llti and arg_ihhe.end == arg_zbxo:
            arg_ihhe.count += arg_rdmc
        else:
            arg_ihhe.left.update(arg_llti, var_rjut(arg_ihhe.mid, arg_zbxo),
                arg_rdmc)
            arg_ihhe.right.update(var_lsgw(arg_ihhe.mid, arg_llti),
                arg_zbxo, arg_rdmc)
        if arg_ihhe.count > 0:
            arg_ihhe.total = arg_ihhe.X[arg_ihhe.end] - arg_ihhe.X[arg_ihhe
                .start]
        else:
            arg_ihhe.total = arg_ihhe.left.total + arg_ihhe.right.total
        return arg_ihhe.total


class Solution:

    def func_cbvh(arg_ihhe, arg_yjch: var_rgwu[var_rgwu[var_hqta]]) ->var_hqta:
        var_dmio, var_ulfl = 1, -1
        var_lgvi = []
        arg_bacg = var_wvuc()
        for var_tufr, var_xhfo, var_miuw, var_rhvk in arg_yjch:
            if var_tufr < var_miuw and var_xhfo < var_rhvk:
                var_lgvi.append((var_xhfo, var_dmio, var_tufr, var_miuw))
                var_lgvi.append((var_rhvk, var_ulfl, var_tufr, var_miuw))
                arg_bacg.add(var_tufr)
                arg_bacg.add(var_miuw)
        var_lgvi.sort()
        arg_bacg = var_yybh(arg_bacg)
        var_bzkm = {var_icgs: arg_llti for arg_llti, var_icgs in var_wkgu(
            arg_bacg)}
        var_pmuo = var_wnki(0, var_eieh(arg_bacg) - 1, arg_bacg)
        var_xrri = 0
        var_xsns = 0
        var_mlhe = var_lgvi[0][0]
        for var_qpcy, var_bdeu, var_tufr, var_miuw in var_lgvi:
            var_xrri += var_xsns * (var_qpcy - var_mlhe)
            var_xsns = var_pmuo.update(var_bzkm[var_tufr], var_bzkm[
                var_miuw], var_bdeu)
            var_mlhe = var_qpcy
        return var_xrri % (10 ** 9 + 7)
