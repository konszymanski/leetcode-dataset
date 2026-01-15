class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            for var_ayzf in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                var_hqta = var_wnki(var_hqta, (arg_xdvx[var_rgwu] - 1) * (
                    arg_xdvx[var_ayzf] - 1))
        return var_hqta
