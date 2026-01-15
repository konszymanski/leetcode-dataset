class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti:
        var_bacg = var_hqta(arg_xdvx / 25)
        var_rgwu = {}

        def func_wrnh(arg_osiz, arg_ayzf):
            return (var_rgwu[var_wnki(0, arg_osiz - 4)][arg_ayzf] +
                var_rgwu[var_wnki(0, arg_osiz - 3)][arg_ayzf - 1] +
                var_rgwu[var_wnki(0, arg_osiz - 2)][var_wnki(0, arg_ayzf - 
                2)] + var_rgwu[arg_osiz - 1][var_wnki(0, arg_ayzf - 3)]) / 4
        var_rgwu[0] = {(0): 0.5}
        for var_egyk in var_dcmd(1, var_bacg + 1):
            var_rgwu[0][var_egyk] = 1
            var_rgwu[var_egyk] = {(0): 0}
            for arg_ayzf in var_dcmd(1, var_egyk + 1):
                var_rgwu[arg_ayzf][var_egyk] = func_wrnh(arg_ayzf, var_egyk)
                var_rgwu[var_egyk][arg_ayzf] = func_wrnh(var_egyk, arg_ayzf)
            if var_rgwu[var_egyk][var_egyk] > 1 - 1e-05:
                return 1
        return var_rgwu[var_bacg][var_bacg]
