class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = {}
        var_rgwu = {}
        var_wrnh = {}
        for var_osiz in arg_xdvx:
            var_ayzf, var_wnki = var_osiz
            var_hqta[var_ayzf] = 0
            var_rgwu[var_wnki] = 0

        def func_egyk(arg_dcmd):
            var_llti = var_zbxo(arg_dcmd.keys())
            for var_rdmc, var_rjut in var_lsgw(var_llti):
                arg_dcmd[var_rjut] = var_rdmc + 1
        func_egyk(var_hqta)
        func_egyk(var_rgwu)
        var_cbvh = var_yjch(var_hqta) + 1
        var_dmio = var_yjch(var_rgwu) + 1
        arg_dcmd = [([0] * var_dmio) for var_ulfl in var_lgvi(var_cbvh)]
        var_wvuc = [([0] * var_dmio) for var_ulfl in var_lgvi(var_cbvh)]
        for var_osiz in arg_xdvx:
            var_ayzf, var_wnki = var_osiz
            var_tufr = var_hqta[var_ayzf]
            var_xhfo = var_rgwu[var_wnki]
            var_wrnh[var_miuw(var_osiz)] = var_tufr, var_xhfo
            arg_dcmd[var_tufr][var_xhfo] = 1
        for var_rhvk in var_lgvi(1, var_cbvh):
            for var_yybh in var_lgvi(1, var_dmio):
                var_wvuc[var_rhvk][var_yybh] = var_wvuc[var_rhvk - 1][var_yybh
                    ] + var_wvuc[var_rhvk][var_yybh - 1] - var_wvuc[
                    var_rhvk - 1][var_yybh - 1] + arg_dcmd[var_rhvk][var_yybh]
        var_bzkm = 0
        arg_xdvx.sort(key=lambda p: (var_icgs[0], -var_icgs[1]))
        var_wkgu = var_yjch(arg_xdvx)
        for var_rhvk in var_lgvi(var_wkgu - 1):
            for var_yybh in var_lgvi(var_rhvk + 1, var_wkgu):
                if arg_xdvx[var_rhvk][1] >= arg_xdvx[var_yybh][1]:
                    var_pmuo, var_eieh = var_wrnh[var_miuw(arg_xdvx[var_rhvk])]
                    var_xrri, var_xsns = var_wrnh[var_miuw(arg_xdvx[var_yybh])]
                    var_mlhe = var_wvuc[var_xrri][var_eieh] - var_wvuc[
                        var_pmuo - 1][var_eieh] - var_wvuc[var_xrri][
                        var_xsns - 1] + var_wvuc[var_pmuo - 1][var_xsns - 1]
                    if var_mlhe == 2:
                        var_bzkm += 1
        return var_bzkm
