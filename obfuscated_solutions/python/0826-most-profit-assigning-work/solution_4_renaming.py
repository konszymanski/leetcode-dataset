class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_rgwu]) ->var_rgwu:
        var_wrnh = var_osiz(arg_bacg)
        var_ayzf = [0] * (var_wrnh + 1)
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] <= var_wrnh:
                var_ayzf[arg_xdvx[var_wnki]] = var_osiz(var_ayzf[arg_xdvx[
                    var_wnki]], arg_rcsn[var_wnki])
        for var_wnki in var_egyk(1, var_wrnh + 1):
            var_ayzf[var_wnki] = var_osiz(var_ayzf[var_wnki], var_ayzf[
                var_wnki - 1])
        var_llti = 0
        for var_zbxo in arg_bacg:
            var_llti += var_ayzf[var_zbxo]
        return var_llti
