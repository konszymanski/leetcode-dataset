class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        if var_rgwu(arg_xdvx) == 1:
            return 1
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * (var_wrnh + 1)
        for var_wnki in arg_xdvx:
            var_ayzf[var_osiz(var_wnki - arg_rcsn, 0)] += 1
            if var_wnki + arg_rcsn + 1 <= var_wrnh:
                var_ayzf[var_wnki + arg_rcsn + 1] -= 1
        var_egyk = 0
        var_dcmd = 0
        for var_llti in var_ayzf:
            var_dcmd += var_llti
            var_egyk = var_osiz(var_egyk, var_dcmd)
        return var_egyk
