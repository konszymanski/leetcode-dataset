class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [var_rgwu for var_rgwu in arg_xdvx if var_rgwu % 3 == 0]
        var_wrnh = var_osiz([var_rgwu for var_rgwu in arg_xdvx if var_rgwu %
            3 == 1], reverse=True)
        var_ayzf = var_osiz([var_rgwu for var_rgwu in arg_xdvx if var_rgwu %
            3 == 2], reverse=True)
        var_wnki = 0
        var_egyk, var_dcmd = var_llti(var_wrnh), var_llti(var_ayzf)
        for var_zbxo in [var_egyk - 2, var_egyk - 1, var_egyk]:
            if var_zbxo >= 0:
                for var_rdmc in [var_dcmd - 2, var_dcmd - 1, var_dcmd]:
                    if var_rdmc >= 0 and (var_zbxo - var_rdmc) % 3 == 0:
                        var_wnki = var_rjut(var_wnki, var_lsgw(var_wrnh[:
                            var_zbxo]) + var_lsgw(var_ayzf[:var_rdmc]))
        return var_wnki + var_lsgw(var_hqta)
