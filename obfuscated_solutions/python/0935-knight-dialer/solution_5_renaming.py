class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if arg_xdvx == 1:
            return 10

        def func_bacg(arg_hqta, arg_rgwu):
            var_wrnh = [([0] * var_osiz(arg_rgwu[0])) for var_ayzf in
                var_wnki(var_osiz(arg_hqta))]
            for var_egyk in var_wnki(var_osiz(arg_hqta)):
                for var_dcmd in var_wnki(var_osiz(arg_rgwu[0])):
                    for var_llti in var_wnki(var_osiz(arg_rgwu)):
                        var_wrnh[var_egyk][var_dcmd] = (var_wrnh[var_egyk][
                            var_dcmd] + arg_hqta[var_egyk][var_llti] *
                            arg_rgwu[var_llti][var_dcmd]) % var_zbxo
            return var_wrnh
        arg_hqta = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0,
            1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0,
            1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0,
            0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0,
            0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0,
            0, 0]]
        var_rdmc = [[1] * 10]
        var_zbxo = 10 ** 9 + 7
        arg_xdvx -= 1
        while arg_xdvx:
            if arg_xdvx & 1:
                var_rdmc = func_bacg(var_rdmc, arg_hqta)
            arg_hqta = func_bacg(arg_hqta, arg_hqta)
            arg_xdvx >>= 1
        return var_rjut(var_rdmc[0]) % var_zbxo
