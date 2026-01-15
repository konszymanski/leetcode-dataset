class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx[0])
        var_wrnh = [0] * var_hqta
        for var_osiz in arg_xdvx:
            var_ayzf = 0
            for var_wnki in var_egyk(var_hqta):
                var_ayzf = var_dcmd(var_ayzf - 1, var_wrnh[var_wnki])
                var_wrnh[var_wnki] = var_ayzf
            var_ayzf = 0
            for var_wnki in var_egyk(var_hqta - 1, -1, -1):
                var_ayzf = var_dcmd(var_ayzf - 1, var_wrnh[var_wnki])
                var_wrnh[var_wnki] = var_dcmd(var_wrnh[var_wnki], var_ayzf
                    ) + var_osiz[var_wnki]
        return var_dcmd(var_wrnh)
