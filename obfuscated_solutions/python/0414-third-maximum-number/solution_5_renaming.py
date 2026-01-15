class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = -1, False
        var_rgwu = -1, False
        func_udax = -1, False
        for var_wrnh in arg_xdvx:
            if var_hqta[1] and var_hqta[0] == var_wrnh or var_rgwu[1
                ] and var_rgwu[0] == var_wrnh or func_udax[1] and func_udax[0
                ] == var_wrnh:
                continue
            if not var_hqta[1] or var_hqta[0] <= var_wrnh:
                func_udax = var_rgwu
                var_rgwu = var_hqta
                var_hqta = var_wrnh, True
            elif not var_rgwu[1] or var_rgwu[0] <= var_wrnh:
                func_udax = var_rgwu
                var_rgwu = var_wrnh, True
            elif not func_udax[1] or func_udax[0] <= var_wrnh:
                func_udax = var_wrnh, True
        if not func_udax[1]:
            return var_hqta[0]
        return func_udax[0]
