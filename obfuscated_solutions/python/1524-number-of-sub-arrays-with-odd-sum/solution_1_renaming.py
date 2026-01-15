class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 1000000000.0 + 7
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        for var_ayzf in var_wnki(var_rgwu):
            var_egyk = 0
            for var_dcmd in var_wnki(var_ayzf, var_rgwu):
                var_egyk += arg_xdvx[var_dcmd]
                if var_egyk % 2 != 0:
                    var_osiz += 1
        return var_bacg(var_osiz % var_hqta)
