class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * (var_wrnh + 1)
        var_wnki = [0] * (var_wrnh + 1)
        for var_egyk in var_dcmd(var_wrnh):
            var_ayzf[var_egyk + 1] = var_ayzf[var_egyk] + arg_xdvx[var_egyk
                ] * arg_rcsn[var_egyk]
            var_wnki[var_egyk + 1] = var_wnki[var_egyk] + arg_xdvx[var_egyk]
        var_llti = var_ayzf[var_wrnh]
        for var_egyk in var_dcmd(arg_bacg - 1, var_wrnh):
            var_zbxo = var_ayzf[var_egyk - arg_bacg + 1]
            var_rdmc = var_ayzf[var_wrnh] - var_ayzf[var_egyk + 1]
            var_rjut = var_wnki[var_egyk + 1] - var_wnki[var_egyk - 
                arg_bacg // 2 + 1]
            var_llti = var_lsgw(var_llti, var_zbxo + var_rjut + var_rdmc)
        return var_llti
