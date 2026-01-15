class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * (var_hqta + 1)
        for var_osiz in arg_xdvx:
            var_wrnh[var_ayzf(var_osiz, var_hqta)] += 1
        var_wnki = 1
        for var_osiz in var_egyk(2, var_hqta + 1):
            var_wnki = var_ayzf(var_wnki + var_wrnh[var_osiz], var_osiz)
        return var_wnki
