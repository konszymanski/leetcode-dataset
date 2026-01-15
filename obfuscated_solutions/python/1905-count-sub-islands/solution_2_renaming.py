class Solution:
    var_udax = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        return arg_hqta[arg_rcsn][arg_bacg] == 1

    def func_rgwu(arg_xdvx, arg_rcsn, arg_bacg, arg_wrnh, arg_osiz, arg_ayzf):
        var_wnki = var_egyk(arg_osiz)
        var_dcmd = var_egyk(arg_osiz[0])
        func_rgwu = True
        if not arg_xdvx.is_cell_land(arg_rcsn, arg_bacg, arg_wrnh):
            func_rgwu = False
        for var_llti in arg_xdvx.directions:
            var_zbxo = arg_rcsn + var_llti[0]
            var_rdmc = arg_bacg + var_llti[1]
            if (0 <= var_zbxo < var_wnki and 0 <= var_rdmc < var_dcmd and 
                not arg_ayzf[var_zbxo][var_rdmc] and arg_xdvx.is_cell_land(
                var_zbxo, var_rdmc, arg_osiz)):
                arg_ayzf[var_zbxo][var_rdmc] = True
                var_rjut = arg_xdvx.is_sub_island(var_zbxo, var_rdmc,
                    arg_wrnh, arg_osiz, arg_ayzf)
                func_rgwu = func_rgwu and var_rjut
        return func_rgwu

    def func_lsgw(arg_xdvx, arg_wrnh: var_cbvh[var_cbvh[var_yjch]],
        arg_osiz: var_cbvh[var_cbvh[var_yjch]]) ->var_yjch:
        var_wnki = var_egyk(arg_osiz)
        var_dcmd = var_egyk(arg_osiz[0])
        arg_ayzf = [([False] * var_dcmd) for var_dmio in var_ulfl(var_wnki)]
        var_lgvi = 0
        for arg_rcsn in var_ulfl(var_wnki):
            for arg_bacg in var_ulfl(var_dcmd):
                if not arg_ayzf[arg_rcsn][arg_bacg] and arg_xdvx.is_cell_land(
                    arg_rcsn, arg_bacg, arg_osiz):
                    arg_ayzf[arg_rcsn][arg_bacg] = True
                    if arg_xdvx.is_sub_island(arg_rcsn, arg_bacg, arg_wrnh,
                        arg_osiz, arg_ayzf):
                        var_lgvi += 1
        return var_lgvi
