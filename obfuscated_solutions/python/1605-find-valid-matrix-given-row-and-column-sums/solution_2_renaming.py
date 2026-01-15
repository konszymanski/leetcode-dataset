class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_hqta(arg_rcsn)
        var_wrnh = [([0] * var_rgwu) for var_osiz in var_ayzf(var_bacg)]
        for var_wnki in var_ayzf(var_bacg):
            for var_egyk in var_ayzf(var_rgwu):
                var_wrnh[var_wnki][var_egyk] = var_dcmd(arg_xdvx[var_wnki],
                    arg_rcsn[var_egyk])
                arg_xdvx[var_wnki] -= var_wrnh[var_wnki][var_egyk]
                arg_rcsn[var_egyk] -= var_wrnh[var_wnki][var_egyk]
        return var_wrnh
