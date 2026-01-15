class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        if var_rgwu % arg_rcsn == 0:
            return 0
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = var_osiz
        for var_egyk in var_dcmd(var_osiz):
            var_llti = 0
            for var_zbxo in var_dcmd(var_egyk, var_osiz):
                var_llti += arg_xdvx[var_zbxo]
                var_rdmc = (var_rgwu - var_llti) % arg_rcsn
                if var_rdmc == 0:
                    var_wnki = var_rjut(var_wnki, var_zbxo - var_egyk + 1)
        return var_wnki if var_wnki != var_osiz else -1
