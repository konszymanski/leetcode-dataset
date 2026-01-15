class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = arg_xdvx[:]
        var_rgwu = arg_xdvx[:]
        for var_wrnh in var_osiz(1, var_rcsn):
            var_hqta[var_wrnh] = var_ayzf(var_hqta[var_wrnh - 1], var_hqta[
                var_wrnh])
        for var_wrnh in var_osiz(var_rcsn - 2, -1, -1):
            var_rgwu[var_wrnh] = var_wnki(var_rgwu[var_wrnh + 1], var_rgwu[
                var_wrnh])
        var_egyk = 0
        for var_wrnh in var_osiz(var_rcsn):
            if var_wrnh == 0 or var_rgwu[var_wrnh] > var_hqta[var_wrnh - 1]:
                var_egyk += 1
        return var_egyk
