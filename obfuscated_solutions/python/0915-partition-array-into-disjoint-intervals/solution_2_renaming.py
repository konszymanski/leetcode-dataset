class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [None] * var_hqta
        var_wrnh[-1] = arg_xdvx[-1]
        for var_osiz in var_ayzf(var_hqta - 2, -1, -1):
            var_wrnh[var_osiz] = var_wnki(var_wrnh[var_osiz + 1], arg_xdvx[
                var_osiz])
        var_egyk = arg_xdvx[0]
        for var_osiz in var_ayzf(1, var_hqta):
            var_egyk = var_dcmd(var_egyk, arg_xdvx[var_osiz - 1])
            if var_egyk <= var_wrnh[var_osiz]:
                return var_osiz
