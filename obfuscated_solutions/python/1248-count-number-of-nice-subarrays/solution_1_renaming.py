class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = {var_rgwu: 1}
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            var_rgwu += arg_xdvx[var_ayzf] % 2
            if var_rgwu - arg_rcsn in var_osiz:
                var_wrnh = var_wrnh + var_osiz[var_rgwu - arg_rcsn]
            var_osiz[var_rgwu] = var_osiz.get(var_rgwu, 0) + 1
        return var_wrnh
