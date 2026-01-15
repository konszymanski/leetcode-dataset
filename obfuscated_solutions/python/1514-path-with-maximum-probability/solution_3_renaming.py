class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_osiz[var_osiz
        [var_wrnh]], arg_bacg: var_osiz[var_ayzf], arg_hqta: var_wrnh,
        arg_rgwu: var_wrnh) ->var_ayzf:
        var_wnki = var_egyk(var_dcmd)
        for var_llti, (var_zbxo, var_rdmc) in var_rjut(arg_rcsn):
            var_wnki[var_zbxo].append((var_rdmc, arg_bacg[var_llti]))
            var_wnki[var_rdmc].append((var_zbxo, arg_bacg[var_llti]))
        var_lsgw = [0.0] * arg_xdvx
        var_lsgw[arg_hqta] = 1.0
        var_cbvh = [(-1.0, arg_hqta)]
        while var_cbvh:
            var_yjch, var_dmio = var_ulfl.heappop(var_cbvh)
            if var_dmio == arg_rgwu:
                return -var_yjch
            if var_wnki[var_dmio]:
                for var_lgvi, var_wvuc in var_wnki[var_dmio]:
                    if -var_yjch * var_wvuc > var_lsgw[var_lgvi]:
                        var_lsgw[var_lgvi] = -var_yjch * var_wvuc
                        var_ulfl.heappush(var_cbvh, (-var_lsgw[var_lgvi],
                            var_lgvi))
                var_wnki[var_dmio].clear()
        return 0.0
