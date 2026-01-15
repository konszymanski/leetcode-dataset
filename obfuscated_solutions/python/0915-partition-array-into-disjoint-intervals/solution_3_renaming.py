class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = arg_xdvx[0]
        var_rgwu = arg_xdvx[0]
        var_wrnh = 1
        for var_osiz in var_ayzf(1, var_wnki(arg_xdvx)):
            if arg_xdvx[var_osiz] < var_hqta:
                var_wrnh = var_osiz + 1
                var_hqta = var_rgwu
            else:
                var_rgwu = var_egyk(var_rgwu, arg_xdvx[var_osiz])
        return var_wrnh
