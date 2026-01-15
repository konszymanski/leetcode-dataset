class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_xdvx[0])

        @var_dmio
        def func_ayzf(arg_wnki, arg_egyk, arg_dcmd, arg_llti, arg_zbxo):
            var_rdmc, var_rjut = arg_wnki + var_hqta[arg_dcmd][0
                ], arg_egyk + var_hqta[arg_dcmd][1]
            if (var_rdmc < 0 or var_rjut < 0 or var_rdmc >= var_rgwu or 
                var_rjut >= var_wrnh or arg_xdvx[var_rdmc][var_rjut] !=
                arg_zbxo):
                return 0
            var_lsgw = 1 if arg_llti else 0
            var_cbvh = func_ayzf(var_rdmc, var_rjut, arg_dcmd, arg_llti, 2 -
                arg_zbxo)
            if arg_llti:
                var_cbvh = var_yjch(var_cbvh, func_ayzf(var_rdmc, var_rjut,
                    (arg_dcmd + 1) % 4, False, 2 - arg_zbxo))
            return var_cbvh + 1
        var_ulfl = 0
        for var_lgvi in var_wvuc(var_rgwu):
            for var_tufr in var_wvuc(var_wrnh):
                if arg_xdvx[var_lgvi][var_tufr] == 1:
                    for arg_dcmd in var_wvuc(4):
                        var_ulfl = var_yjch(var_ulfl, func_ayzf(var_lgvi,
                            var_tufr, arg_dcmd, True, 2) + 1)
        return var_ulfl
