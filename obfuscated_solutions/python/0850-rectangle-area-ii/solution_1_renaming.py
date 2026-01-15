class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz = var_ayzf(), var_ayzf()
        for var_wnki, var_egyk, var_dcmd, var_llti in arg_xdvx:
            var_wrnh.add(var_wnki)
            var_wrnh.add(var_dcmd)
            var_osiz.add(var_egyk)
            var_osiz.add(var_llti)
        var_zbxo = var_rdmc(var_wrnh)
        var_rjut = var_rdmc(var_osiz)
        var_lsgw = {var_cbvh: var_yjch for var_yjch, var_cbvh in var_dmio(
            var_zbxo)}
        var_ulfl = {var_lgvi: var_yjch for var_yjch, var_lgvi in var_dmio(
            var_rjut)}
        var_wvuc = [([0] * var_rgwu(var_rjut)) for var_tufr in var_zbxo]
        for var_wnki, var_egyk, var_dcmd, var_llti in arg_xdvx:
            for var_cbvh in var_xhfo(var_lsgw[var_wnki], var_lsgw[var_dcmd]):
                for var_lgvi in var_xhfo(var_ulfl[var_egyk], var_ulfl[var_llti]
                    ):
                    var_wvuc[var_cbvh][var_lgvi] = 1
        var_miuw = 0
        for var_cbvh, var_rhvk in var_dmio(var_wvuc):
            for var_lgvi, var_yybh in var_dmio(var_rhvk):
                if var_yybh:
                    var_miuw += (var_zbxo[var_cbvh + 1] - var_zbxo[var_cbvh]
                        ) * (var_rjut[var_lgvi + 1] - var_rjut[var_lgvi])
        return var_miuw % (10 ** 9 + 7)
