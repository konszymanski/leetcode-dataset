class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 1
        var_hqta = 1
        var_rgwu = 0
        while var_hqta <= arg_xdvx:
            var_rgwu += (var_bacg + 1) // 2 * (var_wrnh(var_hqta * 2 - 1,
                arg_xdvx) - var_hqta + 1)
            var_bacg += 1
            var_hqta *= 2
        return var_rgwu

    def func_osiz(arg_ihhe, arg_ayzf: var_wnki[var_wnki[var_rcsn]]) ->var_rcsn:
        var_egyk = 0
        for var_dcmd in arg_ayzf:
            var_egyk += (arg_ihhe.get(var_dcmd[1]) - arg_ihhe.get(var_dcmd[
                0] - 1) + 1) // 2
        return var_egyk
