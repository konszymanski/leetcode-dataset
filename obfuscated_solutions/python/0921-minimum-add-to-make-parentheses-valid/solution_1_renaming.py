class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = 0
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            if var_rgwu == '(':
                var_bacg += 1
            elif var_bacg > 0:
                var_bacg -= 1
            else:
                var_hqta += 1
        return var_hqta + var_bacg
