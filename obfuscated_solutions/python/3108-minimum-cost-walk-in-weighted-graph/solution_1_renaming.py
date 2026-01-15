class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        arg_ihhe.parent = [-1] * arg_xdvx
        arg_ihhe.depth = [0] * arg_xdvx
        var_hqta = [-1] * arg_xdvx
        for var_rgwu in arg_rcsn:
            arg_ihhe._union(var_rgwu[0], var_rgwu[1])
        for var_rgwu in arg_rcsn:
            var_wrnh = arg_ihhe._find(var_rgwu[0])
            var_hqta[var_wrnh] &= var_rgwu[2]
        var_osiz = []
        for var_ayzf in arg_bacg:
            var_wnki, var_egyk = var_ayzf
            if arg_ihhe._find(var_wnki) != arg_ihhe._find(var_egyk):
                var_osiz.append(-1)
            else:
                var_wrnh = arg_ihhe._find(var_wnki)
                var_osiz.append(var_hqta[var_wrnh])
        return var_osiz

    def func_dcmd(arg_ihhe, arg_llti):
        if arg_ihhe.parent[arg_llti] == -1:
            return arg_llti
        arg_ihhe.parent[arg_llti] = arg_ihhe._find(arg_ihhe.parent[arg_llti])
        return arg_ihhe.parent[arg_llti]

    def func_zbxo(arg_ihhe, arg_rdmc, arg_rjut):
        var_lsgw = arg_ihhe._find(arg_rdmc)
        var_cbvh = arg_ihhe._find(arg_rjut)
        if var_lsgw == var_cbvh:
            return
        if arg_ihhe.depth[var_lsgw] < arg_ihhe.depth[var_cbvh]:
            var_lsgw, var_cbvh = var_cbvh, var_lsgw
        arg_ihhe.parent[var_cbvh] = var_lsgw
        if arg_ihhe.depth[var_lsgw] == arg_ihhe.depth[var_cbvh]:
            arg_ihhe.depth[var_lsgw] += 1
