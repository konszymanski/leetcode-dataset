class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_hqta
        var_osiz = var_ayzf(var_wnki(arg_xdvx))
        var_egyk = 0
        for var_dcmd in var_llti(var_rgwu(var_osiz)):
            while var_egyk < var_rgwu(var_osiz) and var_osiz[var_egyk
                ] < var_osiz[var_dcmd] + var_hqta:
                var_egyk += 1
            var_zbxo = var_egyk - var_dcmd
            var_wrnh = var_rdmc(var_wrnh, var_hqta - var_zbxo)
        return var_wrnh
