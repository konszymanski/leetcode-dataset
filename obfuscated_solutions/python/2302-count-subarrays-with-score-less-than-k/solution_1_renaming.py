class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz, var_ayzf = 0, 0
        var_wnki = 0
        for var_egyk in var_dcmd(var_rgwu):
            var_ayzf += arg_xdvx[var_egyk]
            while var_wnki <= var_egyk and var_ayzf * (var_egyk - var_wnki + 1
                ) >= arg_rcsn:
                var_ayzf -= arg_xdvx[var_wnki]
                var_wnki += 1
            var_osiz += var_egyk - var_wnki + 1
        return var_osiz
