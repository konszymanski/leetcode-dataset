class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_rjut:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [[[(False) for var_osiz in var_ayzf(var_hqta)] for
            var_wnki in var_ayzf(var_hqta)] for var_egyk in var_ayzf(
            var_hqta + 1)]
        for var_wnki in var_ayzf(var_hqta):
            for var_osiz in var_ayzf(var_hqta):
                var_wrnh[1][var_wnki][var_osiz] = arg_xdvx[var_wnki
                    ] == arg_rcsn[var_osiz]
        for var_dcmd in var_ayzf(2, var_hqta + 1):
            for var_wnki in var_ayzf(var_hqta + 1 - var_dcmd):
                for var_osiz in var_ayzf(var_hqta + 1 - var_dcmd):
                    for var_llti in var_ayzf(1, var_dcmd):
                        var_zbxo = var_wrnh[var_llti][var_wnki]
                        var_rdmc = var_wrnh[var_dcmd - var_llti][var_wnki +
                            var_llti]
                        var_wrnh[var_dcmd][var_wnki][var_osiz] |= var_zbxo[
                            var_osiz] and var_rdmc[var_osiz + var_llti]
                        var_wrnh[var_dcmd][var_wnki][var_osiz] |= var_zbxo[
                            var_osiz + var_dcmd - var_llti] and var_rdmc[
                            var_osiz]
        return var_wrnh[var_hqta][0][0]
