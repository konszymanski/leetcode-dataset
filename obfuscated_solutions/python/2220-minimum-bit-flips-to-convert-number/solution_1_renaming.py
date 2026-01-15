class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        while arg_xdvx > 0 or arg_rcsn > 0:
            if arg_xdvx & 1 != arg_rcsn & 1:
                var_hqta += 1
            arg_xdvx >>= 1
            arg_rcsn >>= 1
        return var_hqta
