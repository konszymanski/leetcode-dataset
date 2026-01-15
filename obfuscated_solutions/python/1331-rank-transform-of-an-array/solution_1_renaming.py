class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = {}
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 1
        for var_ayzf in var_wnki(var_egyk(var_rgwu)):
            if var_ayzf > 0 and var_rgwu[var_ayzf] > var_rgwu[var_ayzf - 1]:
                var_osiz += 1
            var_hqta[var_rgwu[var_ayzf]] = var_osiz
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            arg_xdvx[var_ayzf] = var_hqta[arg_xdvx[var_ayzf]]
        return arg_xdvx
