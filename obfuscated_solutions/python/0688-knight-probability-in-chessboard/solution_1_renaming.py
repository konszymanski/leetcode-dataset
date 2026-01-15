class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_yjch:
        var_wrnh = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-
            2, 1), (-2, -1)]
        var_osiz = [[([0] * arg_xdvx) for var_ayzf in var_wnki(arg_xdvx)] for
            var_ayzf in var_wnki(arg_rcsn + 1)]
        var_osiz[0][arg_bacg][arg_hqta] = 1
        for var_egyk in var_wnki(1, arg_rcsn + 1):
            for var_dcmd in var_wnki(arg_xdvx):
                for var_llti in var_wnki(arg_xdvx):
                    for var_zbxo in var_wrnh:
                        var_rdmc, var_rjut = var_dcmd - var_zbxo[0
                            ], var_llti - var_zbxo[1]
                        if (0 <= var_rdmc < arg_xdvx and 0 <= var_rjut <
                            arg_xdvx):
                            var_osiz[var_egyk][var_dcmd][var_llti] += var_osiz[
                                var_egyk - 1][var_rdmc][var_rjut]
                    var_osiz[var_egyk][var_dcmd][var_llti] /= 8
        var_lsgw = var_cbvh(var_osiz[arg_rcsn][var_dcmd][var_llti] for
            var_dcmd in var_wnki(arg_xdvx) for var_llti in var_wnki(arg_xdvx))
        return var_lsgw
