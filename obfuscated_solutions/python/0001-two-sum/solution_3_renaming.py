class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = {}
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_wnki = arg_rcsn - arg_xdvx[var_wrnh]
            if var_wnki in var_rgwu:
                return [var_wrnh, var_rgwu[var_wnki]]
            var_rgwu[arg_xdvx[var_wrnh]] = var_wrnh
        return []
