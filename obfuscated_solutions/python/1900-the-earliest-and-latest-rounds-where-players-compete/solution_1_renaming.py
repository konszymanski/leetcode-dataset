class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_wvuc[var_hqta]:

        @var_lgvi
        def func_rgwu(arg_xdvx: var_hqta, arg_wrnh: var_hqta, arg_osiz:
            var_hqta) ->(var_hqta, var_hqta):
            if arg_wrnh + arg_osiz == arg_xdvx + 1:
                return 1, 1
            if arg_wrnh + arg_osiz > arg_xdvx + 1:
                return func_rgwu(arg_xdvx, arg_xdvx + 1 - arg_osiz, 
                    arg_xdvx + 1 - arg_wrnh)
            var_ayzf, var_wnki = var_egyk('inf'), var_egyk('-inf')
            var_dcmd = (arg_xdvx + 1) // 2
            if arg_osiz <= var_dcmd:
                for var_llti in var_zbxo(arg_wrnh):
                    for var_rdmc in var_zbxo(arg_osiz - arg_wrnh):
                        var_rjut, var_lsgw = func_rgwu(var_dcmd, var_llti +
                            1, var_llti + var_rdmc + 2)
                        var_ayzf = var_cbvh(var_ayzf, var_rjut)
                        var_wnki = var_yjch(var_wnki, var_lsgw)
            else:
                var_dmio = arg_xdvx + 1 - arg_osiz
                var_ulfl = (arg_xdvx - 2 * var_dmio + 1) // 2
                for var_llti in var_zbxo(arg_wrnh):
                    for var_rdmc in var_zbxo(var_dmio - arg_wrnh):
                        var_rjut, var_lsgw = func_rgwu(var_dcmd, var_llti +
                            1, var_llti + var_rdmc + var_ulfl + 2)
                        var_ayzf = var_cbvh(var_ayzf, var_rjut)
                        var_wnki = var_yjch(var_wnki, var_lsgw)
            return var_ayzf + 1, var_wnki + 1
        if arg_rcsn > arg_bacg:
            arg_rcsn, arg_bacg = arg_bacg, arg_rcsn
        var_ayzf, var_wnki = func_rgwu(arg_xdvx, arg_rcsn, arg_bacg)
        func_rgwu.cache_clear()
        return [var_ayzf, var_wnki]
