class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_rcsn), var_osiz(arg_rcsn[0])
        var_ayzf, var_wnki = [0] * var_rgwu, [0] * var_wrnh
        var_egyk = {}
        for var_dcmd in var_llti(var_rgwu):
            for var_zbxo in var_llti(var_wrnh):
                var_egyk[arg_rcsn[var_dcmd][var_zbxo]] = [var_dcmd, var_zbxo]
        for var_rdmc in var_llti(var_osiz(arg_xdvx)):
            var_rjut = arg_xdvx[var_rdmc]
            var_dcmd, var_zbxo = var_egyk[var_rjut]
            var_ayzf[var_dcmd] += 1
            var_wnki[var_zbxo] += 1
            if var_ayzf[var_dcmd] == var_wrnh or var_wnki[var_zbxo
                ] == var_rgwu:
                return var_rdmc
        return -1
