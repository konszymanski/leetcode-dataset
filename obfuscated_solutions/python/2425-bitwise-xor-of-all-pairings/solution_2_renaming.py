class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu, var_wrnh = 0, 0
        var_osiz, var_ayzf = var_wnki(arg_xdvx), var_wnki(arg_rcsn)
        if var_ayzf % 2:
            for var_egyk in arg_xdvx:
                var_rgwu ^= var_egyk
        if var_osiz % 2:
            for var_egyk in arg_rcsn:
                var_wrnh ^= var_egyk
        return var_rgwu ^ var_wrnh
