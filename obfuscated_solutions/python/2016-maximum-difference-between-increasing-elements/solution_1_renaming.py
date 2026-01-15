class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz = -1, arg_xdvx[0]
        for var_ayzf in var_wnki(1, var_hqta):
            if arg_xdvx[var_ayzf] > var_osiz:
                var_wrnh = var_egyk(var_wrnh, arg_xdvx[var_ayzf] - var_osiz)
            else:
                var_osiz = arg_xdvx[var_ayzf]
        return var_wrnh
