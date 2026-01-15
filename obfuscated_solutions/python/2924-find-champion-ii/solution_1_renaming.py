class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [0] * arg_xdvx
        for var_wrnh in arg_rcsn:
            var_rgwu[var_wrnh[1]] += 1
        var_osiz = -1
        var_ayzf = 0
        for var_wnki in var_egyk(arg_xdvx):
            if var_rgwu[var_wnki] == 0:
                var_ayzf += 1
                var_osiz = var_wnki
        return var_osiz if var_ayzf == 1 else -1
