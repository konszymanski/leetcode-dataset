class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        var_osiz = [0] * var_hqta
        for var_ayzf in var_wnki(1, var_hqta):
            var_wrnh[var_ayzf] = var_egyk(var_wrnh[var_ayzf - 1], arg_xdvx[
                var_ayzf - 1])
            var_osiz[var_hqta - 1 - var_ayzf] = var_egyk(var_osiz[var_hqta -
                var_ayzf], arg_xdvx[var_hqta - var_ayzf])
        var_dcmd = 0
        for var_llti in var_wnki(1, var_hqta - 1):
            var_dcmd = var_egyk(var_dcmd, (var_wrnh[var_llti] - arg_xdvx[
                var_llti]) * var_osiz[var_llti])
        return var_dcmd
