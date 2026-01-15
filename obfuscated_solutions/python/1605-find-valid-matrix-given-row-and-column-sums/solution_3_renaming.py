class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_hqta(arg_rcsn)
        var_wrnh = [([0] * var_rgwu) for var_osiz in var_ayzf(var_bacg)]
        var_wnki, var_egyk = 0, 0
        while var_wnki < var_bacg and var_egyk < var_rgwu:
            var_wrnh[var_wnki][var_egyk] = var_dcmd(arg_xdvx[var_wnki],
                arg_rcsn[var_egyk])
            arg_xdvx[var_wnki] -= var_wrnh[var_wnki][var_egyk]
            arg_rcsn[var_egyk] -= var_wrnh[var_wnki][var_egyk]
            if arg_xdvx[var_wnki] == 0:
                var_wnki += 1
            else:
                var_egyk += 1
        return var_wrnh
