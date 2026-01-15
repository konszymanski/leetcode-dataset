class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_hqta[var_rgwu]],
        arg_rcsn: var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * (var_wrnh + 1)
        var_wnki = [0] * var_wrnh
        for var_egyk in var_dcmd(var_wrnh):
            var_ayzf[var_egyk + 1] = var_ayzf[var_egyk] + arg_xdvx[var_egyk][1]
            var_wnki[var_egyk] = arg_xdvx[var_egyk][0]
        var_llti = 0
        for var_zbxo in var_dcmd(arg_bacg // 2 + 1):
            var_rdmc = arg_bacg - 2 * var_zbxo
            var_rjut = arg_rcsn - var_zbxo
            var_lsgw = arg_rcsn + var_rdmc
            var_cbvh = var_yjch(var_wnki, var_rjut)
            var_dmio = var_ulfl(var_wnki, var_lsgw)
            var_llti = var_lgvi(var_llti, var_ayzf[var_dmio] - var_ayzf[
                var_cbvh])
            var_rdmc = arg_bacg - 2 * var_zbxo
            var_rjut = arg_rcsn - var_rdmc
            var_lsgw = arg_rcsn + var_zbxo
            var_cbvh = var_yjch(var_wnki, var_rjut)
            var_dmio = var_ulfl(var_wnki, var_lsgw)
            var_llti = var_lgvi(var_llti, var_ayzf[var_dmio] - var_ayzf[
                var_cbvh])
        return var_llti
