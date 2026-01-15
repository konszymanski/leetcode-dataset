class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_wrnh]) ->var_wrnh:
        var_osiz = var_ayzf(arg_xdvx)
        arg_ihhe.max_score = 0
        var_wnki = [(0) for var_egyk in var_dcmd(26)]
        var_llti = [(0) for var_egyk in var_dcmd(26)]
        for var_zbxo in arg_rcsn:
            var_wnki[var_rdmc(var_zbxo) - 97] += 1

        def func_rjut(var_llti):
            for var_zbxo in var_dcmd(26):
                if var_wnki[var_zbxo] < var_llti[var_zbxo]:
                    return False
            else:
                return True

        def func_lsgw(arg_cbvh, arg_xdvx, arg_bacg, var_llti, arg_yjch):
            if arg_cbvh == -1:
                arg_ihhe.max_score = var_dmio(arg_ihhe.max_score, arg_yjch)
                return
            func_lsgw(arg_cbvh - 1, arg_xdvx, arg_bacg, var_llti, arg_yjch)
            var_ulfl = var_ayzf(arg_xdvx[arg_cbvh])
            for var_egyk in var_dcmd(var_ulfl):
                var_zbxo = var_rdmc(arg_xdvx[arg_cbvh][var_egyk]) - 97
                var_llti[var_zbxo] += 1
                arg_yjch += arg_bacg[var_zbxo]
            if func_rjut(var_llti):
                func_lsgw(arg_cbvh - 1, arg_xdvx, arg_bacg, var_llti, arg_yjch)
            for var_egyk in var_dcmd(var_ulfl):
                var_zbxo = var_rdmc(arg_xdvx[arg_cbvh][var_egyk]) - 97
                var_llti[var_zbxo] -= 1
                arg_yjch -= arg_bacg[var_zbxo]
        func_lsgw(var_osiz - 1, arg_xdvx, arg_bacg, var_llti, 0)
        return arg_ihhe.max_score
