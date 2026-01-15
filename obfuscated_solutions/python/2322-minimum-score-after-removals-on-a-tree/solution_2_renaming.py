class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        return var_rgwu(arg_xdvx, arg_rcsn, arg_bacg) - var_wrnh(arg_xdvx,
            arg_rcsn, arg_bacg)

    def func_osiz(arg_ihhe, arg_ayzf: var_egyk[var_hqta], arg_wnki:
        var_egyk[var_egyk[var_hqta]]) ->var_hqta:
        var_dcmd = var_llti(arg_ayzf)
        var_zbxo = 0
        var_rdmc = [0] * var_dcmd
        var_rjut = [0] * var_dcmd
        var_lsgw = [0] * var_dcmd
        var_cbvh = [[] for var_yjch in var_dmio(var_dcmd)]
        for var_ulfl, var_lgvi in arg_wnki:
            var_cbvh[var_ulfl].append(var_lgvi)
            var_cbvh[var_lgvi].append(var_ulfl)

        def func_wvuc(arg_tufr: var_hqta, arg_xhfo: var_hqta):
            nonlocal cnt
            var_rjut[arg_tufr] = var_zbxo
            var_zbxo += 1
            var_rdmc[arg_tufr] = arg_ayzf[arg_tufr]
            for var_miuw in var_cbvh[arg_tufr]:
                if var_miuw == arg_xhfo:
                    continue
                func_wvuc(var_miuw, arg_tufr)
                var_rdmc[arg_tufr] ^= var_rdmc[var_miuw]
            var_lsgw[arg_tufr] = var_zbxo
        func_wvuc(0, -1)
        var_rhvk = var_yybh('inf')
        for var_ulfl in var_dmio(1, var_dcmd):
            for var_lgvi in var_dmio(var_ulfl + 1, var_dcmd):
                if var_rjut[var_lgvi] > var_rjut[var_ulfl] and var_rjut[
                    var_lgvi] < var_lsgw[var_ulfl]:
                    var_rhvk = var_wrnh(var_rhvk, arg_ihhe.calc(var_rdmc[0] ^
                        var_rdmc[var_ulfl], var_rdmc[var_ulfl] ^ var_rdmc[
                        var_lgvi], var_rdmc[var_lgvi]))
                elif var_rjut[var_ulfl] > var_rjut[var_lgvi] and var_rjut[
                    var_ulfl] < var_lsgw[var_lgvi]:
                    var_rhvk = var_wrnh(var_rhvk, arg_ihhe.calc(var_rdmc[0] ^
                        var_rdmc[var_lgvi], var_rdmc[var_lgvi] ^ var_rdmc[
                        var_ulfl], var_rdmc[var_ulfl]))
                else:
                    var_rhvk = var_wrnh(var_rhvk, arg_ihhe.calc(var_rdmc[0] ^
                        var_rdmc[var_ulfl] ^ var_rdmc[var_lgvi], var_rdmc[
                        var_ulfl], var_rdmc[var_lgvi]))
        return var_rhvk
