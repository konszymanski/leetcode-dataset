class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_hqta]:

        def func_rgwu(arg_wrnh, arg_osiz, arg_ayzf, arg_wnki, arg_egyk):
            var_dcmd = 1 - arg_ayzf % 2
            arg_egyk[arg_wrnh] = arg_ayzf % 2
            for var_llti in arg_wnki[arg_wrnh]:
                if var_llti == arg_osiz:
                    continue
                var_dcmd += func_rgwu(var_llti, arg_wrnh, arg_ayzf + 1,
                    arg_wnki, arg_egyk)
            return var_dcmd

        def func_zbxo(arg_rdmc, arg_egyk):
            var_rjut = var_lsgw(arg_rdmc) + 1
            arg_wnki = [[] for var_cbvh in var_yjch(var_rjut)]
            for var_dmio, var_ulfl in arg_rdmc:
                arg_wnki[var_dmio].append(var_ulfl)
                arg_wnki[var_ulfl].append(var_dmio)
            var_dcmd = func_rgwu(0, -1, 0, arg_wnki, arg_egyk)
            return [var_dcmd, var_rjut - var_dcmd]
        var_rjut = var_lsgw(arg_xdvx) + 1
        var_lgvi = var_lsgw(arg_rcsn) + 1
        var_wvuc = [0] * var_rjut
        var_tufr = [0] * var_lgvi
        var_xhfo = func_zbxo(arg_xdvx, var_wvuc)
        var_miuw = func_zbxo(arg_rcsn, var_tufr)
        var_dcmd = [0] * var_rjut
        for var_rhvk in var_yjch(var_rjut):
            var_dcmd[var_rhvk] = var_xhfo[var_wvuc[var_rhvk]] + var_yybh(
                var_miuw[0], var_miuw[1])
        return var_dcmd
