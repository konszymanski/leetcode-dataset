from collections import Counter


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(var_rgwu.keys())

        def func_wnki(arg_egyk, arg_dcmd, arg_llti) ->var_hqta:
            var_zbxo = var_rgwu[var_osiz[arg_llti]]
            var_osiz[arg_llti], var_osiz[arg_dcmd] = var_osiz[arg_dcmd
                ], var_osiz[arg_llti]
            var_rdmc = arg_egyk
            for var_rjut in var_lsgw(arg_egyk, arg_dcmd):
                if var_rgwu[var_osiz[var_rjut]] < var_zbxo:
                    var_osiz[var_rdmc], var_osiz[var_rjut] = var_osiz[var_rjut
                        ], var_osiz[var_rdmc]
                    var_rdmc += 1
            var_osiz[arg_dcmd], var_osiz[var_rdmc] = var_osiz[var_rdmc
                ], var_osiz[arg_dcmd]
            return var_rdmc

        def func_cbvh(arg_egyk, arg_dcmd, arg_yjch) ->None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            if arg_egyk == arg_dcmd:
                return
            arg_llti = var_dmio.randint(arg_egyk, arg_dcmd)
            arg_llti = func_wnki(arg_egyk, arg_dcmd, arg_llti)
            if arg_yjch == arg_llti:
                return
            elif arg_yjch < arg_llti:
                func_cbvh(arg_egyk, arg_llti - 1, arg_yjch)
            else:
                func_cbvh(arg_llti + 1, arg_dcmd, arg_yjch)
        var_ulfl = var_lgvi(var_osiz)
        func_cbvh(0, var_ulfl - 1, var_ulfl - arg_rcsn)
        return var_osiz[var_ulfl - arg_rcsn:]
