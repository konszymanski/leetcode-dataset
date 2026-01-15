class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_osiz[var_wrnh
        ], arg_bacg: var_osiz[var_wrnh], arg_hqta: var_osiz[var_osiz[
        var_wrnh]], arg_rgwu: var_wrnh) ->var_wrnh:
        var_ayzf = [[] for var_wnki in var_egyk(arg_xdvx)]
        for var_dcmd in arg_hqta:
            var_ayzf[var_dcmd[0] - 1].append(var_dcmd[1] - 1)

        def func_llti(arg_zbxo: var_wrnh):
            var_rdmc = arg_rcsn[arg_zbxo]
            var_rjut = arg_rcsn[arg_zbxo] // 2
            var_lsgw = [0] * (arg_rgwu + 1)
            var_cbvh = [0] * (arg_rgwu + 1)
            var_yjch = [0] * (arg_rgwu + 1)
            var_dmio = [0] * (arg_rgwu + 1)
            var_ulfl = var_rdmc
            for var_lgvi in var_ayzf[arg_zbxo]:
                var_wvuc, var_tufr, var_xhfo = func_llti(var_lgvi)
                var_ulfl += var_xhfo
                for var_miuw in var_egyk(arg_rgwu, -1, -1):
                    for var_rhvk in var_egyk(var_yybh(var_xhfo, var_miuw) + 1):
                        if var_miuw - var_rhvk >= 0:
                            var_yjch[var_miuw] = var_bzkm(var_yjch[var_miuw
                                ], var_yjch[var_miuw - var_rhvk] + var_wvuc
                                [var_rhvk])
                            var_dmio[var_miuw] = var_bzkm(var_dmio[var_miuw
                                ], var_dmio[var_miuw - var_rhvk] + var_tufr
                                [var_rhvk])
            for var_miuw in var_egyk(arg_rgwu + 1):
                var_lsgw[var_miuw] = var_yjch[var_miuw]
                var_cbvh[var_miuw] = var_yjch[var_miuw]
                if var_miuw >= var_rjut:
                    var_cbvh[var_miuw] = var_bzkm(var_yjch[var_miuw], 
                        var_dmio[var_miuw - var_rjut] + arg_bacg[arg_zbxo] -
                        var_rjut)
                if var_miuw >= var_rdmc:
                    var_lsgw[var_miuw] = var_bzkm(var_yjch[var_miuw], 
                        var_dmio[var_miuw - var_rdmc] + arg_bacg[arg_zbxo] -
                        var_rdmc)
            return var_lsgw, var_cbvh, var_ulfl
        return func_llti(0)[0][arg_rgwu]
