class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh('inf')
        var_osiz = var_ayzf(arg_xdvx)
        for var_wnki in var_egyk(var_osiz):
            for var_dcmd in var_egyk(var_wnki + 1, var_osiz):
                var_llti = arg_xdvx[var_wnki] + arg_xdvx[var_dcmd]
                if var_llti < var_rgwu:
                    var_rgwu = var_llti
        if var_rgwu <= arg_rcsn:
            return arg_rcsn - var_rgwu
        else:
            return arg_rcsn
