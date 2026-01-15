class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_hqta[var_hqta[var_bacg]]:
        var_rgwu = [([0] * (arg_xdvx + 1)) for var_wrnh in var_osiz(
            arg_xdvx + 1)]
        for var_ayzf, var_wnki, var_egyk, var_dcmd in arg_rcsn:
            var_rgwu[var_ayzf][var_wnki] += 1
            var_rgwu[var_egyk + 1][var_wnki] -= 1
            var_rgwu[var_ayzf][var_dcmd + 1] -= 1
            var_rgwu[var_egyk + 1][var_dcmd + 1] += 1
        var_llti = [([0] * arg_xdvx) for var_wrnh in var_osiz(arg_xdvx)]
        for var_zbxo in var_osiz(arg_xdvx):
            for var_rdmc in var_osiz(arg_xdvx):
                var_rjut = 0 if var_zbxo == 0 else var_llti[var_zbxo - 1][
                    var_rdmc]
                var_lsgw = 0 if var_rdmc == 0 else var_llti[var_zbxo][
                    var_rdmc - 1]
                var_cbvh = 0 if var_zbxo == 0 or var_rdmc == 0 else var_llti[
                    var_zbxo - 1][var_rdmc - 1]
                var_llti[var_zbxo][var_rdmc] = var_rgwu[var_zbxo][var_rdmc
                    ] + var_rjut + var_lsgw - var_cbvh
        return var_llti
