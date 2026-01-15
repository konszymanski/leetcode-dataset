class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_rjut]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * var_rgwu
        var_osiz[-1] = var_rgwu - 1
        for var_ayzf in var_wnki(var_rgwu - 2, -1, -1):
            if arg_xdvx[var_ayzf] % 2 != arg_xdvx[var_ayzf + 1] % 2:
                var_osiz[var_ayzf] = var_osiz[var_ayzf + 1]
            else:
                var_osiz[var_ayzf] = var_ayzf
        var_egyk = [False] * var_wrnh(arg_rcsn)
        for var_ayzf, var_dcmd in var_llti(arg_rcsn):
            var_zbxo, var_rdmc = var_dcmd
            var_egyk[var_ayzf] = var_rdmc <= var_osiz[var_zbxo]
        return var_egyk
