class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [None] * var_hqta
        var_wrnh[var_hqta - 1] = arg_xdvx[var_hqta - 1]
        for var_osiz in var_ayzf(var_hqta - 2, -1, -1):
            var_wrnh[var_osiz] = var_wnki(var_wrnh[var_osiz + 1], arg_xdvx[
                var_osiz])
        var_egyk = 0
        var_dcmd = 0
        var_llti = 0
        while var_dcmd < var_hqta:
            while var_egyk < var_dcmd and arg_xdvx[var_egyk] > var_wrnh[
                var_dcmd]:
                var_egyk += 1
            var_llti = var_wnki(var_llti, var_dcmd - var_egyk)
            var_dcmd += 1
        return var_llti
