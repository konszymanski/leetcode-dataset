class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        while arg_xdvx and arg_rcsn:
            var_hqta += arg_xdvx // arg_rcsn
            arg_xdvx %= arg_rcsn
            arg_xdvx, arg_rcsn = arg_rcsn, arg_xdvx
        return var_hqta
