class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu = var_wrnh = 1
        for var_osiz in var_ayzf(var_wnki(arg_xdvx) - 1):
            if arg_xdvx[var_osiz + 1] > arg_xdvx[var_osiz]:
                var_hqta += 1
                var_rgwu = 1
            elif arg_xdvx[var_osiz + 1] < arg_xdvx[var_osiz]:
                var_rgwu += 1
                var_hqta = 1
            else:
                var_hqta = var_rgwu = 1
            var_wrnh = var_egyk(var_wrnh, var_hqta, var_rgwu)
        return var_wrnh
