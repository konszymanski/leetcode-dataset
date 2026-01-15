class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = [0] + var_wnki(var_egyk(arg_xdvx))
        var_dcmd = [0] * var_rgwu
        var_llti = [0] * var_rgwu
        var_zbxo = [0] * 3
        var_rdmc = var_ayzf[arg_rcsn] - var_ayzf[0]
        for var_rjut in var_lsgw(arg_rcsn, var_rgwu):
            var_cbvh = var_ayzf[var_rjut + 1] - var_ayzf[var_rjut + 1 -
                arg_rcsn]
            if var_cbvh > var_rdmc:
                var_dcmd[var_rjut] = var_rjut + 1 - arg_rcsn
                var_rdmc = var_cbvh
            else:
                var_dcmd[var_rjut] = var_dcmd[var_rjut - 1]
        var_llti[var_rgwu - arg_rcsn] = var_rgwu - arg_rcsn
        var_rdmc = var_ayzf[var_rgwu] - var_ayzf[var_rgwu - arg_rcsn]
        for var_rjut in var_lsgw(var_rgwu - arg_rcsn - 1, -1, -1):
            var_cbvh = var_ayzf[var_rjut + arg_rcsn] - var_ayzf[var_rjut]
            if var_cbvh >= var_rdmc:
                var_llti[var_rjut] = var_rjut
                var_rdmc = var_cbvh
            else:
                var_llti[var_rjut] = var_llti[var_rjut + 1]
        for var_rjut in var_lsgw(arg_rcsn, var_rgwu - 2 * arg_rcsn + 1):
            var_yjch = var_dcmd[var_rjut - 1]
            var_dmio = var_llti[var_rjut + arg_rcsn]
            var_ulfl = var_ayzf[var_rjut + arg_rcsn] - var_ayzf[var_rjut
                ] + var_ayzf[var_yjch + arg_rcsn] - var_ayzf[var_yjch
                ] + var_ayzf[var_dmio + arg_rcsn] - var_ayzf[var_dmio]
            if var_ulfl > var_osiz:
                var_osiz = var_ulfl
                var_zbxo = [var_yjch, var_rjut, var_dmio]
        return var_zbxo
