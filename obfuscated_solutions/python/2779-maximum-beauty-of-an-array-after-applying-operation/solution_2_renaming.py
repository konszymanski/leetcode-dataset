class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            while arg_xdvx[var_osiz] - arg_xdvx[var_rgwu] > 2 * arg_rcsn:
                var_rgwu += 1
            var_wrnh = var_egyk(var_wrnh, var_osiz - var_rgwu + 1)
        return var_wrnh
