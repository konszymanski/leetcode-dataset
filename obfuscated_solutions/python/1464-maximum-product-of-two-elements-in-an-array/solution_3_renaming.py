class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            if var_wrnh > var_hqta:
                var_rgwu = var_hqta
                var_hqta = var_wrnh
            else:
                var_rgwu = var_osiz(var_rgwu, var_wrnh)
        return (var_hqta - 1) * (var_rgwu - 1)
