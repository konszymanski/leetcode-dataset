class UnionFind:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.parent = [-1] * arg_xdvx
        arg_ihhe.size = [1] * arg_xdvx

    def func_rcsn(arg_ihhe, arg_bacg):
        if arg_ihhe.parent[arg_bacg] == -1:
            return arg_bacg
        arg_ihhe.parent[arg_bacg] = arg_ihhe._find(arg_ihhe.parent[arg_bacg])
        return arg_ihhe.parent[arg_bacg]

    def func_hqta(arg_ihhe, arg_rgwu, arg_wrnh):
        var_osiz = arg_ihhe._find(arg_rgwu)
        var_ayzf = arg_ihhe._find(arg_wrnh)
        if var_osiz == var_ayzf:
            return
        if arg_ihhe.size[var_osiz] > arg_ihhe.size[var_ayzf]:
            arg_ihhe.parent[var_ayzf] = var_osiz
            arg_ihhe.size[var_osiz] += arg_ihhe.size[var_ayzf]
        else:
            arg_ihhe.parent[var_osiz] = var_ayzf
            arg_ihhe.size[var_ayzf] += arg_ihhe.size[var_osiz]


class Solution:

    def func_wnki(arg_ihhe, arg_xdvx: var_dcmd, arg_egyk: var_llti[var_llti
        [var_dcmd]]) ->var_dcmd:
        var_zbxo = var_rdmc(arg_xdvx)
        var_rjut = {}
        for var_lsgw in arg_egyk:
            var_zbxo._union(var_lsgw[0], var_lsgw[1])
        for var_lsgw in arg_egyk:
            var_cbvh = var_zbxo._find(var_lsgw[0])
            var_rjut[var_cbvh] = var_rjut.get(var_cbvh, 0) + 1
        var_yjch = 0
        for var_dmio in var_ulfl(arg_xdvx):
            if var_zbxo._find(var_dmio) == var_dmio:
                var_lgvi = var_zbxo.size[var_dmio]
                var_wvuc = var_lgvi * (var_lgvi - 1) // 2
                if var_rjut.get(var_dmio, 0) == var_wvuc:
                    var_yjch += 1
        return var_yjch
