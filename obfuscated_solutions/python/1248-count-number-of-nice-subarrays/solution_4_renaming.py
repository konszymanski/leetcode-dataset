class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        return arg_ihhe.atMost(arg_xdvx, arg_rcsn) - arg_ihhe.atMost(arg_xdvx,
            arg_rcsn - 1)

    def func_rgwu(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_wrnh, var_osiz, var_ayzf = 0, 0, 0
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            var_wrnh += arg_xdvx[var_wnki] % 2
            while var_wrnh > arg_rcsn:
                var_wrnh -= arg_xdvx[var_ayzf] % 2
                var_ayzf += 1
            var_osiz += var_wnki - var_ayzf + 1
        return var_osiz
