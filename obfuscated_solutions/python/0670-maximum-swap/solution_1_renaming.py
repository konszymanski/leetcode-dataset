class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(var_bacg)
        var_osiz = arg_xdvx
        for var_ayzf in var_wnki(var_rgwu):
            for var_egyk in var_wnki(var_ayzf + 1, var_rgwu):
                var_dcmd = var_llti(var_bacg)
                var_dcmd[var_ayzf], var_dcmd[var_egyk] = var_dcmd[var_egyk
                    ], var_dcmd[var_ayzf]
                var_zbxo = var_rcsn(''.join(var_dcmd))
                var_osiz = var_rdmc(var_osiz, var_zbxo)
        return var_osiz
