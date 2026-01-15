class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu[var_hqta, var_hqta]]) ->var_bacg[var_rjut]:
        var_wrnh = [False] * var_osiz(arg_rcsn)
        var_ayzf = []
        for var_wnki in var_egyk(1, var_osiz(arg_xdvx)):
            if arg_xdvx[var_wnki] % 2 == arg_xdvx[var_wnki - 1] % 2:
                var_ayzf.append(var_wnki)
        for var_wnki in var_egyk(var_osiz(arg_rcsn)):
            var_dcmd = arg_rcsn[var_wnki]
            var_llti = var_dcmd[0]
            var_zbxo = var_dcmd[1]
            var_rdmc = arg_ihhe.binarySearch(var_llti + 1, var_zbxo, var_ayzf)
            if var_rdmc:
                var_wrnh[var_wnki] = False
            else:
                var_wrnh[var_wnki] = True
        return var_wrnh

    def func_lsgw(arg_ihhe, var_llti: var_hqta, var_zbxo: var_hqta,
        var_ayzf: var_bacg[var_hqta]) ->var_rjut:
        var_cbvh = 0
        var_yjch = var_osiz(var_ayzf) - 1
        while var_cbvh <= var_yjch:
            var_dmio = var_cbvh + (var_yjch - var_cbvh) // 2
            var_ulfl = var_ayzf[var_dmio]
            if var_ulfl < var_llti:
                var_cbvh = var_dmio + 1
            elif var_ulfl > var_zbxo:
                var_yjch = var_dmio - 1
            else:
                return True
        return False
