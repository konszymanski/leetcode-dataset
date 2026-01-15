class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_osiz, var_hqta):
                if (var_wnki - var_osiz + 1) % 2 == 1:
                    var_egyk = 0
                    for var_dcmd in var_ayzf(var_osiz, var_wnki + 1):
                        var_egyk += arg_xdvx[var_dcmd]
                    var_wrnh += var_egyk
        return var_wrnh
