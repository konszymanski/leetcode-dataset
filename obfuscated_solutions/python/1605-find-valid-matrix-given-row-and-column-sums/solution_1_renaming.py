class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_hqta(arg_rcsn)
        var_wrnh = [0] * var_bacg
        var_osiz = [0] * var_rgwu
        var_ayzf = [([0] * var_rgwu) for var_wnki in var_egyk(var_bacg)]
        for var_dcmd in var_egyk(var_bacg):
            for var_llti in var_egyk(var_rgwu):
                var_ayzf[var_dcmd][var_llti] = var_zbxo(arg_xdvx[var_dcmd] -
                    var_wrnh[var_dcmd], arg_rcsn[var_llti] - var_osiz[var_llti]
                    )
                var_wrnh[var_dcmd] += var_ayzf[var_dcmd][var_llti]
                var_osiz[var_llti] += var_ayzf[var_dcmd][var_llti]
        return var_ayzf
