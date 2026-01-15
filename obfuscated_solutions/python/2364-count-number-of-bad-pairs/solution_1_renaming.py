class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = {}
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_wnki = var_wrnh - arg_xdvx[var_wrnh]
            var_egyk = var_rgwu.get(var_wnki, 0)
            var_hqta += var_wrnh - var_egyk
            var_rgwu[var_wnki] = var_egyk + 1
        return var_hqta
