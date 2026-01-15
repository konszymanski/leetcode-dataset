class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        for var_bacg in var_hqta(var_rgwu(arg_xdvx)):
            if arg_xdvx[var_bacg] == ' ' and arg_xdvx[var_bacg - 1
                ] != arg_xdvx[var_bacg + 1]:
                return False
        return arg_xdvx[0] == arg_xdvx[var_rgwu(arg_xdvx) - 1]
