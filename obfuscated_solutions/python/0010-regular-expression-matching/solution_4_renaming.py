class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn: var_hqta, arg_bacg: var_hqta) ->var_llti:
        var_rgwu = [([False] * (var_wrnh(arg_bacg) + 1)) for var_osiz in
            var_ayzf(var_wrnh(arg_rcsn) + 1)]
        var_rgwu[-1][-1] = True
        for var_wnki in var_ayzf(var_wrnh(arg_rcsn), -1, -1):
            for var_egyk in var_ayzf(var_wrnh(arg_bacg) - 1, -1, -1):
                var_dcmd = var_wnki < var_wrnh(arg_rcsn) and arg_bacg[var_egyk
                    ] in {arg_rcsn[var_wnki], '.'}
                if var_egyk + 1 < var_wrnh(arg_bacg) and arg_bacg[var_egyk + 1
                    ] == '*':
                    var_rgwu[var_wnki][var_egyk] = var_rgwu[var_wnki][
                        var_egyk + 2] or var_dcmd and var_rgwu[var_wnki + 1][
                        var_egyk]
                else:
                    var_rgwu[var_wnki][var_egyk] = var_dcmd and var_rgwu[
                        var_wnki + 1][var_egyk + 1]
        return var_rgwu[0][0]
