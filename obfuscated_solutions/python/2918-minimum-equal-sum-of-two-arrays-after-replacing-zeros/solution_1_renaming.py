class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh = 0
        var_osiz = var_ayzf = 0
        for var_wnki in arg_xdvx:
            var_rgwu += var_wnki
            if var_wnki == 0:
                var_rgwu += 1
                var_osiz += 1
        for var_wnki in arg_rcsn:
            var_wrnh += var_wnki
            if var_wnki == 0:
                var_wrnh += 1
                var_ayzf += 1
        if (var_osiz == 0 and var_wrnh > var_rgwu or var_ayzf == 0 and 
            var_rgwu > var_wrnh):
            return -1
        return var_egyk(var_rgwu, var_wrnh)
