class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = -var_rgwu
        var_wrnh = -var_rgwu
        var_osiz = -var_rgwu
        for var_ayzf in arg_xdvx:
            if (var_hqta == var_ayzf or var_wrnh == var_ayzf or var_osiz ==
                var_ayzf):
                continue
            if var_hqta <= var_ayzf:
                var_osiz = var_wrnh
                var_wrnh = var_hqta
                var_hqta = var_ayzf
            elif var_wrnh <= var_ayzf:
                var_osiz = var_wrnh
                var_wrnh = var_ayzf
            elif var_osiz <= var_ayzf:
                var_osiz = var_ayzf
        if var_osiz == -var_rgwu:
            return var_hqta
        return var_osiz
