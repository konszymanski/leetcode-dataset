class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_bacg)
        var_wrnh = [[] for var_osiz in var_ayzf(var_hqta)]
        var_wnki = {}
        var_egyk = [False] * var_hqta
        var_dcmd = var_llti('-inf')
        for var_zbxo in arg_xdvx:
            var_wrnh[var_zbxo[0]].append(var_zbxo[1])
            var_wrnh[var_zbxo[1]].append(var_zbxo[0])

        def func_rdmc(arg_rjut, arg_lsgw):
            var_wnki[arg_rjut] = arg_lsgw
            var_egyk[arg_rjut] = True
            if arg_rjut == 0:
                return True
            for var_cbvh in var_wrnh[arg_rjut]:
                if not var_egyk[var_cbvh] and func_rdmc(var_cbvh, arg_lsgw + 1
                    ):
                    return True
            var_wnki.pop(arg_rjut, None)
            return False
        func_rdmc(arg_rcsn, 0)
        var_egyk = [False] * var_hqta

        def func_yjch(arg_rjut, arg_lsgw, arg_dmio):
            nonlocal max_income
            var_egyk[arg_rjut] = True
            if arg_rjut not in var_wnki or arg_lsgw < var_wnki[arg_rjut]:
                arg_dmio += arg_bacg[arg_rjut]
            elif arg_lsgw == var_wnki[arg_rjut]:
                arg_dmio += arg_bacg[arg_rjut] // 2
            if var_rgwu(var_wrnh[arg_rjut]) == 1 and arg_rjut != 0:
                var_dcmd = var_ulfl(var_dcmd, arg_dmio)
            for var_cbvh in var_wrnh[arg_rjut]:
                if not var_egyk[var_cbvh]:
                    func_yjch(var_cbvh, arg_lsgw + 1, arg_dmio)
        func_yjch(0, 0, 0)
        return var_dcmd
