class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        while arg_xdvx > 1:
            if arg_xdvx % 2 == 0:
                var_bacg += arg_xdvx // 2
                arg_xdvx = arg_xdvx // 2
            else:
                var_bacg += (arg_xdvx - 1) // 2
                arg_xdvx = (arg_xdvx - 1) // 2 + 1
        return var_bacg
