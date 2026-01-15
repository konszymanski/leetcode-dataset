class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = [0] * 26
        for var_hqta in arg_xdvx:
            var_bacg[var_rgwu(var_hqta) - var_rgwu('A')] += 1
        return arg_ihhe._find_sequences(var_bacg)

    def func_osiz(arg_ihhe, var_bacg: var_ayzf) ->var_wrnh:
        var_wnki = 0
        for var_egyk in var_dcmd(26):
            if var_bacg[var_egyk] == 0:
                continue
            var_wnki += 1
            var_bacg[var_egyk] -= 1
            var_wnki += arg_ihhe._find_sequences(var_bacg)
            var_bacg[var_egyk] += 1
        return var_wnki
