class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(values)
        var_hqta = values[0]
        var_rgwu = 0
        for var_wrnh in var_osiz(1, var_rcsn):
            var_ayzf = values[var_wrnh] - var_wrnh
            var_rgwu = var_wnki(var_rgwu, var_hqta + var_ayzf)
            var_egyk = values[var_wrnh] + var_wrnh
            var_hqta = var_wnki(var_hqta, var_egyk)
        return var_rgwu
