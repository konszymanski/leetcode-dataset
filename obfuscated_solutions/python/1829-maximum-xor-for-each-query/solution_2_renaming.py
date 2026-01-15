class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_rgwu = var_rgwu ^ arg_xdvx[var_wrnh]
        var_wnki = [0] * var_ayzf(arg_xdvx)
        var_egyk = (1 << arg_rcsn) - 1
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_wnki[var_wrnh] = var_rgwu ^ var_egyk
            var_rgwu = var_rgwu ^ arg_xdvx[var_ayzf(arg_xdvx) - 1 - var_wrnh]
        return var_wnki
