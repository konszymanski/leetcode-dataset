class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(var_wrnh)
        for var_osiz in var_ayzf(var_wnki(arg_xdvx) - 1, -1, -1):
            for var_egyk in var_ayzf(var_wnki(arg_xdvx[var_osiz])):
                var_dcmd = var_osiz + var_egyk
                var_hqta[var_dcmd].append(arg_xdvx[var_osiz][var_egyk])
        var_llti = []
        var_zbxo = 0
        while var_zbxo in var_hqta:
            var_llti.extend(var_hqta[var_zbxo])
            var_zbxo += 1
        return var_llti
