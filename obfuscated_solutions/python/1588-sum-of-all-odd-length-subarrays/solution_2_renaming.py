class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            var_wnki = 0
            for var_egyk in var_ayzf(var_osiz, var_hqta):
                var_wnki += arg_xdvx[var_egyk]
                var_wrnh += var_wnki if (var_egyk - var_osiz + 1
                    ) % 2 == 1 else 0
        return var_wrnh
