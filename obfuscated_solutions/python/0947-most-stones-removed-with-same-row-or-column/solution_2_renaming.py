class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = arg_ihhe.UnionFind(var_rcsn)
        for var_rgwu in var_wrnh(var_rcsn):
            for var_osiz in var_wrnh(var_rgwu + 1, var_rcsn):
                if arg_xdvx[var_rgwu][0] == arg_xdvx[var_osiz][0] or arg_xdvx[
                    var_rgwu][1] == arg_xdvx[var_osiz][1]:
                    var_hqta._union(var_rgwu, var_osiz)
        return var_rcsn - var_hqta.count


    class UnionFind:

        def func_ayzf(arg_ihhe, var_rcsn):
            arg_ihhe.parent = [-1] * var_rcsn
            arg_ihhe.count = var_rcsn

        def func_wnki(arg_ihhe, arg_egyk):
            if arg_ihhe.parent[arg_egyk] == -1:
                return arg_egyk
            arg_ihhe.parent[arg_egyk] = arg_ihhe._find(arg_ihhe.parent[
                arg_egyk])
            return arg_ihhe.parent[arg_egyk]

        def func_dcmd(arg_ihhe, arg_llti, arg_zbxo):
            var_rdmc = arg_ihhe._find(arg_llti)
            var_rjut = arg_ihhe._find(arg_zbxo)
            if var_rdmc == var_rjut:
                return
            arg_ihhe.count -= 1
            arg_ihhe.parent[var_rdmc] = var_rjut
