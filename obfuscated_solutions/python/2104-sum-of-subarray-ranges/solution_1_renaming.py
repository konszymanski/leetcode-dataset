class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            var_wnki, var_egyk = var_dcmd.inf, -var_dcmd.inf
            for var_llti in var_ayzf(var_osiz, var_hqta):
                var_egyk = var_zbxo(var_egyk, arg_xdvx[var_llti])
                var_wnki = var_rdmc(var_wnki, arg_xdvx[var_llti])
                var_wrnh += var_egyk - var_wnki
        return var_wrnh
