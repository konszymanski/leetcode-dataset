class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu + 1)
        for var_ayzf in var_wnki(1, var_rgwu + 1):
            var_osiz[var_ayzf] = var_osiz[var_ayzf - 1] + arg_xdvx[var_ayzf - 1
                ]
        var_egyk = [([0] * (var_rgwu + 1)) for var_dcmd in var_wnki(4)]
        var_llti = [([0] * (var_rgwu + 1)) for var_dcmd in var_wnki(4)]
        for var_zbxo in var_wnki(1, 4):
            for var_ayzf in var_wnki(arg_rcsn * var_zbxo, var_rgwu + 1):
                var_rdmc = var_osiz[var_ayzf] - var_osiz[var_ayzf - arg_rcsn
                    ] + var_egyk[var_zbxo - 1][var_ayzf - arg_rcsn]
                if var_rdmc > var_egyk[var_zbxo][var_ayzf - 1]:
                    var_egyk[var_zbxo][var_ayzf] = var_rdmc
                    var_llti[var_zbxo][var_ayzf] = var_ayzf - arg_rcsn
                else:
                    var_egyk[var_zbxo][var_ayzf] = var_egyk[var_zbxo][
                        var_ayzf - 1]
                    var_llti[var_zbxo][var_ayzf] = var_llti[var_zbxo][
                        var_ayzf - 1]
        var_rjut = [0] * 3
        var_lsgw = var_rgwu
        for var_zbxo in var_wnki(3, 0, -1):
            var_rjut[var_zbxo - 1] = var_llti[var_zbxo][var_lsgw]
            var_lsgw = var_rjut[var_zbxo - 1]
        return var_rjut
