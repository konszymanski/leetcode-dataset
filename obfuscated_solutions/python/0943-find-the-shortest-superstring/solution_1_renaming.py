class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = [([0] * var_bacg) for var_wrnh in var_osiz(var_bacg)]
        for var_ayzf, var_wnki in var_egyk(arg_rcsn):
            for var_dcmd, var_llti in var_egyk(arg_rcsn):
                if var_ayzf != var_dcmd:
                    for var_zbxo in var_osiz(var_rdmc(var_hqta(var_wnki),
                        var_hqta(var_llti)), -1, -1):
                        if var_wnki.endswith(var_llti[:var_zbxo]):
                            var_rgwu[var_ayzf][var_dcmd] = var_zbxo
                            break
        var_rjut = [([0] * var_bacg) for var_wrnh in var_osiz(1 << var_bacg)]
        var_lsgw = [([None] * var_bacg) for var_wrnh in var_osiz(1 << var_bacg)
            ]
        for var_cbvh in var_osiz(1, 1 << var_bacg):
            for var_yjch in var_osiz(var_bacg):
                if var_cbvh >> var_yjch & 1:
                    var_dmio = var_cbvh ^ 1 << var_yjch
                    if var_dmio == 0:
                        continue
                    for var_ayzf in var_osiz(var_bacg):
                        if var_dmio >> var_ayzf & 1:
                            var_ulfl = var_rjut[var_dmio][var_ayzf] + var_rgwu[
                                var_ayzf][var_yjch]
                            if var_ulfl > var_rjut[var_cbvh][var_yjch]:
                                var_rjut[var_cbvh][var_yjch] = var_ulfl
                                var_lsgw[var_cbvh][var_yjch] = var_ayzf
        var_lgvi = []
        var_cbvh = (1 << var_bacg) - 1
        var_ayzf = var_wvuc(var_osiz(var_bacg), key=var_rjut[-1].__getitem__)
        while var_ayzf is not None:
            var_lgvi.append(var_ayzf)
            var_cbvh, var_ayzf = var_cbvh ^ 1 << var_ayzf, var_lsgw[var_cbvh][
                var_ayzf]
        var_lgvi = var_lgvi[::-1]
        var_tufr = [False] * var_bacg
        for var_wnki in var_lgvi:
            var_tufr[var_wnki] = True
        var_lgvi.extend([var_ayzf for var_ayzf in var_osiz(var_bacg) if not
            var_tufr[var_ayzf]])
        var_zbxo = [arg_rcsn[var_lgvi[0]]]
        for var_ayzf in var_osiz(1, var_hqta(var_lgvi)):
            var_xhfo = var_rgwu[var_lgvi[var_ayzf - 1]][var_lgvi[var_ayzf]]
            var_zbxo.append(arg_rcsn[var_lgvi[var_ayzf]][var_xhfo:])
        return ''.join(var_zbxo)
