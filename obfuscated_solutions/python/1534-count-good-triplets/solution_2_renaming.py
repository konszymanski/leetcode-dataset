class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu[var_wrnh], arg_rcsn:
        var_wrnh, arg_bacg: var_wrnh, arg_hqta: var_wrnh) ->var_wrnh:
        var_osiz = 0
        var_ayzf = var_wnki(arg_xdvx)
        var_egyk = [0] * 1001
        for var_dcmd in var_llti(var_ayzf):
            for var_zbxo in var_llti(var_dcmd + 1, var_ayzf):
                if var_rdmc(arg_xdvx[var_dcmd] - arg_xdvx[var_zbxo]
                    ) <= arg_bacg:
                    var_rjut, var_lsgw = arg_xdvx[var_dcmd
                        ] - arg_rcsn, arg_xdvx[var_dcmd] + arg_rcsn
                    var_cbvh, var_yjch = arg_xdvx[var_zbxo
                        ] - arg_hqta, arg_xdvx[var_zbxo] + arg_hqta
                    var_dmio = var_ulfl(0, var_rjut, var_cbvh)
                    var_lgvi = var_wvuc(1000, var_lsgw, var_yjch)
                    if var_dmio <= var_lgvi:
                        var_osiz += var_egyk[var_lgvi
                            ] if var_dmio == 0 else var_egyk[var_lgvi
                            ] - var_egyk[var_dmio - 1]
            for var_zbxo in var_llti(arg_xdvx[var_dcmd], 1001):
                var_egyk[var_zbxo] += 1
        return var_osiz
