class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = ''
        while arg_xdvx > 0:
            arg_xdvx -= 1
            var_bacg += var_hqta(arg_xdvx % 26 + var_rgwu('A'))
            arg_xdvx //= 26
        return var_bacg[::-1]
