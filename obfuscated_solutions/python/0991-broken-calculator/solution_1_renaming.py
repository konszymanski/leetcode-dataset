class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        while arg_rcsn > arg_xdvx:
            var_hqta += 1
            if arg_rcsn % 2:
                arg_rcsn += 1
            else:
                arg_rcsn //= 2
        return var_hqta + arg_xdvx - arg_rcsn
