class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [(arg_xdvx[var_ayzf] + arg_xdvx[var_ayzf + 1]) for
            var_ayzf in var_wnki(var_rgwu - 1)]
        var_osiz.sort()
        var_egyk = 0
        for var_ayzf in var_wnki(arg_rcsn - 1):
            var_egyk += var_osiz[var_rgwu - 2 - var_ayzf] - var_osiz[var_ayzf]
        return var_egyk
