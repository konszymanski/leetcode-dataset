class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg, var_hqta, var_rgwu = False, False, False
        var_wrnh = var_osiz(arg_xdvx[0])
        for var_ayzf in var_wnki(var_osiz(arg_xdvx) - 1, 0, -1):
            var_bacg |= 'M' in arg_xdvx[var_ayzf]
            var_hqta |= 'P' in arg_xdvx[var_ayzf]
            var_rgwu |= 'G' in arg_xdvx[var_ayzf]
            var_wrnh += arg_rcsn[var_ayzf - 1] * (var_egyk(var_bacg) +
                var_egyk(var_hqta) + var_egyk(var_rgwu)) + var_osiz(arg_xdvx
                [var_ayzf])
        return var_wrnh
