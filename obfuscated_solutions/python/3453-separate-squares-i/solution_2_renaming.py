class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_lsgw:
        var_hqta = 0
        var_rgwu = []
        for var_wrnh in arg_xdvx:
            var_osiz, var_ayzf = var_wrnh[1], var_wrnh[2]
            var_hqta += var_ayzf * var_ayzf
            var_rgwu.append((var_osiz, var_ayzf, 1))
            var_rgwu.append((var_osiz + var_ayzf, var_ayzf, -1))
        var_rgwu.sort(key=lambda x: var_wnki[0])
        var_egyk = 0.0
        var_dcmd = 0.0
        var_llti = 0.0
        for var_osiz, var_ayzf, var_zbxo in var_rgwu:
            var_rdmc = var_osiz - var_llti
            var_rjut = var_egyk * var_rdmc
            if 2 * (var_dcmd + var_rjut) >= var_hqta:
                return var_llti + (var_hqta - 2 * var_dcmd) / (2 * var_egyk)
            var_egyk += var_zbxo * var_ayzf
            var_dcmd += var_rjut
            var_llti = var_osiz
        return 0.0
