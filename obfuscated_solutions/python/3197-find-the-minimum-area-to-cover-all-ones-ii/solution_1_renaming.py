class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh[var_wrnh[var_osiz]],
        arg_rcsn: var_osiz, arg_bacg: var_osiz, arg_hqta: var_osiz,
        arg_rgwu: var_osiz) ->var_osiz:
        var_ayzf = var_wnki(arg_xdvx)
        var_egyk = 0
        var_dcmd = var_wnki(arg_xdvx[0])
        var_llti = 0
        for var_zbxo in var_rdmc(arg_rcsn, arg_bacg + 1):
            for var_rjut in var_rdmc(arg_hqta, arg_rgwu + 1):
                if arg_xdvx[var_zbxo][var_rjut] == 1:
                    var_ayzf = var_lsgw(var_ayzf, var_zbxo)
                    var_dcmd = var_lsgw(var_dcmd, var_rjut)
                    var_egyk = var_cbvh(var_egyk, var_zbxo)
                    var_llti = var_cbvh(var_llti, var_rjut)
        return (var_egyk - var_ayzf + 1) * (var_llti - var_dcmd + 1
            ) if var_ayzf <= var_egyk else var_yjch.maxsize // 3

    def func_dmio(arg_ihhe, arg_ulfl: var_wrnh[var_wrnh[var_osiz]]) ->var_wrnh[
        var_wrnh[var_osiz]]:
        var_lgvi = var_wnki(arg_ulfl)
        var_wvuc = var_wnki(arg_ulfl[0]) if var_lgvi > 0 else 0
        var_tufr = [([0] * var_lgvi) for var_xhfo in var_rdmc(var_wvuc)]
        for var_zbxo in var_rdmc(var_lgvi):
            for var_rjut in var_rdmc(var_wvuc):
                var_tufr[var_wvuc - var_rjut - 1][var_zbxo] = arg_ulfl[var_zbxo
                    ][var_rjut]
        return var_tufr

    def func_miuw(arg_ihhe, arg_xdvx: var_wrnh[var_wrnh[var_osiz]]) ->var_osiz:
        var_lgvi = var_wnki(arg_xdvx)
        var_wvuc = var_wnki(arg_xdvx[0]) if var_lgvi > 0 else 0
        var_rhvk = var_lgvi * var_wvuc
        for var_zbxo in var_rdmc(var_lgvi - 1):
            for var_rjut in var_rdmc(var_wvuc - 1):
                var_rhvk = var_lsgw(var_rhvk, arg_ihhe.minimumSum2(arg_xdvx,
                    0, var_zbxo, 0, var_wvuc - 1) + arg_ihhe.minimumSum2(
                    arg_xdvx, var_zbxo + 1, var_lgvi - 1, 0, var_rjut) +
                    arg_ihhe.minimumSum2(arg_xdvx, var_zbxo + 1, var_lgvi -
                    1, var_rjut + 1, var_wvuc - 1))
                var_rhvk = var_lsgw(var_rhvk, arg_ihhe.minimumSum2(arg_xdvx,
                    0, var_zbxo, 0, var_rjut) + arg_ihhe.minimumSum2(
                    arg_xdvx, 0, var_zbxo, var_rjut + 1, var_wvuc - 1) +
                    arg_ihhe.minimumSum2(arg_xdvx, var_zbxo + 1, var_lgvi -
                    1, 0, var_wvuc - 1))
        for var_zbxo in var_rdmc(var_lgvi - 2):
            for var_rjut in var_rdmc(var_zbxo + 1, var_lgvi - 1):
                var_rhvk = var_lsgw(var_rhvk, arg_ihhe.minimumSum2(arg_xdvx,
                    0, var_zbxo, 0, var_wvuc - 1) + arg_ihhe.minimumSum2(
                    arg_xdvx, var_zbxo + 1, var_rjut, 0, var_wvuc - 1) +
                    arg_ihhe.minimumSum2(arg_xdvx, var_rjut + 1, var_lgvi -
                    1, 0, var_wvuc - 1))
        return var_rhvk

    def func_yybh(arg_ihhe, arg_xdvx: var_wrnh[var_wrnh[var_osiz]]) ->var_osiz:
        var_bzkm = arg_ihhe.rotate(arg_xdvx)
        return var_lsgw(arg_ihhe.solve(arg_xdvx), arg_ihhe.solve(var_bzkm))
