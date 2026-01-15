class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu = var_wrnh = 0
        for var_osiz in arg_xdvx:
            if var_hqta < var_osiz:
                var_hqta = var_osiz
                var_rgwu = var_wrnh = 0
            if var_hqta == var_osiz:
                var_wrnh += 1
            else:
                var_wrnh = 0
            var_rgwu = var_ayzf(var_rgwu, var_wrnh)
        return var_rgwu
