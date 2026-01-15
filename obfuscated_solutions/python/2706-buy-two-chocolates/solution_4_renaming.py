class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [0] * 101
        for var_wrnh in arg_xdvx:
            var_rgwu[var_wrnh] += 1
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in var_egyk(1, 101):
            if var_rgwu[var_wnki] > 1:
                var_osiz = var_wnki
                var_ayzf = var_wnki
                break
            elif var_rgwu[var_wnki] == 1:
                var_osiz = var_wnki
                break
        if var_ayzf == 0:
            for var_wnki in var_egyk(var_osiz + 1, 101):
                if var_rgwu[var_wnki] > 0:
                    var_ayzf = var_wnki
                    break
        var_dcmd = var_osiz + var_ayzf
        if var_dcmd <= arg_rcsn:
            return arg_rcsn - var_dcmd
        return arg_rcsn
