class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        var_ayzf = {}
        for var_wnki in arg_xdvx:
            var_ayzf[var_wnki] = var_ayzf.get(var_wnki, 0) + var_wrnh
        for var_wnki in arg_rcsn:
            var_ayzf[var_wnki] = var_ayzf.get(var_wnki, 0) + var_rgwu
        var_egyk = 0
        for var_wnki in var_ayzf:
            if var_ayzf[var_wnki] % 2:
                var_egyk ^= var_wnki
        return var_egyk
