class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        var_hqta = {}
        for var_rgwu in arg_xdvx:
            var_hqta[var_rgwu] = var_hqta.get(var_rgwu, 0) + 1
            if var_hqta[var_rgwu] % 2 == 1:
                var_bacg += 1
            else:
                var_bacg -= 1
        if var_bacg > 0:
            return var_wrnh(arg_xdvx) - var_bacg + 1
        else:
            return var_wrnh(arg_xdvx)
