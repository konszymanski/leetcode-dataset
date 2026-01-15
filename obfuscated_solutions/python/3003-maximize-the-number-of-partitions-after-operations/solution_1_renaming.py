class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [([0] * 3) for var_ayzf in var_wnki(var_rgwu)]
        var_egyk = [([0] * 3) for var_ayzf in var_wnki(var_rgwu)]
        var_dcmd, var_llti, var_zbxo = 0, 0, 0
        for var_rdmc in var_wnki(var_rgwu - 1):
            var_rjut = 1 << var_lsgw(arg_xdvx[var_rdmc]) - var_lsgw('a')
            if not var_llti & var_rjut:
                var_zbxo += 1
                if var_zbxo <= arg_rcsn:
                    var_llti |= var_rjut
                else:
                    var_dcmd += 1
                    var_llti = var_rjut
                    var_zbxo = 1
            var_osiz[var_rdmc + 1][0] = var_dcmd
            var_osiz[var_rdmc + 1][1] = var_llti
            var_osiz[var_rdmc + 1][2] = var_zbxo
        var_dcmd, var_llti, var_zbxo = 0, 0, 0
        for var_rdmc in var_wnki(var_rgwu - 1, 0, -1):
            var_rjut = 1 << var_lsgw(arg_xdvx[var_rdmc]) - var_lsgw('a')
            if not var_llti & var_rjut:
                var_zbxo += 1
                if var_zbxo <= arg_rcsn:
                    var_llti |= var_rjut
                else:
                    var_dcmd += 1
                    var_llti = var_rjut
                    var_zbxo = 1
            var_egyk[var_rdmc - 1][0] = var_dcmd
            var_egyk[var_rdmc - 1][1] = var_llti
            var_egyk[var_rdmc - 1][2] = var_zbxo
        var_cbvh = 0
        for var_rdmc in var_wnki(var_rgwu):
            var_yjch = var_osiz[var_rdmc][0] + var_egyk[var_rdmc][0] + 2
            var_dmio = var_osiz[var_rdmc][1] | var_egyk[var_rdmc][1]
            var_ulfl = var_lgvi(var_dmio).count('1')
            if var_osiz[var_rdmc][2] == arg_rcsn and var_egyk[var_rdmc][2
                ] == arg_rcsn and var_ulfl < 26:
                var_yjch += 1
            elif var_wvuc(var_ulfl + 1, 26) <= arg_rcsn:
                var_yjch -= 1
            var_cbvh = var_tufr(var_cbvh, var_yjch)
        return var_cbvh
