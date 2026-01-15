class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_wrnh[var_rgwu], arg_hqta: var_wrnh[var_rgwu]) ->var_rgwu:
        arg_bacg.sort()
        arg_hqta.sort()
        var_osiz, var_ayzf = 1, 1
        var_wnki, var_egyk = 1, 1
        for var_dcmd in var_llti(1, var_zbxo(arg_bacg)):
            if arg_bacg[var_dcmd] == arg_bacg[var_dcmd - 1] + 1:
                var_wnki += 1
            else:
                var_wnki = 1
            var_osiz = var_rdmc(var_osiz, var_wnki)
        for var_dcmd in var_llti(1, var_zbxo(arg_hqta)):
            if arg_hqta[var_dcmd] == arg_hqta[var_dcmd - 1] + 1:
                var_egyk += 1
            else:
                var_egyk = 1
            var_ayzf = var_rdmc(var_ayzf, var_egyk)
        var_rjut = var_lsgw(var_osiz, var_ayzf) + 1
        return var_rjut * var_rjut
