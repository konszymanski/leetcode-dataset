class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [0] + arg_xdvx[:]
        var_rgwu = var_wrnh(var_hqta)
        for var_osiz in var_ayzf(1, var_rgwu):
            var_hqta[var_osiz] ^= var_hqta[var_osiz - 1]
        var_wnki = 0
        for var_egyk in var_ayzf(var_rgwu):
            for var_dcmd in var_ayzf(var_egyk + 1, var_rgwu):
                if var_hqta[var_egyk] == var_hqta[var_dcmd]:
                    var_wnki += var_dcmd - var_egyk - 1
        return var_wnki
