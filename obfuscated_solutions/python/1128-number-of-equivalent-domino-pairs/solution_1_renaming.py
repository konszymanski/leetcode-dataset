class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = [0] * 100
        var_rgwu = 0
        for var_wrnh, var_osiz in arg_xdvx:
            var_ayzf = (var_wrnh * 10 + var_osiz if var_wrnh <= var_osiz else
                var_osiz * 10 + var_wrnh)
            var_rgwu += var_hqta[var_ayzf]
            var_hqta[var_ayzf] += 1
        return var_rgwu
