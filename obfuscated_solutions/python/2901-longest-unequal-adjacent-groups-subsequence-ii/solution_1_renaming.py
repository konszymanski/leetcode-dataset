class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_bacg[var_hqta]:
        var_wrnh = var_osiz(arg_rcsn)
        var_ayzf = [1] * var_wrnh
        var_wnki = [-1] * var_wrnh
        var_egyk = 0
        for var_dcmd in var_llti(1, var_wrnh):
            for var_zbxo in var_llti(var_dcmd):
                if arg_ihhe.check(arg_xdvx[var_dcmd], arg_xdvx[var_zbxo]
                    ) and var_ayzf[var_zbxo] + 1 > var_ayzf[var_dcmd
                    ] and arg_rcsn[var_dcmd] != arg_rcsn[var_zbxo]:
                    var_ayzf[var_dcmd] = var_ayzf[var_zbxo] + 1
                    var_wnki[var_dcmd] = var_zbxo
            if var_ayzf[var_dcmd] > var_ayzf[var_egyk]:
                var_egyk = var_dcmd
        var_rdmc = []
        var_dcmd = var_egyk
        while var_dcmd >= 0:
            var_rdmc.append(arg_xdvx[var_dcmd])
            var_dcmd = var_wnki[var_dcmd]
        var_rdmc.reverse()
        return var_rdmc

    def func_rjut(arg_ihhe, arg_lsgw: var_hqta, arg_cbvh: var_hqta) ->var_wvuc:
        if var_osiz(arg_lsgw) != var_osiz(arg_cbvh):
            return False
        var_yjch = 0
        for var_dmio, var_ulfl in var_lgvi(arg_lsgw, arg_cbvh):
            if var_dmio != var_ulfl:
                var_yjch += 1
                if var_yjch > 1:
                    return False
        return var_yjch == 1
