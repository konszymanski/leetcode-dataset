class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in arg_xdvx:
            var_ayzf = 0
            var_wnki = var_osiz
            while var_wnki in var_rgwu:
                var_ayzf += 1
                if var_wnki * var_wnki > 10 ** 5:
                    break
                var_wnki *= var_wnki
            var_hqta = var_egyk(var_hqta, var_ayzf)
        return var_hqta if var_hqta >= 2 else -1
