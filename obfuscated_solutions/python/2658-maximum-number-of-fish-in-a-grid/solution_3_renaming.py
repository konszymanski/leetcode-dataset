class Solution:

    def func_udax(arg_ihhe, arg_xdvx):

        def func_rcsn(arg_bacg):
            if var_hqta[arg_bacg] != arg_bacg:
                var_hqta[arg_bacg] = func_rcsn(var_hqta[arg_bacg])
            return var_hqta[arg_bacg]

        def func_rgwu(arg_wrnh, arg_osiz):
            var_ayzf = func_rcsn(arg_wrnh)
            var_wnki = func_rcsn(arg_osiz)
            if var_ayzf != var_wnki:
                if var_egyk[var_ayzf] < var_egyk[var_wnki]:
                    var_ayzf, var_wnki = var_wnki, var_ayzf
                var_hqta[var_wnki] = var_ayzf
                var_egyk[var_ayzf] += var_egyk[var_wnki]
                var_dcmd[var_ayzf] += var_dcmd[var_wnki]
        var_llti, var_zbxo = var_rdmc(arg_xdvx), var_rdmc(arg_xdvx[0])
        var_rjut = var_llti * var_zbxo
        var_hqta = var_lsgw(var_cbvh(var_rjut))
        var_egyk = [1] * var_rjut
        var_dcmd = [0] * var_rjut
        for var_yjch in var_cbvh(var_llti):
            for var_dmio in var_cbvh(var_zbxo):
                arg_bacg = var_yjch * var_zbxo + var_dmio
                var_dcmd[arg_bacg] = arg_xdvx[var_yjch][var_dmio]
        var_ulfl = [0, 0, 1, -1]
        var_lgvi = [1, -1, 0, 0]
        for var_yjch in var_cbvh(var_llti):
            for var_dmio in var_cbvh(var_zbxo):
                if arg_xdvx[var_yjch][var_dmio] > 0:
                    arg_bacg = var_yjch * var_zbxo + var_dmio
                    for var_wvuc in var_cbvh(4):
                        var_tufr = var_yjch + var_ulfl[var_wvuc]
                        var_xhfo = var_dmio + var_lgvi[var_wvuc]
                        if (0 <= var_tufr < var_llti and 0 <= var_xhfo <
                            var_zbxo and arg_xdvx[var_tufr][var_xhfo] > 0):
                            var_miuw = var_tufr * var_zbxo + var_xhfo
                            func_rgwu(arg_bacg, var_miuw)
        var_rhvk = 0
        for arg_bacg in var_cbvh(var_rjut):
            if func_rcsn(arg_bacg) == arg_bacg:
                var_rhvk = var_yybh(var_rhvk, var_dcmd[arg_bacg])
        return var_rhvk
