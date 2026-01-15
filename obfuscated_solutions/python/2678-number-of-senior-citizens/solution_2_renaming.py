class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_egyk:
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_wrnh = var_osiz(var_rgwu[11]) - var_osiz('0')
            var_ayzf = var_osiz(var_rgwu[12]) - var_osiz('0')
            var_wnki = var_wrnh * 10 + var_ayzf
            if var_wnki > 60:
                var_hqta += 1
        return var_hqta
