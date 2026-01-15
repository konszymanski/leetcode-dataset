class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz, var_ayzf = var_hqta, 0
        var_wnki, var_egyk = var_rgwu, 0
        for var_dcmd in var_llti(var_hqta):
            for var_zbxo in var_llti(var_rgwu):
                if arg_xdvx[var_dcmd][var_zbxo] == 1:
                    var_osiz = var_rdmc(var_osiz, var_dcmd)
                    var_ayzf = var_rjut(var_ayzf, var_dcmd)
                    var_wnki = var_rdmc(var_wnki, var_zbxo)
                    var_egyk = var_rjut(var_egyk, var_zbxo)
        return (var_ayzf - var_osiz + 1) * (var_egyk - var_wnki + 1)
