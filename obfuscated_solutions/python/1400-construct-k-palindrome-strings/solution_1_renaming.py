class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_dcmd:
        if var_rgwu(arg_xdvx) < arg_rcsn:
            return False
        if var_rgwu(arg_xdvx) == arg_rcsn:
            return True
        var_wrnh = [0] * 26
        var_osiz = 0
        for var_ayzf in arg_xdvx:
            var_wrnh[var_wnki(var_ayzf) - var_wnki('a')] += 1
        for var_egyk in var_wrnh:
            if var_egyk % 2 == 1:
                var_osiz += 1
        return var_osiz <= arg_rcsn
