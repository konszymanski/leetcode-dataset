class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(var_bacg)
        for var_wrnh in arg_xdvx:
            var_hqta[var_wrnh] += 1
        var_osiz = var_ayzf(arg_xdvx) / 4
        for var_wnki, var_egyk in var_hqta.items():
            if var_egyk > var_osiz:
                return var_wnki
        return -1
