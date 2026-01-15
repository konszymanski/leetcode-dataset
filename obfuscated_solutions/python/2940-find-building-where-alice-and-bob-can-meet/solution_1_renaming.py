class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = [(-1) for var_rgwu in var_wrnh(var_osiz(arg_rcsn))]
        var_ayzf = [[] for var_rgwu in var_wrnh(var_osiz(arg_xdvx))]
        for var_wnki in var_wrnh(var_osiz(arg_rcsn)):
            var_egyk = arg_rcsn[var_wnki][0]
            var_dcmd = arg_rcsn[var_wnki][1]
            if var_egyk > var_dcmd:
                var_egyk, var_dcmd = var_dcmd, var_egyk
            if arg_xdvx[var_dcmd] > arg_xdvx[var_egyk] or var_egyk == var_dcmd:
                var_hqta[var_wnki] = var_dcmd
            else:
                var_ayzf[var_dcmd].append((arg_xdvx[var_egyk], var_wnki))
        for var_wnki in var_wrnh(var_osiz(arg_xdvx) - 1, -1, -1):
            var_llti = var_osiz(var_bacg)
            for var_egyk, var_dcmd in var_ayzf[var_wnki]:
                var_zbxo = arg_ihhe.search(var_egyk, var_bacg)
                if var_zbxo < var_llti and var_zbxo >= 0:
                    var_hqta[var_dcmd] = var_bacg[var_zbxo][1]
            while var_bacg and var_bacg[-1][0] <= arg_xdvx[var_wnki]:
                var_bacg.pop()
            var_bacg.append((arg_xdvx[var_wnki], var_wnki))
        return var_hqta

    def func_rdmc(arg_ihhe, arg_rjut, var_bacg):
        var_lsgw = 0
        var_cbvh = var_osiz(var_bacg) - 1
        var_yjch = -1
        while var_lsgw <= var_cbvh:
            var_dmio = (var_lsgw + var_cbvh) // 2
            if var_bacg[var_dmio][0] > arg_rjut:
                var_yjch = var_ulfl(var_yjch, var_dmio)
                var_lsgw = var_dmio + 1
            else:
                var_cbvh = var_dmio - 1
        return var_yjch
