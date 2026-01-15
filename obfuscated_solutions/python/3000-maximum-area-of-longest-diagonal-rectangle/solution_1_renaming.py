class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh, var_osiz in arg_xdvx:
            var_ayzf = var_wrnh * var_wrnh + var_osiz * var_osiz
            var_wnki = var_wrnh * var_osiz
            if var_ayzf > var_hqta:
                var_hqta = var_ayzf
                var_rgwu = var_wnki
            elif var_ayzf == var_hqta:
                var_rgwu = var_egyk(var_rgwu, var_wnki)
        return var_rgwu
