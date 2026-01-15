class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 1
        var_rgwu = 0
        var_wrnh = 1
        while var_rgwu < arg_rcsn:
            if 0 < var_hqta + var_wrnh <= arg_xdvx:
                var_hqta += var_wrnh
                var_rgwu += 1
            else:
                var_wrnh *= -1
        return var_hqta
