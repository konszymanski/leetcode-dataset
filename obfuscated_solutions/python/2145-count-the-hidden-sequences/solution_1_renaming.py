class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz = var_ayzf = 0
        for var_wnki in arg_xdvx:
            var_ayzf += var_wnki
            var_wrnh = var_egyk(var_wrnh, var_ayzf)
            var_osiz = var_dcmd(var_osiz, var_ayzf)
            if var_osiz - var_wrnh > arg_bacg - arg_rcsn:
                return 0
        return arg_bacg - arg_rcsn - (var_osiz - var_wrnh) + 1
