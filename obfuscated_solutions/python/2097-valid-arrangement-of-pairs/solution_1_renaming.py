class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        from collections import defaultdict, deque
        var_rcsn = var_bacg(var_hqta)
        var_rgwu, var_wrnh = var_bacg(var_osiz), var_bacg(var_osiz)
        for var_ayzf in arg_xdvx:
            var_wnki, var_egyk = var_ayzf
            var_rcsn[var_wnki].append(var_egyk)
            var_wrnh[var_wnki] += 1
            var_rgwu[var_egyk] += 1
        var_dcmd = []

        def func_llti(arg_zbxo):
            while var_rcsn[arg_zbxo]:
                var_rdmc = var_rcsn[arg_zbxo].popleft()
                func_llti(var_rdmc)
            var_dcmd.append(arg_zbxo)
        var_rjut = -1
        for arg_zbxo in var_wrnh:
            if var_wrnh[arg_zbxo] == var_rgwu[arg_zbxo] + 1:
                var_rjut = arg_zbxo
                break
        if var_rjut == -1:
            var_rjut = arg_xdvx[0][0]
        func_llti(var_rjut)
        var_dcmd.reverse()
        var_lsgw = [[var_dcmd[var_cbvh - 1], var_dcmd[var_cbvh]] for
            var_cbvh in var_yjch(1, var_dmio(var_dcmd))]
        return var_lsgw
