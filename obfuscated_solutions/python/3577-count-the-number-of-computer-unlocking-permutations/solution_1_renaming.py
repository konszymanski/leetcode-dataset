class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        for var_wrnh in var_osiz(1, var_hqta):
            if arg_xdvx[var_wrnh] <= arg_xdvx[0]:
                return 0
        var_ayzf, var_wnki = 1, 10 ** 9 + 7
        for var_wrnh in var_osiz(2, var_hqta):
            var_ayzf = var_ayzf * var_wrnh % var_wnki
        return var_ayzf
