class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu):
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf in var_wnki(arg_rcsn):
            var_egyk = 0
            for var_dcmd in var_wnki(var_wrnh):
                if arg_xdvx[var_dcmd] < arg_xdvx[var_egyk]:
                    var_egyk = var_dcmd
            arg_xdvx[var_egyk] *= arg_bacg
        return arg_xdvx
