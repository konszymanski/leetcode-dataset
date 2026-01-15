class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_bacg - 1, 0, -1):
            var_wnki = var_egyk(arg_xdvx[var_osiz]) + var_wrnh
            if var_wnki % 2 == 1:
                var_rgwu += 2
                var_wrnh = 1
            else:
                var_rgwu += 1
        return var_rgwu + var_wrnh
