class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        var_hqta = 2
        while arg_xdvx > 1:
            while arg_xdvx % var_hqta == 0:
                var_bacg += var_hqta
                arg_xdvx //= var_hqta
            var_hqta += 1
        return var_bacg
