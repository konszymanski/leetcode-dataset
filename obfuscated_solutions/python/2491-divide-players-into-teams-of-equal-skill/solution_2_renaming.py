class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * 2001
        for var_wnki in arg_xdvx:
            var_ayzf[var_wnki] += 1
        if var_wrnh % (var_hqta // 2) != 0:
            return -1
        var_egyk = var_wrnh // (var_hqta // 2)
        var_dcmd = 0
        for var_wnki in arg_xdvx:
            var_llti = var_egyk - var_wnki
            if var_ayzf[var_llti] == 0:
                return -1
            var_dcmd += var_wnki * var_llti
            var_ayzf[var_llti] -= 1
        return var_dcmd // 2
