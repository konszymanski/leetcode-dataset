class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = {}
        for var_hqta in arg_xdvx:
            var_bacg[var_hqta] = var_bacg.get(var_hqta, 0) + 1
        var_rgwu = 0
        var_wrnh = False
        for var_osiz in var_bacg.values():
            if var_osiz % 2 == 0:
                var_rgwu += var_osiz
            else:
                var_rgwu += var_osiz - 1
                var_wrnh = True
        if var_wrnh:
            return var_rgwu + 1
        return var_rgwu
