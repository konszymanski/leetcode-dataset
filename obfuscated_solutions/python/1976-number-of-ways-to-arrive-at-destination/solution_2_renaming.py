class Solution:
    var_udax = 1000000007

    def func_ihhe(arg_xdvx, arg_rcsn: var_hqta, arg_bacg: var_rgwu[var_rgwu
        [var_hqta]]) ->var_hqta:
        var_wrnh = [[[0, 0] for var_osiz in var_ayzf(arg_rcsn)] for
            var_osiz in var_ayzf(arg_rcsn)]
        for var_wnki in var_ayzf(arg_rcsn):
            for var_egyk in var_ayzf(arg_rcsn):
                if var_wnki != var_egyk:
                    var_wrnh[var_wnki][var_egyk][0] = var_hqta(1000000000000.0)
                    var_wrnh[var_wnki][var_egyk][1] = 0
                else:
                    var_wrnh[var_wnki][var_egyk][0] = 0
                    var_wrnh[var_wnki][var_egyk][1] = 1
        for var_dcmd, var_llti, var_zbxo in arg_bacg:
            var_wrnh[var_dcmd][var_llti][0] = var_zbxo
            var_wrnh[var_llti][var_dcmd][0] = var_zbxo
            var_wrnh[var_dcmd][var_llti][1] = 1
            var_wrnh[var_llti][var_dcmd][1] = 1
        for var_rdmc in var_ayzf(arg_rcsn):
            for var_wnki in var_ayzf(arg_rcsn):
                for var_egyk in var_ayzf(arg_rcsn):
                    if var_wnki != var_rdmc and var_egyk != var_rdmc:
                        var_rjut = var_wrnh[var_wnki][var_rdmc][0] + var_wrnh[
                            var_rdmc][var_egyk][0]
                        if var_rjut < var_wrnh[var_wnki][var_egyk][0]:
                            var_wrnh[var_wnki][var_egyk][0] = var_rjut
                            var_wrnh[var_wnki][var_egyk][1] = var_wrnh[var_wnki
                                ][var_rdmc][1] * var_wrnh[var_rdmc][var_egyk][1
                                ] % arg_xdvx.MOD
                        elif var_rjut == var_wrnh[var_wnki][var_egyk][0]:
                            var_wrnh[var_wnki][var_egyk][1] = (var_wrnh[
                                var_wnki][var_egyk][1] + var_wrnh[var_wnki]
                                [var_rdmc][1] * var_wrnh[var_rdmc][var_egyk][1]
                                ) % arg_xdvx.MOD
        return var_wrnh[arg_rcsn - 1][0][1]
