class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx[0])
        var_wrnh = 0
        var_osiz = var_ayzf('inf')
        for var_wnki in var_egyk(var_dcmd(arg_xdvx[0])):
            var_hqta -= arg_xdvx[0][var_wnki]
            var_osiz = var_llti(var_osiz, var_zbxo(var_hqta, var_wrnh))
            var_wrnh += arg_xdvx[1][var_wnki]
        return var_osiz
