class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = {}
        for var_rgwu in arg_xdvx:
            var_hqta[var_rgwu[0]] = var_hqta.get(var_rgwu[0], 0) + 1
            var_hqta[var_rgwu[1]] = var_hqta.get(var_rgwu[1], 0) + 1
        for var_wrnh, var_osiz in var_hqta.items():
            if var_osiz == var_ayzf(arg_xdvx):
                return var_wrnh
        return -1
