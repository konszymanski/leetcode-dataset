class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 1
        var_hqta = arg_xdvx
        var_rgwu = var_bacg
        var_wrnh = var_hqta
        if arg_xdvx == 1:
            return arg_xdvx
        while var_bacg < var_hqta:
            if var_rgwu < var_wrnh:
                var_rgwu += var_bacg + 1
                var_bacg += 1
            else:
                var_wrnh += var_hqta - 1
                var_hqta -= 1
            if var_rgwu == var_wrnh and var_bacg + 1 == var_hqta - 1:
                return var_bacg + 1
        return -1
