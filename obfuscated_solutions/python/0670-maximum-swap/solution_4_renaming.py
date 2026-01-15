class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(var_rgwu(arg_xdvx))
        var_wrnh = var_osiz(var_bacg)
        var_ayzf = -1
        var_wnki = -1
        var_egyk = -1
        for var_dcmd in var_llti(var_wrnh - 1, -1, -1):
            if var_ayzf == -1 or var_bacg[var_dcmd] > var_bacg[var_ayzf]:
                var_ayzf = var_dcmd
            elif var_bacg[var_dcmd] < var_bacg[var_ayzf]:
                var_wnki = var_dcmd
                var_egyk = var_ayzf
        if var_wnki != -1 and var_egyk != -1:
            var_bacg[var_wnki], var_bacg[var_egyk] = var_bacg[var_egyk
                ], var_bacg[var_wnki]
        return var_rcsn(''.join(var_bacg))
