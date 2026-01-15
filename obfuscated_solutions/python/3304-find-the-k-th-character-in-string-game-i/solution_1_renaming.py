class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        while arg_xdvx != 1:
            var_hqta = arg_xdvx.bit_length() - 1
            if 1 << var_hqta == arg_xdvx:
                var_hqta -= 1
            arg_xdvx -= 1 << var_hqta
            var_bacg += 1
        return var_rgwu(var_wrnh('a') + var_bacg)
