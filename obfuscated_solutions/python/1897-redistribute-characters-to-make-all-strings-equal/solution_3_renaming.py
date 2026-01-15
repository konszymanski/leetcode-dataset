class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_dcmd:
        var_hqta = [0] * 26
        for var_rgwu in arg_xdvx:
            for var_wrnh in var_rgwu:
                var_hqta[var_osiz(var_wrnh) - var_osiz('a')] += 1
        var_ayzf = var_wnki(arg_xdvx)
        for var_egyk in var_hqta:
            if var_egyk % var_ayzf != 0:
                return False
        return True
