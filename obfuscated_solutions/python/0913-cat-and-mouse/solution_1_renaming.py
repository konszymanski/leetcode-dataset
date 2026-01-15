class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)

        def func_rgwu(arg_wrnh, arg_osiz, arg_ayzf):
            if arg_ayzf == 2:
                for var_wnki in arg_rcsn[arg_wrnh]:
                    yield var_wnki, arg_osiz, 3 - arg_ayzf
            else:
                for var_egyk in arg_rcsn[arg_osiz]:
                    if var_egyk:
                        yield arg_wrnh, var_egyk, 3 - arg_ayzf
        var_dcmd, var_llti, var_zbxo = 0, 1, 2
        var_rdmc = var_rjut.defaultdict(var_lsgw)
        var_cbvh = {}
        for arg_wrnh in var_yjch(var_bacg):
            for arg_osiz in var_yjch(var_bacg):
                var_cbvh[arg_wrnh, arg_osiz, 1] = var_hqta(arg_rcsn[arg_wrnh])
                var_cbvh[arg_wrnh, arg_osiz, 2] = var_hqta(arg_rcsn[arg_osiz]
                    ) - (0 in arg_rcsn[arg_osiz])
        var_dmio = var_rjut.deque([])
        for var_ulfl in var_yjch(var_bacg):
            for arg_ayzf in var_yjch(1, 3):
                var_rdmc[0, var_ulfl, arg_ayzf] = var_llti
                var_dmio.append((0, var_ulfl, arg_ayzf, var_llti))
                if var_ulfl > 0:
                    var_rdmc[var_ulfl, var_ulfl, arg_ayzf] = var_zbxo
                    var_dmio.append((var_ulfl, var_ulfl, arg_ayzf, var_zbxo))
        while var_dmio:
            var_ulfl, var_lgvi, arg_ayzf, arg_osiz = var_dmio.popleft()
            for var_wvuc, var_tufr, var_xhfo in func_rgwu(var_ulfl,
                var_lgvi, arg_ayzf):
                if var_rdmc[var_wvuc, var_tufr, var_xhfo] is var_dcmd:
                    if var_xhfo == arg_osiz:
                        var_rdmc[var_wvuc, var_tufr, var_xhfo] = arg_osiz
                        var_dmio.append((var_wvuc, var_tufr, var_xhfo,
                            arg_osiz))
                    else:
                        var_cbvh[var_wvuc, var_tufr, var_xhfo] -= 1
                        if var_cbvh[var_wvuc, var_tufr, var_xhfo] == 0:
                            var_rdmc[var_wvuc, var_tufr, var_xhfo
                                ] = 3 - var_xhfo
                            var_dmio.append((var_wvuc, var_tufr, var_xhfo, 
                                3 - var_xhfo))
        return var_rdmc[1, 2, 1]
