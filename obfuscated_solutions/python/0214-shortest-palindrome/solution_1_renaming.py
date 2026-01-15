class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = arg_xdvx[::-1]
        for var_wrnh in var_osiz(var_bacg):
            if arg_xdvx[:var_bacg - var_wrnh] == var_rgwu[var_wrnh:]:
                return var_rgwu[:var_wrnh] + arg_xdvx
        return ''
