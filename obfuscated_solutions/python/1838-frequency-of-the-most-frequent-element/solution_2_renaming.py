class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            var_egyk = arg_xdvx[var_osiz]
            var_wrnh += var_egyk
            if (var_osiz - var_rgwu + 1) * var_egyk - var_wrnh > arg_rcsn:
                var_wrnh -= arg_xdvx[var_rgwu]
                var_rgwu += 1
        return var_wnki(arg_xdvx) - var_rgwu
