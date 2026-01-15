class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = var_hqta()
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            if var_wrnh in var_bacg:
                var_bacg.remove(var_wrnh)
                var_rgwu += 2
            else:
                var_bacg.add(var_wrnh)
        if var_bacg:
            var_rgwu += 1
        return var_rgwu
