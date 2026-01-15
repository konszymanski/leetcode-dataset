class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_wrnh[var_rgwu], arg_hqta: var_wrnh[var_rgwu]) ->var_rgwu:
        var_osiz = var_ayzf(arg_bacg)
        var_wnki = 0
        var_egyk = 0
        for var_dcmd in var_llti(var_osiz):
            var_egyk += arg_hqta[var_dcmd] - arg_bacg[var_dcmd]
            var_zbxo = 0 if var_dcmd <= arg_rcsn - 1 else arg_hqta[var_dcmd -
                arg_rcsn]
            var_rdmc = arg_xdvx if var_dcmd == var_osiz - 1 else arg_bacg[
                var_dcmd + 1]
            var_wnki = var_rjut(var_wnki, var_rdmc - var_zbxo - var_egyk)
            if var_dcmd >= arg_rcsn - 1:
                var_egyk -= arg_hqta[var_dcmd - arg_rcsn + 1] - arg_bacg[
                    var_dcmd - arg_rcsn + 1]
        return var_wnki
