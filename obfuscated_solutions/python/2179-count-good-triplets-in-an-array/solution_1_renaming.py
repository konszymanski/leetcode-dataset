class FenwickTree:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.tree = [0] * (arg_xdvx + 1)

    def func_rcsn(arg_ihhe, arg_bacg, arg_hqta):
        arg_bacg += 1
        while arg_bacg <= var_rgwu(arg_ihhe.tree) - 1:
            arg_ihhe.tree[arg_bacg] += arg_hqta
            arg_bacg += arg_bacg & -arg_bacg

    def func_wrnh(arg_ihhe, arg_bacg):
        arg_bacg += 1
        var_osiz = 0
        while arg_bacg > 0:
            var_osiz += arg_ihhe.tree[arg_bacg]
            arg_bacg -= arg_bacg & -arg_bacg
        return var_osiz


class Solution:

    def func_ayzf(arg_ihhe, arg_wnki: var_dcmd[var_llti], arg_egyk:
        var_dcmd[var_llti]) ->var_llti:
        var_zbxo = var_rgwu(arg_wnki)
        var_rdmc, var_rjut = [0] * var_zbxo, [0] * var_zbxo
        for var_lsgw, var_cbvh in var_yjch(arg_egyk):
            var_rdmc[var_cbvh] = var_lsgw
        for var_lsgw, var_dmio in var_yjch(arg_wnki):
            var_rjut[var_rdmc[var_dmio]] = var_lsgw
        var_ulfl = var_lgvi(var_zbxo)
        var_osiz = 0
        for var_wvuc in var_tufr(var_zbxo):
            var_xhfo = var_rjut[var_wvuc]
            var_miuw = var_ulfl.query(var_xhfo)
            var_ulfl.update(var_xhfo, 1)
            var_rhvk = var_zbxo - 1 - var_xhfo - (var_wvuc - var_miuw)
            var_osiz += var_miuw * var_rhvk
        return var_osiz
