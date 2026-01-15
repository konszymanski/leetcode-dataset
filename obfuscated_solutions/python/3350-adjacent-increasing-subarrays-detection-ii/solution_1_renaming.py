class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz, var_ayzf = 1, 0, 0
        for var_wnki in var_egyk(1, var_hqta):
            if arg_xdvx[var_wnki] > arg_xdvx[var_wnki - 1]:
                var_wrnh += 1
            else:
                var_osiz, var_wrnh = var_wrnh, 1
            var_ayzf = var_dcmd(var_ayzf, var_llti(var_osiz, var_wrnh))
            var_ayzf = var_dcmd(var_ayzf, var_wrnh // 2)
        return var_ayzf
