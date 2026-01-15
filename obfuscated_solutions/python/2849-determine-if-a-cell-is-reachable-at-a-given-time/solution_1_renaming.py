class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_wrnh,
        arg_bacg: var_wrnh, arg_hqta: var_wrnh, arg_rgwu: var_wrnh) ->var_dcmd:
        var_osiz = var_ayzf(arg_xdvx - arg_bacg)
        var_wnki = var_ayzf(arg_rcsn - arg_hqta)
        if var_osiz == 0 and var_wnki == 0 and arg_rgwu == 1:
            return False
        return arg_rgwu >= var_egyk(var_osiz, var_wnki)
