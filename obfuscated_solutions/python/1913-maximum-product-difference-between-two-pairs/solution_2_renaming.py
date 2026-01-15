class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = 0
        var_wrnh = var_osiz
        var_ayzf = var_osiz
        for var_wnki in arg_xdvx:
            if var_wnki > var_hqta:
                var_rgwu = var_hqta
                var_hqta = var_wnki
            else:
                var_rgwu = var_egyk(var_rgwu, var_wnki)
            if var_wnki < var_wrnh:
                var_ayzf = var_wrnh
                var_wrnh = var_wnki
            else:
                var_ayzf = var_dcmd(var_ayzf, var_wnki)
        return var_hqta * var_rgwu - var_wrnh * var_ayzf
