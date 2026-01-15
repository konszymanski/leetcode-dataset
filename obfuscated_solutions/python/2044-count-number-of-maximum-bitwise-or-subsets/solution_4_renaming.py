class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = [0] * (1 << 17)
        var_rgwu[0] = 1
        for var_wrnh in arg_xdvx:
            for var_osiz in var_ayzf(var_hqta, -1, -1):
                var_rgwu[var_osiz | var_wrnh] += var_rgwu[var_osiz]
            var_hqta |= var_wrnh
        return var_rgwu[var_hqta]
