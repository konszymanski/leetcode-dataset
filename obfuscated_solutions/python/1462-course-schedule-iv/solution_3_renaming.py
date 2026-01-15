class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_rgwu[var_hqta]]) ->var_rgwu[
        var_lgvi]:
        var_wrnh = var_osiz(var_ayzf)
        var_wnki = [0] * arg_xdvx
        for var_egyk in arg_rcsn:
            var_wrnh[var_egyk[0]].append(var_egyk[1])
            var_wnki[var_egyk[1]] += 1
        var_dcmd = var_llti()
        for var_zbxo in var_rdmc(arg_xdvx):
            if var_wnki[var_zbxo] == 0:
                var_dcmd.append(var_zbxo)
        var_rjut = var_osiz(var_lsgw)
        while var_dcmd:
            var_cbvh = var_dcmd.popleft()
            for var_yjch in var_wrnh[var_cbvh]:
                var_rjut[var_yjch].add(var_cbvh)
                for var_dmio in var_rjut[var_cbvh]:
                    var_rjut[var_yjch].add(var_dmio)
                var_wnki[var_yjch] -= 1
                if var_wnki[var_yjch] == 0:
                    var_dcmd.append(var_yjch)
        var_ulfl = []
        for var_dcmd in arg_bacg:
            var_ulfl.append(var_dcmd[0] in var_rjut[var_dcmd[1]])
        return var_ulfl
