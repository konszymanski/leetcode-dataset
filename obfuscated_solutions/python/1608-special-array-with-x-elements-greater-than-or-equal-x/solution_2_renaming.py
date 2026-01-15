class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * (var_hqta + 1)
        for var_osiz in arg_xdvx:
            var_wrnh[var_ayzf(var_hqta, var_osiz)] += 1
        var_wnki = 0
        for var_egyk in var_dcmd(var_hqta, 0, -1):
            var_wnki += var_wrnh[var_egyk]
            if var_egyk == var_wnki:
                return var_egyk
        return -1
