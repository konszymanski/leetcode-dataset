class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:

        def func_hqta(arg_rgwu: var_bacg, arg_wrnh: var_ayzf, arg_osiz:
            var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
            var_wnki = var_egyk([(arg_rgwu, 0)])
            var_dcmd = 0
            while var_wnki:
                var_llti, var_zbxo = var_wnki.popleft()
                for var_rdmc in arg_osiz[var_llti]:
                    if var_rdmc in arg_wrnh:
                        continue
                    arg_wrnh.add(var_rdmc)
                    var_wnki.append((var_rdmc, var_zbxo + 1))
                    var_dcmd = var_rjut(var_dcmd, var_zbxo + 1)
            return var_dcmd
        var_lsgw = var_cbvh(arg_xdvx)
        arg_osiz = [[] for var_yjch in var_dmio(var_lsgw)]
        for var_ulfl in var_dmio(var_lsgw):
            arg_osiz[arg_xdvx[var_ulfl]].append(var_ulfl)
        var_lgvi = 0
        var_wvuc = 0
        var_tufr = [False] * var_lsgw
        for var_ulfl in var_dmio(var_lsgw):
            if not var_tufr[var_ulfl]:
                var_xhfo = {}
                var_miuw = var_ulfl
                var_rhvk = 0
                while True:
                    if var_tufr[var_miuw]:
                        break
                    var_tufr[var_miuw] = True
                    var_xhfo[var_miuw] = var_rhvk
                    var_rhvk += 1
                    var_yybh = arg_xdvx[var_miuw]
                    if var_yybh in var_xhfo:
                        var_bzkm = var_rhvk - var_xhfo[var_yybh]
                        var_lgvi = var_rjut(var_lgvi, var_bzkm)
                        if var_bzkm == 2:
                            arg_wrnh = {var_miuw, var_yybh}
                            var_wvuc += 2 + func_hqta(var_yybh, arg_wrnh,
                                arg_osiz) + func_hqta(var_miuw, arg_wrnh,
                                arg_osiz)
                        break
                    var_miuw = var_yybh
        return var_rjut(var_lgvi, var_wvuc)
