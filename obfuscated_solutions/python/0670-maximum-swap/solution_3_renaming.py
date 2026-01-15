class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(var_bacg)
        var_osiz = [-1] * 10
        for var_ayzf in var_wnki(var_rgwu):
            var_osiz[var_rcsn(var_bacg[var_ayzf])] = var_ayzf
        for var_ayzf in var_wnki(var_rgwu):
            for var_egyk in var_wnki(9, var_rcsn(var_bacg[var_ayzf]), -1):
                if var_osiz[var_egyk] > var_ayzf:
                    var_bacg = var_dcmd(var_bacg)
                    var_bacg[var_ayzf], var_bacg[var_osiz[var_egyk]
                        ] = var_bacg[var_osiz[var_egyk]], var_bacg[var_ayzf]
                    var_bacg = ''.join(var_bacg)
                    return var_rcsn(var_bacg)
        return arg_xdvx
