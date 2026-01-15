class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = {}
        for var_osiz in arg_xdvx:
            for var_ayzf in var_osiz:
                var_wrnh[var_ayzf] = var_wrnh.get(var_ayzf, 0) + 1
        for var_ayzf in var_wnki(1, var_hqta * var_hqta + 1):
            if var_ayzf not in var_wrnh:
                var_egyk = var_ayzf
            elif var_wrnh[var_ayzf] == 2:
                var_dcmd = var_ayzf
        return [var_dcmd, var_egyk]
