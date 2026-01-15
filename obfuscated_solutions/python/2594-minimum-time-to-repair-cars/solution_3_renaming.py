class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [[arg_xdvx, arg_xdvx, 1, var_rgwu[arg_xdvx]] for
            arg_xdvx in var_rgwu]
        var_ayzf(var_osiz)
        while arg_rcsn > 0:
            var_wnki, arg_xdvx, var_egyk, var_rgwu = var_dcmd(var_osiz)
            arg_rcsn -= var_rgwu
            var_egyk += 1
            var_llti(var_osiz, [arg_xdvx * var_egyk * var_egyk, arg_xdvx,
                var_egyk, var_rgwu])
        return var_wnki
