class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        arg_xdvx.sort()
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = arg_xdvx[-1]
        var_wrnh = var_rgwu * 2
        var_osiz = [0] * var_wrnh
        var_ayzf = [0] * (var_rgwu + 1)
        var_wnki = 0
        for var_egyk in var_dcmd(var_wrnh):
            while var_wnki < var_bacg and arg_xdvx[var_wnki] <= var_egyk:
                var_wnki += 1
            var_osiz[var_egyk] = var_wnki
        for var_llti in var_dcmd(var_bacg):
            var_ayzf[arg_xdvx[var_llti]] += 1
        var_zbxo, var_rdmc = 0, var_rgwu
        while var_zbxo < var_rdmc:
            var_rjut = (var_zbxo + var_rdmc) // 2
            var_lsgw = arg_ihhe._count_pairs(arg_xdvx, var_osiz, var_ayzf,
                var_rjut)
            if var_lsgw < arg_rcsn:
                var_zbxo = var_rjut + 1
            else:
                var_rdmc = var_rjut
        return var_zbxo

    def func_cbvh(arg_ihhe, arg_xdvx, var_osiz, var_ayzf, arg_yjch):
        var_lsgw = 0
        var_bacg = var_hqta(arg_xdvx)
        var_wnki = 0
        while var_wnki < var_bacg:
            var_dmio = arg_xdvx[var_wnki]
            var_ulfl = var_ayzf[var_dmio]
            var_lgvi = var_osiz[var_wvuc(var_dmio + arg_yjch, var_hqta(
                var_osiz) - 1)] - var_osiz[var_dmio]
            var_tufr = var_ulfl * (var_ulfl - 1) // 2
            var_lsgw += var_lgvi * var_ulfl + var_tufr
            while var_wnki + 1 < var_bacg and arg_xdvx[var_wnki] == arg_xdvx[
                var_wnki + 1]:
                var_wnki += 1
            var_wnki += 1
        return var_lsgw
