class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh('inf')
        var_osiz = 0
        for var_ayzf in arg_xdvx:
            for var_wnki in var_ayzf:
                var_hqta += var_egyk(var_wnki)
                if var_wnki < 0:
                    var_osiz += 1
                var_rgwu = var_dcmd(var_rgwu, var_egyk(var_wnki))
        if var_osiz % 2 != 0:
            var_hqta -= 2 * var_rgwu
        return var_hqta
