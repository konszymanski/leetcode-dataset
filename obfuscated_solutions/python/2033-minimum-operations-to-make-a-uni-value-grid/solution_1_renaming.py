class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            for var_wrnh in var_rgwu:
                var_bacg.append(var_wrnh)
        var_bacg.sort()
        var_osiz = var_ayzf(var_bacg)
        var_wnki = var_bacg[var_osiz // 2]
        for var_egyk in var_bacg:
            if var_egyk % arg_rcsn != var_wnki % arg_rcsn:
                return -1
            var_hqta += var_dcmd(var_wnki - var_egyk) // arg_rcsn
        return var_hqta
