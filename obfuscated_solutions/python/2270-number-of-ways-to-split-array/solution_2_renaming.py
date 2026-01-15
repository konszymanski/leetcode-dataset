class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu = 0
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        for var_ayzf in var_wnki(var_egyk(arg_xdvx) - 1):
            var_hqta += arg_xdvx[var_ayzf]
            var_rgwu -= arg_xdvx[var_ayzf]
            if var_hqta >= var_rgwu:
                var_osiz += 1
        return var_osiz
