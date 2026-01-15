class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(var_bacg)
        var_wrnh = var_rgwu(var_bacg)
        var_osiz = var_ayzf(arg_xdvx)
        for var_wnki in arg_xdvx:
            var_wrnh[var_wnki] += 1
        for var_egyk in var_dcmd(var_osiz):
            var_wnki = arg_xdvx[var_egyk]
            var_wrnh[var_wnki] -= 1
            var_hqta[var_wnki] += 1
            if var_hqta[var_wnki] * 2 > var_egyk + 1 and var_wrnh[var_wnki
                ] * 2 > var_osiz - var_egyk - 1:
                return var_egyk
        return -1
