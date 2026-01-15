class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = 10 ** 9 + 7
        var_hqta, var_rgwu = 0, var_wrnh(arg_xdvx)
        var_osiz = [0] * 10
        for var_ayzf in arg_xdvx:
            var_wnki = var_egyk(var_ayzf)
            var_osiz[var_wnki] += 1
            var_hqta += var_wnki
        if var_hqta % 2 != 0:
            return 0
        var_dcmd = var_hqta // 2
        var_llti = (var_rgwu + 1) // 2
        var_zbxo = [([0] * (var_llti + 1)) for var_rdmc in var_rjut(
            var_dcmd + 1)]
        var_zbxo[0][0] = 1
        var_lsgw = var_cbvh = 0
        for var_yjch in var_rjut(10):
            var_lsgw += var_osiz[var_yjch]
            var_cbvh += var_yjch * var_osiz[var_yjch]
            for var_dmio in var_rjut(var_ulfl(var_lsgw, var_llti), var_lgvi
                (0, var_lsgw - (var_rgwu - var_llti)) - 1, -1):
                var_wvuc = var_lsgw - var_dmio
                for var_tufr in var_rjut(var_ulfl(var_cbvh, var_dcmd), 
                    var_lgvi(0, var_cbvh - var_dcmd) - 1, -1):
                    var_xhfo = 0
                    for var_miuw in var_rjut(var_lgvi(0, var_osiz[var_yjch] -
                        var_wvuc), var_ulfl(var_osiz[var_yjch], var_dmio) + 1):
                        if var_yjch * var_miuw > var_tufr:
                            break
                        var_rhvk = var_yybh(var_dmio, var_miuw) * var_yybh(
                            var_wvuc, var_osiz[var_yjch] - var_miuw) % var_bacg
                        var_xhfo = (var_xhfo + var_rhvk * var_zbxo[var_tufr -
                            var_yjch * var_miuw][var_dmio - var_miuw] %
                            var_bacg) % var_bacg
                    var_zbxo[var_tufr][var_dmio] = var_xhfo % var_bacg
        return var_zbxo[var_dcmd][var_llti]
