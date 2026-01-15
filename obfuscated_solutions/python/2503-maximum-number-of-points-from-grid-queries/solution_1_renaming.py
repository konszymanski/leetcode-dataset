class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_xdvx[0])
        var_ayzf = [0] * var_osiz(arg_rcsn)
        var_wnki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for var_egyk, var_dcmd in var_llti(arg_rcsn):
            var_zbxo = var_rdmc([(0, 0)])
            var_rjut = [([0] * var_wrnh) for var_lsgw in var_cbvh(var_rgwu)]
            var_rjut[0][0] = 1
            var_yjch = 0
            while var_zbxo:
                var_dmio = var_osiz(var_zbxo)
                for var_lsgw in var_cbvh(var_dmio):
                    var_ulfl, var_lgvi = var_zbxo.popleft()
                    if arg_xdvx[var_ulfl][var_lgvi] >= var_dcmd:
                        continue
                    var_yjch += 1
                    for var_wvuc, var_tufr in var_wnki:
                        var_xhfo = var_ulfl + var_wvuc
                        var_miuw = var_lgvi + var_tufr
                        if (0 <= var_xhfo < var_rgwu and 0 <= var_miuw <
                            var_wrnh and not var_rjut[var_xhfo][var_miuw] and
                            arg_xdvx[var_xhfo][var_miuw] < var_dcmd):
                            var_zbxo.append((var_xhfo, var_miuw))
                            var_rjut[var_xhfo][var_miuw] = 1
                var_ayzf[var_egyk] = var_yjch
        return var_ayzf
