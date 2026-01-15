class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            var_rgwu = var_rgwu ^ var_wrnh
        var_osiz = 0
        while arg_rcsn or var_rgwu:
            if arg_rcsn % 2 != var_rgwu % 2:
                var_osiz += 1
            arg_rcsn //= 2
            var_rgwu //= 2
        return var_osiz
