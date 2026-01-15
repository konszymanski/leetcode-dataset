class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = {None: -1}

        def func_hqta(arg_rgwu, arg_wrnh=None):
            if arg_rgwu:
                var_bacg[arg_rgwu] = var_bacg[arg_wrnh] + 1
                func_hqta(arg_rgwu.left, arg_rgwu)
                func_hqta(arg_rgwu.right, arg_rgwu)
        func_hqta(arg_rcsn)
        var_osiz = var_ayzf(var_bacg.itervalues())

        def func_wnki(arg_rgwu):
            if not arg_rgwu or var_bacg.get(arg_rgwu, None) == var_osiz:
                return arg_rgwu
            var_egyk, var_dcmd = func_wnki(arg_rgwu.left), func_wnki(arg_rgwu
                .right)
            return arg_rgwu if var_egyk and var_dcmd else var_egyk or var_dcmd
        return func_wnki(arg_rcsn)
