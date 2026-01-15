class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [([0] * var_hqta) for var_osiz in var_ayzf(var_hqta)]
        var_wnki = 0
        for var_egyk in var_ayzf(2, var_hqta):
            var_dcmd = 0
            var_llti = var_egyk - 1
            while var_dcmd < var_llti:
                var_zbxo = arg_xdvx[var_dcmd] + arg_xdvx[var_llti]
                if var_zbxo > arg_xdvx[var_egyk]:
                    var_llti -= 1
                elif var_zbxo < arg_xdvx[var_egyk]:
                    var_dcmd += 1
                else:
                    var_wrnh[var_llti][var_egyk] = var_wrnh[var_dcmd][var_llti
                        ] + 1
                    var_wnki = var_rdmc(var_wrnh[var_llti][var_egyk], var_wnki)
                    var_llti -= 1
                    var_dcmd += 1
        return var_wnki + 2 if var_wnki else 0
