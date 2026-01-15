class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta()
        for var_rgwu in arg_xdvx:
            while var_rgwu not in var_bacg and var_rgwu > 0:
                var_bacg.add(var_rgwu)
                var_rgwu //= 10
        var_wrnh = 0
        for var_rgwu in arg_rcsn:
            while var_rgwu not in var_bacg and var_rgwu > 0:
                var_rgwu //= 10
            if var_rgwu > 0:
                var_wrnh = var_osiz(var_wrnh, var_ayzf(var_wnki(var_rgwu)))
        return var_wrnh
