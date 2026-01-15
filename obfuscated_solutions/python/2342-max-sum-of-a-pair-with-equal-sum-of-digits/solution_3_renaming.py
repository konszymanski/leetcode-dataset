class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = -1
        var_bacg = [0] * 82
        for var_hqta in arg_xdvx:
            var_rgwu = 0
            var_wrnh = var_hqta
            while var_wrnh:
                var_wrnh, var_osiz = var_ayzf(var_wrnh, 10)
                var_rgwu += var_osiz
            if var_bacg[var_rgwu] > 0:
                var_rcsn = var_wnki(var_rcsn, var_bacg[var_rgwu] + var_hqta)
            var_bacg[var_rgwu] = var_wnki(var_bacg[var_rgwu], var_hqta)
        return var_rcsn
