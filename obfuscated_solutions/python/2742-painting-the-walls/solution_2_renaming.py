class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [([0] * (var_rgwu + 1)) for var_ayzf in var_wnki(
            var_rgwu + 1)]
        for var_egyk in var_wnki(1, var_rgwu + 1):
            var_osiz[var_rgwu][var_egyk] = var_dcmd
        for var_egyk in var_wnki(var_rgwu - 1, -1, -1):
            for var_llti in var_wnki(1, var_rgwu + 1):
                var_zbxo = arg_xdvx[var_egyk] + var_osiz[var_egyk + 1][var_rdmc
                    (0, var_llti - 1 - arg_rcsn[var_egyk])]
                var_rjut = var_osiz[var_egyk + 1][var_llti]
                var_osiz[var_egyk][var_llti] = var_lsgw(var_zbxo, var_rjut)
        return var_osiz[0][var_rgwu]
