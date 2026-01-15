class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu()
        for var_wrnh in arg_xdvx:
            if var_wrnh < 0:
                var_hqta.add(var_wrnh)
        var_osiz = -1
        for var_wrnh in arg_xdvx:
            if var_wrnh > var_osiz and -var_wrnh in var_hqta:
                var_osiz = var_wrnh
        return var_osiz
