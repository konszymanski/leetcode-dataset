class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_dmio:
        var_rgwu = var_wrnh(arg_xdvx[0])
        var_osiz = var_wrnh(arg_rcsn)
        var_ayzf = 1000000007
        var_wnki = [([0] * 26) for var_egyk in var_dcmd(var_rgwu)]
        for var_llti in arg_xdvx:
            for var_zbxo in var_dcmd(var_rgwu):
                var_wnki[var_zbxo][var_rdmc(var_llti[var_zbxo]) - var_rdmc('a')
                    ] += 1
        var_rjut = [([0] * (var_osiz + 1)) for var_egyk in var_dcmd(
            var_rgwu + 1)]
        for var_lsgw in var_dcmd(var_rgwu + 1):
            var_rjut[var_lsgw][0] = 1
        for var_lsgw in var_dcmd(1, var_rgwu + 1):
            for var_cbvh in var_dcmd(1, var_osiz + 1):
                var_rjut[var_lsgw][var_cbvh] = var_rjut[var_lsgw - 1][var_cbvh]
                var_yjch = var_rdmc(arg_rcsn[var_cbvh - 1]) - var_rdmc('a')
                var_rjut[var_lsgw][var_cbvh] += var_wnki[var_lsgw - 1][var_yjch
                    ] * var_rjut[var_lsgw - 1][var_cbvh - 1] % var_ayzf
                var_rjut[var_lsgw][var_cbvh] %= var_ayzf
        return var_rjut[var_rgwu][var_osiz]
