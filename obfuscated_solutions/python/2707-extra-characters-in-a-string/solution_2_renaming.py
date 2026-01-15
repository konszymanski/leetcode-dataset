class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_rjut:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(arg_rcsn)
        var_wnki = [0] * (var_wrnh(arg_xdvx) + 1)
        for var_egyk in var_dcmd(var_rgwu - 1, -1, -1):
            var_wnki[var_egyk] = 1 + var_wnki[var_egyk + 1]
            for var_llti in var_dcmd(var_egyk, var_rgwu):
                var_zbxo = arg_xdvx[var_egyk:var_llti + 1]
                if var_zbxo in var_osiz:
                    var_wnki[var_egyk] = var_rdmc(var_wnki[var_egyk],
                        var_wnki[var_llti + 1])
        return var_wnki[0]
