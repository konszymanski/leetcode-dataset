class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 1000000007
        var_hqta = [[([0] * 3) for var_rgwu in var_wrnh(2)] for var_rgwu in
            var_wrnh(arg_xdvx + 1)]
        var_hqta[0][0][0] = 1
        for var_osiz in var_wrnh(arg_xdvx):
            for var_ayzf in var_wrnh(2):
                for var_wnki in var_wrnh(3):
                    var_hqta[var_osiz + 1][var_ayzf][0] = (var_hqta[
                        var_osiz + 1][var_ayzf][0] + var_hqta[var_osiz][
                        var_ayzf][var_wnki]) % var_bacg
                    if var_ayzf < 1:
                        var_hqta[var_osiz + 1][var_ayzf + 1][0] = (var_hqta
                            [var_osiz + 1][var_ayzf + 1][0] + var_hqta[
                            var_osiz][var_ayzf][var_wnki]) % var_bacg
                    if var_wnki < 2:
                        var_hqta[var_osiz + 1][var_ayzf][var_wnki + 1] = (
                            var_hqta[var_osiz + 1][var_ayzf][var_wnki + 1] +
                            var_hqta[var_osiz][var_ayzf][var_wnki]) % var_bacg
        var_egyk = 0
        for var_ayzf in var_wrnh(2):
            for var_wnki in var_wrnh(3):
                var_egyk = (var_egyk + var_hqta[arg_xdvx][var_ayzf][var_wnki]
                    ) % var_bacg
        return var_egyk
