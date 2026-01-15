class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = {}
        for var_rgwu in arg_xdvx:
            if var_rgwu in var_hqta:
                var_hqta[var_rgwu] += 1
            else:
                var_hqta[var_rgwu] = 1
        var_wrnh = 0
        for var_osiz in var_hqta.values():
            var_wrnh = var_ayzf(var_wrnh, var_osiz)
        var_wnki = 0
        for var_osiz in var_hqta.values():
            if var_osiz == var_wrnh:
                var_wnki += 1
        return var_wnki * var_wrnh
