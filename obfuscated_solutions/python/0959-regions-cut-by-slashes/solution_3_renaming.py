class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_yjch:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_hqta + 1
        var_osiz = var_wrnh * var_wrnh
        var_ayzf = [-1] * var_osiz
        for var_wnki in var_egyk(var_wrnh):
            for var_dcmd in var_egyk(var_wrnh):
                if (var_wnki == 0 or var_dcmd == 0 or var_wnki == var_wrnh -
                    1 or var_dcmd == var_wrnh - 1):
                    var_llti = var_wnki * var_wrnh + var_dcmd
                    var_ayzf[var_llti] = 0
        var_ayzf[0] = -1
        var_zbxo = 1
        for var_wnki in var_egyk(var_hqta):
            for var_dcmd in var_egyk(var_hqta):
                if arg_xdvx[var_wnki][var_dcmd] == '/':
                    var_rdmc = var_wnki * var_wrnh + (var_dcmd + 1)
                    var_rjut = (var_wnki + 1) * var_wrnh + var_dcmd
                    var_zbxo += arg_ihhe._union(var_ayzf, var_rdmc, var_rjut)
                elif arg_xdvx[var_wnki][var_dcmd] == '\\':
                    var_lsgw = var_wnki * var_wrnh + var_dcmd
                    var_cbvh = (var_wnki + 1) * var_wrnh + (var_dcmd + 1)
                    var_zbxo += arg_ihhe._union(var_ayzf, var_lsgw, var_cbvh)
        return var_zbxo

    def func_dmio(arg_ihhe, var_ayzf: var_rcsn[var_yjch], arg_ulfl: var_yjch
        ) ->var_yjch:
        if var_ayzf[arg_ulfl] == -1:
            return arg_ulfl
        var_ayzf[arg_ulfl] = arg_ihhe._find(var_ayzf, var_ayzf[arg_ulfl])
        return var_ayzf[arg_ulfl]

    def func_lgvi(arg_ihhe, var_ayzf: var_rcsn[var_yjch], arg_wvuc:
        var_yjch, arg_tufr: var_yjch) ->var_yjch:
        var_xhfo = arg_ihhe._find(var_ayzf, arg_wvuc)
        var_miuw = arg_ihhe._find(var_ayzf, arg_tufr)
        if var_xhfo == var_miuw:
            return 1
        var_ayzf[var_miuw] = var_xhfo
        return 0
