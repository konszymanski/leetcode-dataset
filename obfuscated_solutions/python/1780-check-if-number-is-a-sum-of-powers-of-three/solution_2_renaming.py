class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_hqta:
        var_bacg = 0
        while 3 ** var_bacg <= arg_xdvx:
            var_bacg += 1
        while arg_xdvx > 0:
            if arg_xdvx >= 3 ** var_bacg:
                arg_xdvx -= 3 ** var_bacg
            if arg_xdvx >= 3 ** var_bacg:
                return False
            var_bacg -= 1
        return True
