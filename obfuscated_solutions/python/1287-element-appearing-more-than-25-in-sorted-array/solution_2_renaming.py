class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(var_bacg)
        var_wrnh = var_osiz(arg_xdvx) / 4
        for var_ayzf in arg_xdvx:
            var_hqta[var_ayzf] += 1
            if var_hqta[var_ayzf] > var_wrnh:
                return var_ayzf
        return -1
