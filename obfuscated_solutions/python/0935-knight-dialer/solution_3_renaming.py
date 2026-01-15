class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0
            ], [2, 6], [1, 3], [2, 4]]
        var_hqta = 10 ** 9 + 7
        var_rgwu = [0] * 10
        var_wrnh = [1] * 10
        for var_osiz in var_ayzf(1, arg_xdvx):
            var_rgwu = [0] * 10
            for var_wnki in var_ayzf(10):
                var_egyk = 0
                for var_dcmd in var_bacg[var_wnki]:
                    var_egyk = (var_egyk + var_wrnh[var_dcmd]) % var_hqta
                var_rgwu[var_wnki] = var_egyk
            var_wrnh = var_rgwu
        var_egyk = 0
        for var_wnki in var_ayzf(10):
            var_egyk = (var_egyk + var_wrnh[var_wnki]) % var_hqta
        return var_egyk
