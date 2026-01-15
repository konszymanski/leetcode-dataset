class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bzkm:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)

        def func_osiz(arg_ayzf, arg_wnki):
            var_egyk = var_dcmd(arg_ayzf - arg_wnki)
            var_llti = var_hqta - var_egyk
            return var_zbxo(var_egyk, var_llti)
        var_rdmc = var_rjut.defaultdict(var_lsgw)
        for var_cbvh, var_yjch in var_dmio(arg_xdvx):
            var_rdmc[var_yjch].append(var_cbvh)
        var_ulfl = [(0, 0, 0)]
        var_lgvi = var_wvuc()
        while var_ulfl:
            var_tufr, var_xhfo, var_miuw = var_rhvk.heappop(var_ulfl)
            if var_miuw == var_wrnh:
                break
            if (var_xhfo, var_miuw) in var_lgvi:
                continue
            var_lgvi.add((var_xhfo, var_miuw))
            for var_yybh in var_rdmc[arg_rcsn[var_miuw]]:
                var_rhvk.heappush(var_ulfl, (var_tufr + func_osiz(var_xhfo,
                    var_yybh), var_yybh, var_miuw + 1))
        return var_tufr + var_wrnh
