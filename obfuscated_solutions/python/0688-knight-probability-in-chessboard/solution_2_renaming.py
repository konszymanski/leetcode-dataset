class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_dmio:
        var_wrnh = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-
            2, 1), (-2, -1)]
        var_osiz = [([0] * arg_xdvx) for var_ayzf in var_wnki(arg_xdvx)]
        var_egyk = [([0] * arg_xdvx) for var_ayzf in var_wnki(arg_xdvx)]
        var_osiz[arg_bacg][arg_hqta] = 1
        for var_dcmd in var_wnki(1, arg_rcsn + 1):
            for var_llti in var_wnki(arg_xdvx):
                for var_zbxo in var_wnki(arg_xdvx):
                    var_egyk[var_llti][var_zbxo] = 0
                    for var_rdmc in var_wrnh:
                        var_rjut, var_lsgw = var_llti - var_rdmc[0
                            ], var_zbxo - var_rdmc[1]
                        if (0 <= var_rjut < arg_xdvx and 0 <= var_lsgw <
                            arg_xdvx):
                            var_egyk[var_llti][var_zbxo] += var_osiz[var_rjut][
                                var_lsgw] / 8
            var_osiz, var_egyk = var_egyk, var_osiz
        var_cbvh = var_yjch(var_osiz[var_llti][var_zbxo] for var_llti in
            var_wnki(arg_xdvx) for var_zbxo in var_wnki(arg_xdvx))
        return var_cbvh
