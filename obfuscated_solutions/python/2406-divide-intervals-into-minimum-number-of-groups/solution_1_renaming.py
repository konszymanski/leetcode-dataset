class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = []
        for var_rgwu in arg_xdvx:
            var_hqta.append((var_rgwu[0], 1))
            var_hqta.append((var_rgwu[1] + 1, -1))
        var_hqta.sort(key=lambda x: (var_wrnh[0], var_wrnh[1]))
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in var_hqta:
            var_osiz += var_wnki[1]
            var_ayzf = var_egyk(var_ayzf, var_osiz)
        return var_ayzf
