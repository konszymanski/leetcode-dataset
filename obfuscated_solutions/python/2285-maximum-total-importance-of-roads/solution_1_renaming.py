class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [0] * arg_xdvx
        for var_wrnh in arg_rcsn:
            var_rgwu[var_wrnh[0]] += 1
            var_rgwu[var_wrnh[1]] += 1
        var_rgwu.sort()
        var_osiz = 1
        var_ayzf = 0
        for var_wnki in var_rgwu:
            var_ayzf += var_osiz * var_wnki
            var_osiz += 1
        return var_ayzf
