class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_wrnh
        [var_rgwu]], arg_bacg: var_wrnh[var_rgwu], arg_hqta: var_rgwu
        ) ->var_rgwu:
        if arg_xdvx < 2:
            return 1
        var_osiz = 0
        var_ayzf = var_wnki(var_egyk)
        var_dcmd = [(0) for var_llti in var_zbxo(arg_xdvx)]
        for var_rdmc, var_rjut in arg_rcsn:
            var_ayzf[var_rdmc].append(var_rjut)
            var_ayzf[var_rjut].append(var_rdmc)
            var_dcmd[var_rdmc] += 1
            var_dcmd[var_rjut] += 1
        var_lsgw = var_cbvh(var_yjch for var_yjch in var_zbxo(arg_xdvx) if 
            var_dcmd[var_yjch] == 1)
        while var_lsgw:
            var_dmio = var_lsgw.popleft()
            var_dcmd[var_dmio] -= 1
            var_ulfl = 0
            if values[var_dmio] % arg_hqta == 0:
                var_osiz += 1
            else:
                var_ulfl = values[var_dmio]
            for var_lgvi in var_ayzf[var_dmio]:
                if var_dcmd[var_lgvi] == 0:
                    continue
                var_dcmd[var_lgvi] -= 1
                values[var_lgvi] += var_ulfl
                if var_dcmd[var_lgvi] == 1:
                    var_lsgw.append(var_lgvi)
        return var_osiz
