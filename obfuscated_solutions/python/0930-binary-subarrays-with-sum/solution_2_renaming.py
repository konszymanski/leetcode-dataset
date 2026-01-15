class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu, var_wrnh, var_osiz = 0, 0, 0
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            var_wrnh += arg_xdvx[var_ayzf]
            while var_rgwu <= var_ayzf and var_wrnh > arg_rcsn:
                var_wrnh -= arg_xdvx[var_rgwu]
                var_rgwu += 1
            var_osiz += var_ayzf - var_rgwu + 1
        return var_osiz

    def func_dcmd(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        return arg_ihhe.sliding_window_at_most(arg_xdvx, arg_rcsn
            ) - arg_ihhe.sliding_window_at_most(arg_xdvx, arg_rcsn - 1)
