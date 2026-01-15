class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = 0
        var_wnki = []
        for var_egyk in var_dcmd(var_rgwu(arg_xdvx)):
            var_llti = var_wrnh - var_ayzf - arg_xdvx[var_egyk]
            var_zbxo = var_egyk
            var_rdmc = var_hqta - 1 - var_egyk
            var_rjut = var_zbxo * arg_xdvx[var_egyk] - var_ayzf
            var_lsgw = var_llti - var_rdmc * arg_xdvx[var_egyk]
            var_wnki.append(var_rjut + var_lsgw)
            var_ayzf += arg_xdvx[var_egyk]
        return var_wnki
