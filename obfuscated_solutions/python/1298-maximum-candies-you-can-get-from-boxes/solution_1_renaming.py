class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh[var_osiz], arg_rcsn:
        var_wrnh[var_osiz], arg_bacg: var_wrnh[var_wrnh[var_osiz]],
        arg_hqta: var_wrnh[var_wrnh[var_osiz]], arg_rgwu: var_wrnh[var_osiz]
        ) ->var_osiz:
        var_ayzf = var_wnki(arg_xdvx)
        var_egyk = [(arg_xdvx[var_dcmd] == 1) for var_dcmd in var_llti(
            var_ayzf)]
        var_zbxo, var_rdmc = [False] * var_ayzf, [False] * var_ayzf
        var_rjut = var_lsgw.deque()
        var_cbvh = 0
        for var_yjch in arg_rgwu:
            var_zbxo[var_yjch] = True
            if var_egyk[var_yjch]:
                var_rjut.append(var_yjch)
                var_rdmc[var_yjch] = True
                var_cbvh += arg_rcsn[var_yjch]
        while var_wnki(var_rjut) > 0:
            var_dmio = var_rjut.popleft()
            for var_ulfl in keys[var_dmio]:
                var_egyk[var_ulfl] = True
                if not var_rdmc[var_ulfl] and var_zbxo[var_ulfl]:
                    var_rjut.append(var_ulfl)
                    var_rdmc[var_ulfl] = True
                    var_cbvh += arg_rcsn[var_ulfl]
            for var_yjch in arg_hqta[var_dmio]:
                var_zbxo[var_yjch] = True
                if not var_rdmc[var_yjch] and var_egyk[var_yjch]:
                    var_rjut.append(var_yjch)
                    var_rdmc[var_yjch] = True
                    var_cbvh += arg_rcsn[var_yjch]
        return var_cbvh
