class SegmentTree(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        arg_xdvx.N = arg_rcsn
        arg_xdvx.H = 1
        while 1 << arg_xdvx.H < arg_rcsn:
            arg_xdvx.H += 1
        arg_xdvx.update_fn = arg_bacg
        arg_xdvx.query_fn = arg_hqta
        arg_xdvx.tree = [0] * (2 * arg_rcsn)
        arg_xdvx.lazy = [0] * arg_rcsn

    def func_rgwu(arg_xdvx, arg_wrnh, arg_osiz):
        arg_xdvx.tree[arg_wrnh] = arg_xdvx.update_fn(arg_xdvx.tree[arg_wrnh
            ], arg_osiz)
        if arg_wrnh < arg_xdvx.N:
            arg_xdvx.lazy[arg_wrnh] = arg_xdvx.update_fn(arg_xdvx.lazy[
                arg_wrnh], arg_osiz)

    def func_ayzf(arg_xdvx, arg_wrnh):
        while arg_wrnh > 1:
            arg_wrnh /= 2
            arg_xdvx.tree[arg_wrnh] = arg_xdvx.query_fn(arg_xdvx.tree[
                arg_wrnh * 2], arg_xdvx.tree[arg_wrnh * 2 + 1])
            arg_xdvx.tree[arg_wrnh] = arg_xdvx.update_fn(arg_xdvx.tree[
                arg_wrnh], arg_xdvx.lazy[arg_wrnh])

    def func_wnki(arg_xdvx, arg_wrnh):
        for var_egyk in var_dcmd(arg_xdvx.H, 0, -1):
            var_llti = arg_wrnh >> var_egyk
            if arg_xdvx.lazy[var_llti]:
                arg_xdvx._apply(var_llti * 2, arg_xdvx.lazy[var_llti])
                arg_xdvx._apply(var_llti * 2 + 1, arg_xdvx.lazy[var_llti])
                arg_xdvx.lazy[var_llti] = 0

    def func_zbxo(arg_xdvx, arg_rdmc, arg_rjut, var_egyk):
        arg_rdmc += arg_xdvx.N
        arg_rjut += arg_xdvx.N
        var_lsgw, var_cbvh = arg_rdmc, arg_rjut
        while arg_rdmc <= arg_rjut:
            if arg_rdmc & 1:
                arg_xdvx._apply(arg_rdmc, var_egyk)
                arg_rdmc += 1
            if arg_rjut & 1 == 0:
                arg_xdvx._apply(arg_rjut, var_egyk)
                arg_rjut -= 1
            arg_rdmc /= 2
            arg_rjut /= 2
        arg_xdvx._pull(var_lsgw)
        arg_xdvx._pull(var_cbvh)

    def func_yjch(arg_xdvx, arg_rdmc, arg_rjut):
        arg_rdmc += arg_xdvx.N
        arg_rjut += arg_xdvx.N
        arg_xdvx._push(arg_rdmc)
        arg_xdvx._push(arg_rjut)
        var_dmio = 0
        while arg_rdmc <= arg_rjut:
            if arg_rdmc & 1:
                var_dmio = arg_xdvx.query_fn(var_dmio, arg_xdvx.tree[arg_rdmc])
                arg_rdmc += 1
            if arg_rjut & 1 == 0:
                var_dmio = arg_xdvx.query_fn(var_dmio, arg_xdvx.tree[arg_rjut])
                arg_rjut -= 1
            arg_rdmc /= 2
            arg_rjut /= 2
        return var_dmio


class Solution(var_udax):

    def func_ulfl(arg_xdvx, arg_lgvi):
        var_wvuc = var_tufr(var_xhfo(var_miuw), var_rhvk, var_rhvk)
        var_yybh = 0
        var_dmio = []
        for var_bzkm, var_icgs in arg_lgvi:
            arg_rdmc, arg_rjut = var_miuw[var_bzkm], var_miuw[var_bzkm +
                var_icgs - 1]
            var_egyk = var_wvuc.query(arg_rdmc, arg_rjut) + var_icgs
            var_wvuc.update(arg_rdmc, arg_rjut, var_egyk)
            var_yybh = var_rhvk(var_yybh, var_egyk)
            var_dmio.append(var_yybh)
        return var_dmio
