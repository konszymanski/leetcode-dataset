from collections import Counter


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh((var_bacg[var_osiz] for var_osiz in var_bacg if
            var_osiz in 'aeiou'), default=0)
        var_ayzf = var_wrnh((var_bacg[var_osiz] for var_osiz in var_bacg if
            var_osiz not in 'aeiou'), default=0)
        return var_rgwu + var_ayzf
