class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [0] + arg_xdvx
        var_rgwu = var_wrnh(var_hqta)
        var_osiz = 0
        for var_ayzf in var_wnki(1, var_rgwu):
            var_hqta[var_ayzf] ^= var_hqta[var_ayzf - 1]
        var_egyk = var_dcmd(var_bacg)
        var_llti = var_dcmd(var_bacg)
        for var_ayzf in var_wnki(var_rgwu):
            var_osiz += var_egyk[var_hqta[var_ayzf]] * (var_ayzf - 1
                ) - var_llti[var_hqta[var_ayzf]]
            var_llti[var_hqta[var_ayzf]] += var_ayzf
            var_egyk[var_hqta[var_ayzf]] += 1
        return var_osiz
