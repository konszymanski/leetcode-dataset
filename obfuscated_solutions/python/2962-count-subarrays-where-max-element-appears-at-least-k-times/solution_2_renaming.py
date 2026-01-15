class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = []
        var_ayzf = 0
        for var_wnki, var_egyk in var_dcmd(arg_xdvx):
            if var_egyk == var_rgwu:
                var_osiz.append(var_wnki)
            var_llti = var_zbxo(var_osiz)
            if var_llti >= arg_rcsn:
                var_ayzf += var_osiz[-arg_rcsn] + 1
        return var_ayzf
