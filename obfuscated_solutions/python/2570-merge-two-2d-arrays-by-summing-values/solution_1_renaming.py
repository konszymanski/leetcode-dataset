class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_bacg[var_hqta]]:
        var_rgwu = {}
        for var_wrnh in arg_xdvx:
            var_rgwu[var_wrnh[0]] = var_wrnh[1]
        for var_wrnh in arg_rcsn:
            var_rgwu[var_wrnh[0]] = var_rgwu.get(var_wrnh[0], 0) + var_wrnh[1]
        var_osiz = []
        for var_ayzf, var_wnki in var_egyk(var_rgwu.items()):
            var_osiz.append([var_ayzf, var_wnki])
        return var_osiz
