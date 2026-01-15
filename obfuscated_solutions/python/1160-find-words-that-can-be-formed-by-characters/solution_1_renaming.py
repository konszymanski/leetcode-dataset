class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_osiz:
        var_rgwu = var_wrnh(var_osiz)
        for var_ayzf in arg_rcsn:
            var_rgwu[var_ayzf] += 1
        var_wnki = 0
        for var_egyk in arg_xdvx:
            var_dcmd = var_wrnh(var_osiz)
            for var_ayzf in var_egyk:
                var_dcmd[var_ayzf] += 1
            var_llti = True
            for var_ayzf, var_zbxo in var_dcmd.items():
                if var_rgwu[var_ayzf] < var_zbxo:
                    var_llti = False
                    break
            if var_llti:
                var_wnki += var_rdmc(var_egyk)
        return var_wnki
