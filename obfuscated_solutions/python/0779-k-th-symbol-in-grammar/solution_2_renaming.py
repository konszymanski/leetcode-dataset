class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == 1:
            return 0
        var_hqta = 2 ** (arg_xdvx - 1)
        var_rgwu = var_hqta // 2
        if arg_rcsn > var_rgwu:
            return 1 - arg_ihhe.recursion(arg_xdvx, arg_rcsn - var_rgwu)
        return arg_ihhe.recursion(arg_xdvx - 1, arg_rcsn)

    def func_wrnh(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        return arg_ihhe.recursion(arg_xdvx, arg_rcsn)
