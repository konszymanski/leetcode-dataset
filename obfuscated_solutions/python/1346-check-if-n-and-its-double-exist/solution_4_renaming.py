class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wrnh:
        var_hqta = {}
        for var_rgwu in arg_xdvx:
            var_hqta[var_rgwu] = var_hqta.get(var_rgwu, 0) + 1
        for var_rgwu in arg_xdvx:
            if var_rgwu != 0 and 2 * var_rgwu in var_hqta:
                return True
            if var_rgwu == 0 and var_hqta[var_rgwu] > 1:
                return True
        return False
