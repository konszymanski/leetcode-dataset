class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = {}
        for var_ayzf in arg_xdvx:
            var_wrnh += var_ayzf
            if var_wrnh == arg_rcsn:
                var_rgwu += 1
            if var_wrnh - arg_rcsn in var_osiz:
                var_rgwu += var_osiz[var_wrnh - arg_rcsn]
            var_osiz[var_wrnh] = var_osiz.get(var_wrnh, 0) + 1
        return var_rgwu
