class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0
            ], [2, 6], [1, 3], [2, 4]]
        var_hqta = 10 ** 9 + 7
        var_rgwu = [([0] * 10) for var_wrnh in var_osiz(arg_xdvx)]
        for var_ayzf in var_osiz(10):
            var_rgwu[0][var_ayzf] = 1
        for var_wnki in var_osiz(1, arg_xdvx):
            for var_ayzf in var_osiz(10):
                var_egyk = 0
                for var_dcmd in var_bacg[var_ayzf]:
                    var_egyk = (var_egyk + var_rgwu[var_wnki - 1][var_dcmd]
                        ) % var_hqta
                var_rgwu[var_wnki][var_ayzf] = var_egyk
        var_egyk = 0
        for var_ayzf in var_osiz(10):
            var_egyk = (var_egyk + var_rgwu[arg_xdvx - 1][var_ayzf]) % var_hqta
        return var_egyk
