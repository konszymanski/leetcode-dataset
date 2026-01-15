class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = [([0] * (arg_xdvx + 1)) for var_wrnh in var_osiz(
            arg_xdvx + 1)]
        var_rgwu[0][0] = 1
        for var_ayzf in var_osiz(1, arg_xdvx + 1):
            var_wnki = var_ayzf ** arg_rcsn
            for var_egyk in var_osiz(arg_xdvx + 1):
                var_rgwu[var_ayzf][var_egyk] = var_rgwu[var_ayzf - 1][var_egyk]
                if var_egyk >= var_wnki:
                    var_rgwu[var_ayzf][var_egyk] = (var_rgwu[var_ayzf][
                        var_egyk] + var_rgwu[var_ayzf - 1][var_egyk - var_wnki]
                        ) % var_hqta
        return var_rgwu[arg_xdvx][arg_xdvx]
