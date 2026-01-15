class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_hqta:
        var_bacg = 0
        while arg_xdvx:
            var_bacg += 1
            arg_xdvx //= 10
        return var_bacg & 1 == 0

    def func_rgwu(arg_ihhe, arg_wrnh: var_osiz[var_rcsn]) ->var_rcsn:
        var_ayzf = 0
        for arg_xdvx in arg_wrnh:
            if arg_ihhe.hasEvenDigits(arg_xdvx):
                var_ayzf += 1
        return var_ayzf
