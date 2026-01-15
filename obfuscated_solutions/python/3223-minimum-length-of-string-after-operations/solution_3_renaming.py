class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            var_rgwu = 1 << var_osiz(var_wrnh) - var_osiz('a')
            var_bacg |= var_rgwu
            var_hqta ^= var_rgwu
        var_ayzf = 0
        while var_bacg > 0:
            var_rgwu = var_bacg & var_bacg - 1
            var_ayzf += 2 - (var_hqta & var_bacg - var_rgwu != 0)
            var_bacg = var_rgwu
        return var_ayzf
