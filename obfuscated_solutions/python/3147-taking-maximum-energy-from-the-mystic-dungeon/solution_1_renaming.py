class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = -var_ayzf
        for var_wnki in var_egyk(var_rgwu - arg_rcsn, var_rgwu):
            var_dcmd = 0
            var_llti = var_wnki
            while var_llti >= 0:
                var_dcmd += arg_xdvx[var_llti]
                var_osiz = var_zbxo(var_osiz, var_dcmd)
                var_llti -= arg_rcsn
        return var_osiz
