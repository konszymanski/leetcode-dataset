class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = arg_rcsn
        arg_xdvx -= 1
        var_rgwu = 1
        while arg_xdvx > 0:
            if var_rgwu & arg_rcsn == 0:
                var_hqta |= (arg_xdvx & 1) * var_rgwu
                arg_xdvx >>= 1
            var_rgwu <<= 1
        return var_hqta
