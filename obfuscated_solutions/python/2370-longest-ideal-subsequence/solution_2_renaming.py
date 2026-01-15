class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * 26
        var_ayzf = 0
        for var_wnki in var_egyk(var_rgwu):
            var_dcmd = var_llti(arg_xdvx[var_wnki]) - var_llti('a')
            var_zbxo = 0
            for var_rdmc in var_egyk(var_rjut(0, var_dcmd - arg_rcsn),
                var_lsgw(26, var_dcmd + arg_rcsn + 1)):
                var_zbxo = var_rjut(var_zbxo, var_osiz[var_rdmc])
            var_osiz[var_dcmd] = var_zbxo + 1
            var_ayzf = var_rjut(var_ayzf, var_osiz[var_dcmd])
        return var_ayzf
