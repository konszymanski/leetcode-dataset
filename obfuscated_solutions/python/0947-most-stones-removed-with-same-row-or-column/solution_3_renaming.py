class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = arg_ihhe.UnionFind(20002)
        for var_bacg, var_hqta in arg_xdvx:
            var_rcsn._union_nodes(var_bacg, var_hqta + 10001)
        return var_rgwu(arg_xdvx) - var_rcsn.component_count


    class UnionFind:

        def func_wrnh(arg_ihhe, arg_osiz):
            arg_ihhe.parent = [-1] * arg_osiz
            arg_ihhe.component_count = 0
            arg_ihhe.unique_nodes = var_ayzf()

        def func_wnki(arg_ihhe, arg_egyk):
            if arg_egyk not in arg_ihhe.unique_nodes:
                arg_ihhe.component_count += 1
                arg_ihhe.unique_nodes.add(arg_egyk)
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
            arg_ihhe.parent[var_rdmc] = var_rjut
            arg_ihhe.component_count -= 1
