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
        var_yjch, var_dmio = var_ulfl(var_rgwu, var_wrnh), 0
        for var_dcmd in var_egyk(1, var_rgwu + 1):
            for var_llti in var_egyk(1, var_wrnh + 1):
                for var_lgvi in var_egyk(var_dmio + 1, var_yjch + 1):
                    if (var_dcmd + var_lgvi - 1 <= var_rgwu and var_llti +
                        var_lgvi - 1 <= var_wrnh and func_zbxo(var_dcmd,
                        var_llti, var_dcmd + var_lgvi - 1, var_llti +
                        var_lgvi - 1) <= arg_rcsn):
                        var_dmio += 1
                    else:
                        break
        return var_dmio
