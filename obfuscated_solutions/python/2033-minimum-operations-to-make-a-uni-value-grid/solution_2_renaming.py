class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = var_rgwu('inf')
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            for var_wnki in var_osiz(var_ayzf(arg_xdvx[0])):
                if arg_xdvx[var_wrnh][var_wnki] % arg_rcsn != arg_xdvx[0][0
                    ] % arg_rcsn:
                    return -1
                var_bacg.append(arg_xdvx[var_wrnh][var_wnki])
        var_bacg.sort()
        var_egyk = var_ayzf(var_bacg)
        var_dcmd = [0] * var_egyk
        var_llti = [0] * var_egyk
        for var_zbxo in var_osiz(1, var_egyk):
            var_dcmd[var_zbxo] = var_dcmd[var_zbxo - 1] + var_bacg[var_zbxo - 1
                ]
        for var_zbxo in var_osiz(var_egyk - 2, -1, -1):
            var_llti[var_zbxo] = var_llti[var_zbxo + 1] + var_bacg[var_zbxo + 1
                ]
        for var_zbxo in var_osiz(var_egyk):
            var_rdmc = (var_bacg[var_zbxo] * var_zbxo - var_dcmd[var_zbxo]
                ) // arg_rcsn
            var_rjut = (var_llti[var_zbxo] - var_bacg[var_zbxo] * (var_egyk -
                var_zbxo - 1)) // arg_rcsn
            var_hqta = var_lsgw(var_hqta, var_rdmc + var_rjut)
        return var_hqta
