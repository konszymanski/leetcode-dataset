class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn: var_hqta, arg_bacg: var_hqta) ->var_wrnh:
        if not arg_bacg:
            return not arg_rcsn
        var_rgwu = var_wrnh(arg_rcsn) and arg_bacg[0] in {arg_rcsn[0], '.'}
        if var_osiz(arg_bacg) >= 2 and arg_bacg[1] == '*':
            return arg_xdvx.isMatch(arg_rcsn, arg_bacg[2:]
                ) or var_rgwu and arg_xdvx.isMatch(arg_rcsn[1:], arg_bacg)
        else:
            return var_rgwu and arg_xdvx.isMatch(arg_rcsn[1:], arg_bacg[1:])
