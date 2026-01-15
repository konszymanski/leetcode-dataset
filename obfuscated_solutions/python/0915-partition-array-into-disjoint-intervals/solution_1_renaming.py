class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [None] * var_hqta
        var_osiz = [None] * var_hqta
        var_wrnh[0] = arg_xdvx[0]
        var_osiz[-1] = arg_xdvx[-1]
        for var_ayzf in var_wnki(1, var_hqta):
            var_wrnh[var_ayzf] = var_egyk(var_wrnh[var_ayzf - 1], arg_xdvx[
                var_ayzf])
        for var_ayzf in var_wnki(var_hqta - 2, -1, -1):
            var_osiz[var_ayzf] = var_dcmd(var_osiz[var_ayzf + 1], arg_xdvx[
                var_ayzf])
        for var_ayzf in var_wnki(1, var_hqta):
            if var_wrnh[var_ayzf - 1] <= var_osiz[var_ayzf]:
                return var_ayzf
