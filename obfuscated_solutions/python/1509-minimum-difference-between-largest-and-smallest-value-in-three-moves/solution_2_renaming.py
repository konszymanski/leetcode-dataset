class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        if var_hqta <= 4:
            return 0
        var_wrnh = var_osiz(var_ayzf.nsmallest(4, arg_xdvx))
        var_wnki = var_osiz(var_ayzf.nlargest(4, arg_xdvx))
        var_egyk = var_dcmd('inf')
        for var_llti in var_zbxo(4):
            var_egyk = var_rdmc(var_egyk, var_wnki[var_llti] - var_wrnh[
                var_llti])
        return var_egyk
