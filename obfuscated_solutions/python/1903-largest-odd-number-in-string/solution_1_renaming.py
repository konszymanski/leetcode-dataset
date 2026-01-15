class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        for var_bacg in var_hqta(var_rgwu(arg_xdvx) - 1, -1, -1):
            if var_wrnh(arg_xdvx[var_bacg]) % 2 != 0:
                return arg_xdvx[:var_bacg + 1]
        return ''
