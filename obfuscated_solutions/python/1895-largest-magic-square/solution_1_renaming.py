class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = [([0] * var_rgwu) for var_ayzf in var_wnki(var_hqta)]
        for var_egyk in var_wnki(var_hqta):
            var_osiz[var_egyk][0] = arg_xdvx[var_egyk][0]
            for var_dcmd in var_wnki(1, var_rgwu):
                var_osiz[var_egyk][var_dcmd] = var_osiz[var_egyk][var_dcmd - 1
                    ] + arg_xdvx[var_egyk][var_dcmd]
        var_llti = [([0] * var_rgwu) for var_ayzf in var_wnki(var_hqta)]
        for var_dcmd in var_wnki(var_rgwu):
            var_llti[0][var_dcmd] = arg_xdvx[0][var_dcmd]
            for var_egyk in var_wnki(1, var_hqta):
                var_llti[var_egyk][var_dcmd] = var_llti[var_egyk - 1][var_dcmd
                    ] + arg_xdvx[var_egyk][var_dcmd]
        for var_zbxo in var_wnki(var_rdmc(var_hqta, var_rgwu), 1, -1):
            for var_egyk in var_wnki(var_hqta - var_zbxo + 1):
                for var_dcmd in var_wnki(var_rgwu - var_zbxo + 1):
                    var_rjut = var_osiz[var_egyk][var_dcmd + var_zbxo - 1] - (
                        0 if var_dcmd == 0 else var_osiz[var_egyk][var_dcmd -
                        1])
                    var_lsgw = True
                    for var_cbvh in var_wnki(var_egyk + 1, var_egyk + var_zbxo
                        ):
                        if var_osiz[var_cbvh][var_dcmd + var_zbxo - 1] - (0 if
                            var_dcmd == 0 else var_osiz[var_cbvh][var_dcmd - 1]
                            ) != var_rjut:
                            var_lsgw = False
                            break
                    if not var_lsgw:
                        continue
                    for var_yjch in var_wnki(var_dcmd, var_dcmd + var_zbxo):
                        if var_llti[var_egyk + var_zbxo - 1][var_yjch] - (0 if
                            var_egyk == 0 else var_llti[var_egyk - 1][var_yjch]
                            ) != var_rjut:
                            var_lsgw = False
                            break
                    if not var_lsgw:
                        continue
                    var_dmio = var_ulfl = 0
                    for var_lgvi in var_wnki(var_zbxo):
                        var_dmio += arg_xdvx[var_egyk + var_lgvi][var_dcmd +
                            var_lgvi]
                        var_ulfl += arg_xdvx[var_egyk + var_lgvi][var_dcmd +
                            var_zbxo - 1 - var_lgvi]
                    if var_dmio == var_rjut and var_ulfl == var_rjut:
                        return var_zbxo
        return 1
