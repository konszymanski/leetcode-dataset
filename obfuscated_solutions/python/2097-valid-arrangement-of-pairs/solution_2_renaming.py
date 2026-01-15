class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg.defaultdict(var_hqta)
        var_rgwu, var_wrnh = var_bacg.defaultdict(var_osiz
            ), var_bacg.defaultdict(var_osiz)
        for var_ayzf in arg_xdvx:
            var_wnki, var_egyk = var_ayzf[0], var_ayzf[1]
            var_rcsn[var_wnki].append(var_egyk)
            var_wrnh[var_wnki] += 1
            var_rgwu[var_egyk] += 1
        var_dcmd = []
        var_llti = -1
        for var_zbxo in var_wrnh:
            if var_wrnh[var_zbxo] == var_rgwu[var_zbxo] + 1:
                var_llti = var_zbxo
                break
        if var_llti == -1:
            var_llti = arg_xdvx[0][0]
        var_rdmc = [var_llti]
        while var_rdmc:
            var_zbxo = var_rdmc[-1]
            if var_rcsn[var_zbxo]:
                var_rjut = var_rcsn[var_zbxo].pop(0)
                var_rdmc.append(var_rjut)
            else:
                var_dcmd.append(var_zbxo)
                var_rdmc.pop()
        var_dcmd.reverse()
        var_lsgw = []
        for var_cbvh in var_yjch(1, var_dmio(var_dcmd)):
            var_lsgw.append([var_dcmd[var_cbvh - 1], var_dcmd[var_cbvh]])
        return var_lsgw
