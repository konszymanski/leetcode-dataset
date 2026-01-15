class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx[0] - arg_xdvx[var_hqta - 1])
        for var_ayzf in var_wnki(var_hqta - 1):
            var_wrnh = var_egyk(var_wrnh, var_osiz(arg_xdvx[var_ayzf] -
                arg_xdvx[var_ayzf + 1]))
        return var_wrnh
