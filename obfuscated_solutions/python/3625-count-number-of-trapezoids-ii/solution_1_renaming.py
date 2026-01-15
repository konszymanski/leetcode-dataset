class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 10 ** 9 + 7
        var_osiz = var_ayzf(var_wnki)
        var_egyk = var_ayzf(var_wnki)
        var_dcmd = 0
        for var_llti in var_zbxo(var_hqta):
            var_rdmc, var_rjut = arg_xdvx[var_llti]
            for var_lsgw in var_zbxo(var_llti + 1, var_hqta):
                var_cbvh, var_yjch = arg_xdvx[var_lsgw]
                var_dmio = var_rdmc - var_cbvh
                var_ulfl = var_rjut - var_yjch
                if var_cbvh == var_rdmc:
                    var_lgvi = var_wrnh
                    var_wvuc = var_rdmc
                else:
                    var_lgvi = (var_yjch - var_rjut) / (var_cbvh - var_rdmc)
                    var_wvuc = (var_rjut * var_dmio - var_rdmc * var_ulfl
                        ) / var_dmio
                var_tufr = (var_rdmc + var_cbvh) * 10000 + (var_rjut + var_yjch
                    )
                var_osiz[var_lgvi].append(var_wvuc)
                var_egyk[var_tufr].append(var_lgvi)
        for var_xhfo in var_osiz.values():
            if var_rgwu(var_xhfo) == 1:
                continue
            var_miuw = var_ayzf(var_bacg)
            for var_rhvk in var_xhfo:
                var_miuw[var_rhvk] += 1
            var_yybh = 0
            for var_bzkm in var_miuw.values():
                var_dcmd += var_yybh * var_bzkm
                var_yybh += var_bzkm
        for var_icgs in var_egyk.values():
            if var_rgwu(var_icgs) == 1:
                continue
            var_miuw = var_ayzf(var_bacg)
            for var_wkgu in var_icgs:
                var_miuw[var_wkgu] += 1
            var_yybh = 0
            for var_bzkm in var_miuw.values():
                var_dcmd -= var_yybh * var_bzkm
                var_yybh += var_bzkm
        return var_dcmd
