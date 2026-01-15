class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        var_hqta = var_rgwu()
        for var_wrnh in arg_xdvx:
            if (2 * var_wrnh in var_hqta or var_wrnh % 2 == 0 and var_wrnh //
                2 in var_hqta):
                return True
            var_hqta.add(var_wrnh)
        return False
