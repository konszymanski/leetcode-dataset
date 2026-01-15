class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_ulfl:
        var_rgwu = 1000000007
        var_wrnh = var_osiz(arg_xdvx[0])
        var_ayzf = var_osiz(arg_rcsn)
        var_wnki = [([0] * 26) for var_egyk in var_dcmd(var_wrnh)]
        for var_llti in arg_xdvx:
            for var_zbxo in var_dcmd(var_wrnh):
                var_wnki[var_zbxo][var_rdmc(var_llti[var_zbxo]) - var_rdmc('a')
                    ] += 1
        var_rjut = [0] * (var_ayzf + 1)
        var_lsgw = [0] * (var_ayzf + 1)
        var_rjut[0] = 1
        for var_cbvh in var_dcmd(1, var_wrnh + 1):
            var_lsgw = var_rjut.copy()
            for var_yjch in var_dcmd(1, var_ayzf + 1):
                var_dmio = var_rdmc(arg_rcsn[var_yjch - 1]) - var_rdmc('a')
                var_lsgw[var_yjch] += var_wnki[var_cbvh - 1][var_dmio
                    ] * var_rjut[var_yjch - 1] % var_rgwu
                var_lsgw[var_yjch] %= var_rgwu
            var_rjut = var_lsgw.copy()
        return var_lsgw[var_ayzf]
