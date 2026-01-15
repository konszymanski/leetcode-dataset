class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_llti:
        var_hqta, var_rgwu = var_wrnh(arg_rcsn), var_wrnh(arg_xdvx)
        if var_rgwu > var_hqta:
            return False
        var_osiz = [0] * 26
        var_ayzf = [0] * 26
        for var_wnki in var_egyk(var_rgwu):
            var_osiz[var_dcmd(arg_xdvx[var_wnki]) - var_dcmd('a')] += 1
            var_ayzf[var_dcmd(arg_rcsn[var_wnki]) - var_dcmd('a')] += 1
        if var_osiz == var_ayzf:
            return True
        for var_wnki in var_egyk(var_hqta - var_rgwu):
            var_ayzf[var_dcmd(arg_rcsn[var_wnki]) - var_dcmd('a')] -= 1
            var_ayzf[var_dcmd(arg_rcsn[var_wnki + var_rgwu]) - var_dcmd('a')
                ] += 1
            if var_osiz == var_ayzf:
                return True
        return False
