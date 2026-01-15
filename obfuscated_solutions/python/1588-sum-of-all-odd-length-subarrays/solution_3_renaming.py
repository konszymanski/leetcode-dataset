class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz, var_ayzf in var_wnki(arg_xdvx):
            var_egyk, var_dcmd = var_osiz, var_hqta - var_osiz - 1
            var_wrnh += var_ayzf * (var_egyk // 2 + 1) * (var_dcmd // 2 + 1)
            var_wrnh += var_ayzf * ((var_egyk + 1) // 2) * ((var_dcmd + 1) // 2
                )
        return var_wrnh
