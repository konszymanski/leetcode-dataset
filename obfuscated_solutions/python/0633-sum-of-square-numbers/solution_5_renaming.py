class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu:
        var_bacg = 2
        while var_bacg * var_bacg <= arg_xdvx:
            var_hqta = 0
            while arg_xdvx % var_bacg == 0:
                var_hqta += 1
                arg_xdvx //= var_bacg
            if var_bacg % 4 == 3 and var_hqta % 2 != 0:
                return False
            var_bacg += 1
        return arg_xdvx % 4 != 3
