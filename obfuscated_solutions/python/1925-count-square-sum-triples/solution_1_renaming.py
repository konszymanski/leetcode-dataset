from math import sqrt


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        for var_hqta in var_rgwu(1, arg_xdvx + 1):
            for var_wrnh in var_rgwu(1, arg_xdvx + 1):
                var_osiz = var_rcsn(var_ayzf(var_hqta ** 2 + var_wrnh ** 2 + 1)
                    )
                if (var_osiz <= arg_xdvx and var_osiz ** 2 == var_hqta ** 2 +
                    var_wrnh ** 2):
                    var_bacg += 1
        return var_bacg
