class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:

        @var_egyk
        def func_bacg(arg_hqta, arg_rgwu):
            if arg_hqta == 0:
                return 1
            var_wrnh = 0
            for var_osiz in var_ayzf[arg_rgwu]:
                var_wrnh = (var_wrnh + func_bacg(arg_hqta - 1, var_osiz)
                    ) % var_wnki
            return var_wrnh
        var_ayzf = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0
            ], [2, 6], [1, 3], [2, 4]]
        var_wrnh = 0
        var_wnki = 10 ** 9 + 7
        for arg_rgwu in var_dcmd(10):
            var_wrnh = (var_wrnh + func_bacg(arg_xdvx - 1, arg_rgwu)
                ) % var_wnki
        return var_wrnh
