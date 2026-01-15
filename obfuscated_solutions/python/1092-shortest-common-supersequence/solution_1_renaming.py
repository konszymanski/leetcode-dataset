class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if not arg_xdvx and not arg_rcsn:
            return ''
        if not arg_xdvx:
            return arg_rcsn
        if not arg_rcsn:
            return arg_xdvx
        if arg_xdvx[0] == arg_rcsn[0]:
            return arg_xdvx[0] + arg_ihhe.shortestCommonSupersequence(arg_xdvx
                [1:], arg_rcsn[1:])
        else:
            var_hqta = arg_xdvx[0] + arg_ihhe.shortestCommonSupersequence(
                arg_xdvx[1:], arg_rcsn)
            var_rgwu = arg_rcsn[0] + arg_ihhe.shortestCommonSupersequence(
                arg_xdvx, arg_rcsn[1:])
            return var_hqta if var_wrnh(var_hqta) < var_wrnh(var_rgwu
                ) else var_rgwu
