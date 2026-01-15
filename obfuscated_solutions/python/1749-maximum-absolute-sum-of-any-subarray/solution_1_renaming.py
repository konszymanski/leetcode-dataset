class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg('inf')
        var_hqta = var_bacg('-inf')
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            var_rgwu += var_osiz
            var_rcsn = var_ayzf(var_rcsn, var_rgwu)
            var_hqta = var_wnki(var_hqta, var_rgwu)
            if var_rgwu >= 0:
                var_wrnh = var_wnki(var_wrnh, var_wnki(var_rgwu, var_rgwu -
                    var_rcsn))
            elif var_rgwu <= 0:
                var_wrnh = var_wnki(var_wrnh, var_wnki(var_egyk(var_rgwu),
                    var_egyk(var_rgwu - var_hqta)))
        return var_wrnh
