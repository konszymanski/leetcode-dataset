class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(2, var_hqta):
            var_wnki = arg_xdvx[0]
            for var_egyk in var_ayzf(1, var_osiz):
                var_wrnh = var_dcmd(var_wrnh, (var_wnki - arg_xdvx[var_egyk
                    ]) * arg_xdvx[var_osiz])
                var_wnki = var_dcmd(var_wnki, arg_xdvx[var_egyk])
        return var_wrnh
