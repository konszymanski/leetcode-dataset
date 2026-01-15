class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_bacg)
        var_wrnh = var_osiz('-inf')
        var_ayzf = [[] for var_wnki in var_egyk(var_hqta)]
        var_dcmd = {}
        var_llti = [False] * var_hqta
        for var_zbxo in arg_xdvx:
            var_ayzf[var_zbxo[0]].append(var_zbxo[1])
            var_ayzf[var_zbxo[1]].append(var_zbxo[0])

        def func_rdmc(arg_rjut, arg_lsgw):
            var_dcmd[arg_rjut] = arg_lsgw
            var_llti[arg_rjut] = True
            if arg_rjut == 0:
                return True
            for var_cbvh in var_ayzf[arg_rjut]:
                if not var_llti[var_cbvh]:
                    if func_rdmc(var_cbvh, arg_lsgw + 1):
                        return True
            var_dcmd.pop(arg_rjut, None)
            return False
        func_rdmc(arg_rcsn, 0)
        var_llti = [False] * var_hqta
        var_yjch = var_dmio([(0, 0, 0)])
        while var_yjch:
            arg_rjut, arg_lsgw, var_ulfl = var_yjch.popleft()
            if arg_rjut not in var_dcmd or arg_lsgw < var_dcmd[arg_rjut]:
                var_ulfl += arg_bacg[arg_rjut]
            elif arg_lsgw == var_dcmd[arg_rjut]:
                var_ulfl += arg_bacg[arg_rjut] // 2
            if var_rgwu(var_ayzf[arg_rjut]) == 1 and arg_rjut != 0:
                var_wrnh = var_lgvi(var_wrnh, var_ulfl)
            for var_cbvh in var_ayzf[arg_rjut]:
                if not var_llti[var_cbvh]:
                    var_yjch.append((var_cbvh, arg_lsgw + 1, var_ulfl))
            var_llti[arg_rjut] = True
        return var_wrnh
