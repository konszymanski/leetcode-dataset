class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])
        for var_ayzf in var_wnki(var_rgwu - 2):
            for var_egyk in var_wnki(var_osiz - 2):
                if arg_ihhe._isMagicSquare(arg_xdvx, var_ayzf, var_egyk):
                    var_hqta += 1
        return var_hqta

    def func_dcmd(arg_ihhe, arg_xdvx, var_ayzf, var_egyk):
        var_llti = [False] * 10
        for var_zbxo in var_wnki(3):
            for var_rdmc in var_wnki(3):
                var_rjut = arg_xdvx[var_ayzf + var_zbxo][var_egyk + var_rdmc]
                if var_rjut < 1 or var_rjut > 9:
                    return False
                if var_llti[var_rjut]:
                    return False
                var_llti[var_rjut] = True
        var_lsgw = arg_xdvx[var_ayzf][var_egyk] + arg_xdvx[var_ayzf + 1][
            var_egyk + 1] + arg_xdvx[var_ayzf + 2][var_egyk + 2]
        var_cbvh = arg_xdvx[var_ayzf + 2][var_egyk] + arg_xdvx[var_ayzf + 1][
            var_egyk + 1] + arg_xdvx[var_ayzf][var_egyk + 2]
        if var_lsgw != var_cbvh:
            return False
        var_yjch = arg_xdvx[var_ayzf][var_egyk] + arg_xdvx[var_ayzf][
            var_egyk + 1] + arg_xdvx[var_ayzf][var_egyk + 2]
        var_dmio = arg_xdvx[var_ayzf + 1][var_egyk] + arg_xdvx[var_ayzf + 1][
            var_egyk + 1] + arg_xdvx[var_ayzf + 1][var_egyk + 2]
        var_ulfl = arg_xdvx[var_ayzf + 2][var_egyk] + arg_xdvx[var_ayzf + 2][
            var_egyk + 1] + arg_xdvx[var_ayzf + 2][var_egyk + 2]
        if not (var_yjch == var_lsgw and var_dmio == var_lsgw and var_ulfl ==
            var_lsgw):
            return False
        var_lgvi = arg_xdvx[var_ayzf][var_egyk] + arg_xdvx[var_ayzf + 1][
            var_egyk] + arg_xdvx[var_ayzf + 2][var_egyk]
        var_wvuc = arg_xdvx[var_ayzf][var_egyk + 1] + arg_xdvx[var_ayzf + 1][
            var_egyk + 1] + arg_xdvx[var_ayzf + 2][var_egyk + 1]
        var_tufr = arg_xdvx[var_ayzf][var_egyk + 2] + arg_xdvx[var_ayzf + 1][
            var_egyk + 2] + arg_xdvx[var_ayzf + 2][var_egyk + 2]
        if not (var_lgvi == var_lsgw and var_wvuc == var_lsgw and var_tufr ==
            var_lsgw):
            return False
        return True
