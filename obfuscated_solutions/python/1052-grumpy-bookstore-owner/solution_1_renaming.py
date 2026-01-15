class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = 0
        for var_wnki in var_egyk(arg_bacg):
            var_ayzf += arg_xdvx[var_wnki] * arg_rcsn[var_wnki]
        var_dcmd = var_ayzf
        for var_wnki in var_egyk(arg_bacg, var_wrnh):
            var_ayzf += arg_xdvx[var_wnki] * arg_rcsn[var_wnki]
            var_ayzf -= arg_xdvx[var_wnki - arg_bacg] * arg_rcsn[var_wnki -
                arg_bacg]
            var_dcmd = var_llti(var_dcmd, var_ayzf)
        var_zbxo = var_dcmd
        for var_wnki in var_egyk(var_wrnh):
            var_zbxo += arg_xdvx[var_wnki] * (1 - arg_rcsn[var_wnki])
        return var_zbxo
