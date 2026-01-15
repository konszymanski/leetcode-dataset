class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = 0
        var_wnki = [0] * (var_rgwu + 1)
        for var_egyk in var_dcmd(var_rgwu):
            while var_osiz + var_wnki[var_egyk] < arg_xdvx[var_egyk]:
                var_ayzf += 1
                if var_ayzf > var_wrnh(arg_rcsn):
                    return -1
                var_llti, var_zbxo, var_rdmc = arg_rcsn[var_ayzf - 1]
                if var_zbxo >= var_egyk:
                    var_wnki[var_rjut(var_llti, var_egyk)] += var_rdmc
                    var_wnki[var_zbxo + 1] -= var_rdmc
            var_osiz += var_wnki[var_egyk]
        return var_ayzf
