class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = 0
        for var_wnki in var_egyk(1, arg_rcsn + 1):
            if var_wnki in var_wrnh:
                continue
            if arg_bacg - var_wnki < 0:
                return var_ayzf
            arg_bacg -= var_wnki
            var_ayzf += 1
        return var_ayzf
