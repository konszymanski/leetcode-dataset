class UnionFind:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.parent = var_rcsn(var_bacg(arg_xdvx))
        arg_ihhe.rank = [0] * arg_xdvx

    def func_hqta(arg_ihhe, arg_rgwu):
        if arg_ihhe.parent[arg_rgwu] != arg_rgwu:
            arg_ihhe.parent[arg_rgwu] = arg_ihhe.find(arg_ihhe.parent[arg_rgwu]
                )
        return arg_ihhe.parent[arg_rgwu]

    def func_wrnh(arg_ihhe, arg_rgwu, arg_osiz):
        var_ayzf = arg_ihhe.find(arg_rgwu)
        var_wnki = arg_ihhe.find(arg_osiz)
        if arg_ihhe.rank[var_ayzf] < arg_ihhe.rank[var_wnki]:
            arg_ihhe.parent[var_ayzf] = var_wnki
        elif arg_ihhe.rank[var_ayzf] > arg_ihhe.rank[var_wnki]:
            arg_ihhe.parent[var_wnki] = var_ayzf
        else:
            arg_ihhe.parent[var_wnki] = var_ayzf
            arg_ihhe.rank[var_ayzf] += 1


class Solution:

    def func_egyk(arg_ihhe, arg_dcmd):
        var_llti = var_zbxo(arg_dcmd)
        var_rdmc = var_rjut(var_llti)
        var_lsgw = var_llti
        for var_cbvh in var_bacg(var_llti):
            for var_yjch in var_bacg(var_cbvh + 1, var_llti):
                if arg_dcmd[var_cbvh][var_yjch] == 1 and var_rdmc.find(var_cbvh
                    ) != var_rdmc.find(var_yjch):
                    var_lsgw -= 1
                    var_rdmc.union_set(var_cbvh, var_yjch)
        return var_lsgw
