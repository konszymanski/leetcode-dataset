class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rjut:
        var_bacg = 0
        var_hqta = -1
        var_rgwu = ''
        var_wrnh = [[-1, -1, -1] for var_osiz in var_ayzf(26)]
        for var_wnki in arg_xdvx:
            if var_wnki == var_rgwu:
                var_bacg += 1
            else:
                var_bacg = 1
                var_rgwu = var_wnki
            var_egyk = var_dcmd(var_wrnh[var_llti(var_wnki) - var_llti('a')])
            if var_bacg > var_egyk:
                var_wrnh[var_llti(var_wnki) - var_llti('a')][var_wrnh[
                    var_llti(var_wnki) - var_llti('a')].index(var_egyk)
                    ] = var_bacg
        for var_zbxo in var_ayzf(26):
            var_hqta = var_rdmc(var_hqta, var_dcmd(var_wrnh[var_zbxo]))
        return var_hqta
