class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_egyk:
        if var_rgwu(arg_xdvx) < arg_rcsn:
            return False
        if var_rgwu(arg_xdvx) == arg_rcsn:
            return True
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            var_wrnh ^= 1 << var_ayzf(var_osiz) - var_ayzf('a')
        return var_wnki(var_wrnh).count('1') <= arg_rcsn
