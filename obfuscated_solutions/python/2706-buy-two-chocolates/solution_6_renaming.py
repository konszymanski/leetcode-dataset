class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx[0], arg_xdvx[1])
        var_osiz = var_ayzf(arg_xdvx[0], arg_xdvx[1])
        for var_wnki in var_egyk(2, var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] < var_rgwu:
                var_osiz = var_rgwu
                var_rgwu = arg_xdvx[var_wnki]
            elif arg_xdvx[var_wnki] < var_osiz:
                var_osiz = arg_xdvx[var_wnki]
        var_llti = var_rgwu + var_osiz
        if var_llti <= arg_rcsn:
            return arg_rcsn - var_llti
        return arg_rcsn
