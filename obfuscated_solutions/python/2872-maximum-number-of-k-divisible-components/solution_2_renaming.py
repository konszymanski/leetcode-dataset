class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_wrnh
        [var_rgwu]], arg_bacg: var_wrnh[var_rgwu], arg_hqta: var_rgwu
        ) ->var_rgwu:
        if arg_xdvx < 2:
            return 1
        var_osiz = 0
        var_ayzf = var_wnki(var_egyk)
        for var_dcmd, var_llti in arg_rcsn:
            var_ayzf[var_dcmd].add(var_llti)
            var_ayzf[var_llti].add(var_dcmd)
        var_zbxo = var_rdmc(var_rjut for var_rjut, var_lsgw in var_ayzf.
            items() if var_cbvh(var_lsgw) == 1)
        while var_zbxo:
            var_yjch = var_zbxo.popleft()
            var_dmio = var_ulfl(var_lgvi(var_ayzf[var_yjch])) if var_ayzf[
                var_yjch] else -1
            if var_dmio >= 0:
                var_ayzf[var_dmio].remove(var_yjch)
            if values[var_yjch] % arg_hqta == 0:
                var_osiz += 1
            else:
                values[var_dmio] += values[var_yjch]
            if var_dmio >= 0 and var_cbvh(var_ayzf[var_dmio]) == 1:
                var_zbxo.append(var_dmio)
        return var_osiz
