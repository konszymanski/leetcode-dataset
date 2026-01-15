class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_wrnh,
        arg_bacg: var_osiz[var_wrnh], arg_hqta: var_osiz[var_wrnh],
        arg_rgwu: var_osiz[var_ayzf]) ->var_ayzf:
        var_wnki = 0
        var_egyk = [([var_dcmd('inf')] * 26) for var_llti in var_zbxo(26)]
        for var_rdmc, var_rjut, var_lsgw in var_cbvh(arg_bacg, arg_hqta,
            arg_rgwu):
            var_yjch = var_dmio(var_rdmc) - var_dmio('a')
            var_ulfl = var_dmio(var_rjut) - var_dmio('a')
            var_egyk[var_yjch][var_ulfl] = var_lgvi(var_egyk[var_yjch][
                var_ulfl], var_lsgw)
        for var_wvuc in var_zbxo(26):
            for var_tufr in var_zbxo(26):
                for var_xhfo in var_zbxo(26):
                    var_egyk[var_tufr][var_xhfo] = var_lgvi(var_egyk[
                        var_tufr][var_xhfo], var_egyk[var_tufr][var_wvuc] +
                        var_egyk[var_wvuc][var_xhfo])
        for var_miuw, var_rhvk in var_cbvh(arg_xdvx, arg_rcsn):
            if var_miuw == var_rhvk:
                continue
            var_yybh = var_dmio(var_miuw) - var_dmio('a')
            var_bzkm = var_dmio(var_rhvk) - var_dmio('a')
            if var_egyk[var_yybh][var_bzkm] == var_dcmd('inf'):
                return -1
            var_wnki += var_egyk[var_yybh][var_bzkm]
        return var_wnki
