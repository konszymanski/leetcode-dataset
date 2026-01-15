class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(var_bacg)
        for var_wrnh in arg_xdvx:
            var_hqta[var_wrnh[0]] += 1
            var_hqta[var_wrnh[1] + 1] -= 1
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in var_egyk(var_hqta.keys()):
            var_osiz += var_hqta[var_wnki]
            var_ayzf = var_dcmd(var_ayzf, var_osiz)
        return var_ayzf
