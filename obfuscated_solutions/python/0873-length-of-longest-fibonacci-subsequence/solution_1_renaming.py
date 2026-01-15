class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = var_ayzf(arg_xdvx)
        for var_wnki in var_egyk(var_osiz):
            for var_dcmd in var_egyk(var_wnki + 1, var_osiz):
                var_llti = arg_xdvx[var_dcmd]
                var_zbxo = arg_xdvx[var_wnki] + arg_xdvx[var_dcmd]
                var_rdmc = 2
                while var_zbxo in var_hqta:
                    var_llti, var_zbxo = var_zbxo, var_zbxo + var_llti
                    var_rdmc += 1
                    var_wrnh = var_rjut(var_wrnh, var_rdmc)
        return var_wrnh
