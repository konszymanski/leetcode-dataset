class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_xdvx[0])
        var_ayzf = [([0] * (var_wrnh + 1)) for var_wnki in var_egyk(
            var_rgwu + 1)]
        for var_dcmd in var_egyk(1, var_rgwu + 1):
            for var_llti in var_egyk(1, var_wrnh + 1):
                var_ayzf[var_dcmd][var_llti] = var_ayzf[var_dcmd - 1][var_llti
                    ] + var_ayzf[var_dcmd][var_llti - 1] - var_ayzf[
                    var_dcmd - 1][var_llti - 1] + arg_xdvx[var_dcmd - 1][
                    var_llti - 1]

        def func_zbxo(arg_rdmc, arg_rjut, arg_lsgw, arg_cbvh):
            return var_ayzf[arg_lsgw][arg_cbvh] - var_ayzf[arg_rdmc - 1][
                arg_cbvh] - var_ayzf[arg_lsgw][arg_rjut - 1] + var_ayzf[
                arg_rdmc - 1][arg_rjut - 1]
        var_yjch, var_dmio, var_ulfl = 1, var_lgvi(var_rgwu, var_wrnh), 0
        while var_yjch <= var_dmio:
            var_wvuc = (var_yjch + var_dmio) // 2
            var_tufr = var_xhfo(func_zbxo(var_dcmd, var_llti, var_dcmd +
                var_wvuc - 1, var_llti + var_wvuc - 1) <= arg_rcsn for
                var_dcmd in var_egyk(1, var_rgwu - var_wvuc + 2) for
                var_llti in var_egyk(1, var_wrnh - var_wvuc + 2))
            if var_tufr:
                var_ulfl = var_wvuc
                var_yjch = var_wvuc + 1
            else:
                var_dmio = var_wvuc - 1
        return var_ulfl
