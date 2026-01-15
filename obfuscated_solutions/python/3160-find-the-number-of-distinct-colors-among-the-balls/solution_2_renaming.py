class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_hqta[var_bacg]:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = []
        var_ayzf = {}
        var_wnki = {}
        for var_egyk in var_dcmd(var_rgwu):
            var_llti, var_zbxo = arg_rcsn[var_egyk]
            if var_llti in var_wnki:
                var_rdmc = var_wnki[var_llti]
                var_ayzf[var_rdmc] -= 1
                if var_ayzf[var_rdmc] == 0:
                    del var_ayzf[var_rdmc]
            var_wnki[var_llti] = var_zbxo
            var_ayzf[var_zbxo] = var_ayzf.get(var_zbxo, 0) + 1
            var_osiz.append(var_wrnh(var_ayzf))
        return var_osiz
