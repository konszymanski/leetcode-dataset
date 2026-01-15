class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rgwu:
        var_hqta = [(var_rgwu(var_wrnh[:2]) * 60 + var_rgwu(var_wrnh[3:])) for
            var_wrnh in arg_xdvx]
        var_hqta.sort()
        var_osiz = var_ayzf(var_hqta[var_wnki + 1] - var_hqta[var_wnki] for
            var_wnki in var_egyk(var_dcmd(var_hqta) - 1))
        return var_ayzf(var_osiz, 24 * 60 - var_hqta[-1] + var_hqta[0])
