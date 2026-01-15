class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh(var_wrnh(arg_xdvx), var_wrnh(arg_rcsn))
        var_osiz = [0] * var_rgwu
        for var_ayzf in arg_xdvx:
            var_osiz[var_ayzf - 1] += 1
        for var_ayzf in arg_rcsn:
            var_osiz[var_ayzf - 1] -= 1
        var_wnki = 0
        var_egyk = 0
        for var_dcmd in var_osiz:
            var_wnki += var_llti(var_egyk)
            var_egyk += var_dcmd
        return var_wnki
