class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = arg_xdvx // 7
        var_hqta = 28
        var_rgwu = 28 + (var_bacg - 1) * 7
        var_wrnh = var_bacg * (var_hqta + var_rgwu) // 2
        var_osiz = 1 + var_bacg
        var_ayzf = 0
        for var_wnki in var_egyk(arg_xdvx % 7):
            var_ayzf += var_osiz + var_wnki
        return var_wrnh + var_ayzf
