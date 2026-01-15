class UnionFind:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_ihhe.components = arg_xdvx
        arg_ihhe.parents = var_rcsn(var_bacg(arg_xdvx))

    def func_hqta(arg_ihhe, arg_rgwu, arg_wrnh):
        var_osiz = arg_ihhe.find(arg_rgwu)
        var_ayzf = arg_ihhe.find(arg_wrnh)
        if var_ayzf != arg_wrnh or var_osiz == var_ayzf:
            return False
        arg_ihhe.components -= 1
        arg_ihhe.parents[var_ayzf] = var_osiz
        return True

    def func_wnki(arg_ihhe, arg_egyk):
        if arg_ihhe.parents[arg_egyk] != arg_egyk:
            arg_ihhe.parents[arg_egyk] = arg_ihhe.find(arg_ihhe.parents[
                arg_egyk])
        return arg_ihhe.parents[arg_egyk]


class Solution:

    def func_dcmd(arg_ihhe, arg_xdvx: var_rdmc, arg_llti: var_rjut[var_rdmc
        ], arg_zbxo: var_rjut[var_rdmc]) ->var_yjch:
        var_lsgw = var_cbvh(arg_xdvx)
        for arg_egyk in var_bacg(arg_xdvx):
            for arg_wrnh in [arg_llti[arg_egyk], arg_zbxo[arg_egyk]]:
                if arg_wrnh == -1:
                    continue
                if not var_lsgw.union(arg_egyk, arg_wrnh):
                    return False
        return var_lsgw.components == 1
