class Solution:
    var_udax = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_rcsn), var_osiz(arg_rcsn[0])
        var_ayzf = [(0, 0, 0)]
        var_wnki = [([var_egyk('inf')] * var_wrnh) for var_dcmd in var_llti
            (var_rgwu)]
        var_wnki[0][0] = 0
        while var_ayzf:
            var_zbxo, var_rdmc, var_rjut = var_lsgw.heappop(var_ayzf)
            if var_wnki[var_rdmc][var_rjut] != var_zbxo:
                continue
            for var_cbvh, (var_yjch, var_dmio) in var_ulfl(arg_xdvx._dirs):
                var_lgvi, var_wvuc = var_rdmc + var_yjch, var_rjut + var_dmio
                if 0 <= var_lgvi < var_rgwu and 0 <= var_wvuc < var_wrnh:
                    var_tufr = var_zbxo + (var_cbvh != arg_rcsn[var_rdmc][
                        var_rjut] - 1)
                    if var_wnki[var_lgvi][var_wvuc] > var_tufr:
                        var_wnki[var_lgvi][var_wvuc] = var_tufr
                        var_lsgw.heappush(var_ayzf, (var_tufr, var_lgvi,
                            var_wvuc))
        return var_wnki[var_rgwu - 1][var_wrnh - 1]
