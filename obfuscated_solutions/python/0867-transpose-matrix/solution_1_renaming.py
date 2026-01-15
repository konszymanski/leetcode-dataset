class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = [([None] * var_hqta) for var_ayzf in var_wnki(var_rgwu)]
        for var_egyk, var_dcmd in var_llti(arg_xdvx):
            for var_zbxo, var_rdmc in var_llti(var_dcmd):
                var_osiz[var_zbxo][var_egyk] = var_rdmc
        return var_osiz
