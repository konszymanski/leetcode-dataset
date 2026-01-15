class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_hqta[var_rgwu]], arg_bacg: var_hqta[var_rgwu]) ->var_hqta[
        var_rgwu]:
        var_wrnh = var_osiz(arg_bacg)
        var_ayzf = {var_wnki: var_egyk for var_egyk, var_wnki in var_dcmd(
            arg_xdvx)}
        var_llti = var_zbxo(var_hqta)
        var_rdmc = [0] * var_rjut(arg_xdvx)
        for var_lsgw, var_cbvh in var_dcmd(arg_rcsn):
            for var_yjch in var_cbvh:
                if var_yjch not in var_wrnh:
                    var_llti[var_yjch].append(arg_xdvx[var_lsgw])
                    var_rdmc[var_lsgw] += 1
        var_dmio = var_ulfl(var_egyk for var_egyk, var_lgvi in var_dcmd(
            var_rdmc) if var_lgvi == 0)
        var_wvuc = []
        while var_dmio:
            var_lsgw = var_dmio.popleft()
            var_wnki = arg_xdvx[var_lsgw]
            var_wvuc.append(var_wnki)
            for var_tufr in var_llti[var_wnki]:
                var_rdmc[var_ayzf[var_tufr]] -= 1
                if var_rdmc[var_ayzf[var_tufr]] == 0:
                    var_dmio.append(var_ayzf[var_tufr])
        return var_wvuc
