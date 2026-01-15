class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [([0] * arg_rcsn) for var_wrnh in var_osiz(arg_rcsn)]
        var_ayzf = 0
        for var_wnki in arg_xdvx:
            var_wnki %= arg_rcsn
            for var_egyk in var_osiz(arg_rcsn):
                var_rgwu[var_egyk][var_wnki] = var_rgwu[var_wnki][var_egyk] + 1
                var_ayzf = var_dcmd(var_ayzf, var_rgwu[var_egyk][var_wnki])
        return var_ayzf
