class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = arg_xdvx[0]
        for var_wrnh in var_osiz(1, var_ayzf(arg_xdvx)):
            if arg_xdvx[var_wrnh] <= arg_xdvx[var_wrnh - 1]:
                var_hqta = var_wnki(var_hqta, var_rgwu)
                var_rgwu = 0
            var_rgwu += arg_xdvx[var_wrnh]
        return var_wnki(var_hqta, var_rgwu)
