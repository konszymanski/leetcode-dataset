class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [var_rgwu for var_rgwu in arg_xdvx if var_rgwu % 3 == 0]
        var_wrnh = var_osiz([var_rgwu for var_rgwu in arg_xdvx if var_rgwu %
            3 == 1], reverse=True)
        var_ayzf = var_osiz([var_rgwu for var_rgwu in arg_xdvx if var_rgwu %
            3 == 2], reverse=True)
        var_wnki, var_egyk = var_dcmd(arg_xdvx), var_llti('inf')
        if var_wnki % 3 == 0:
            var_egyk = 0
        elif var_wnki % 3 == 1:
            if var_zbxo(var_wrnh) >= 1:
                var_egyk = var_rdmc(var_egyk, var_wrnh[-1])
            if var_zbxo(var_ayzf) >= 2:
                var_egyk = var_rdmc(var_egyk, var_ayzf[-2] + var_ayzf[-1])
        else:
            if var_zbxo(var_wrnh) >= 2:
                var_egyk = var_rdmc(var_egyk, var_wrnh[-2] + var_wrnh[-1])
            if var_zbxo(var_ayzf) >= 1:
                var_egyk = var_rdmc(var_egyk, var_ayzf[-1])
        return var_wnki - var_egyk
