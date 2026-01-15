class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_dcmd:
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            if arg_xdvx[var_wrnh] == 0:
                var_wnki = var_wrnh == 0 or arg_xdvx[var_wrnh - 1] == 0
                var_egyk = var_wrnh == var_ayzf(arg_xdvx) - 1 or arg_xdvx[
                    var_wrnh + 1] == 0
                if var_wnki and var_egyk:
                    arg_xdvx[var_wrnh] = 1
                    var_rgwu += 1
                    if var_rgwu >= arg_rcsn:
                        return True
        return var_rgwu >= arg_rcsn
