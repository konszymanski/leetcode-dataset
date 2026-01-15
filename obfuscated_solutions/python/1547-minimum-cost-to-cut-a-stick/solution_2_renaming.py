class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        var_rgwu = var_wrnh(arg_rcsn)
        arg_rcsn = [0] + var_osiz(arg_rcsn) + [arg_xdvx]
        var_ayzf = [([0] * (var_rgwu + 2)) for var_wnki in var_egyk(
            var_rgwu + 2)]
        for var_dcmd in var_egyk(2, var_rgwu + 2):
            for var_llti in var_egyk(var_rgwu + 2 - var_dcmd):
                var_zbxo = var_llti + var_dcmd
                var_rdmc = var_rjut('inf')
                for var_lsgw in var_egyk(var_llti + 1, var_zbxo):
                    var_rdmc = var_cbvh(var_rdmc, var_ayzf[var_llti][
                        var_lsgw] + var_ayzf[var_lsgw][var_zbxo] + arg_rcsn
                        [var_zbxo] - arg_rcsn[var_llti])
                var_ayzf[var_llti][var_zbxo] = var_rdmc
        return var_ayzf[0][var_rgwu + 1]
