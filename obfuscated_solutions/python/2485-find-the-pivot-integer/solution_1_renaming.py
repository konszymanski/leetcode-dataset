class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        for var_bacg in var_hqta(1, arg_xdvx + 1):
            var_rgwu = var_wrnh(var_hqta(1, var_bacg + 1))
            var_osiz = var_wrnh(var_hqta(var_bacg, arg_xdvx + 1))
            if var_rgwu == var_osiz:
                return var_bacg
        return -1
