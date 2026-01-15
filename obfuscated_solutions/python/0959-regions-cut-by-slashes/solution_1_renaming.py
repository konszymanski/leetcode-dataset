class Solution:
    var_udax = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = [([0] * (var_bacg * 3)) for var_wrnh in var_osiz(
            var_bacg * 3)]
        for var_ayzf in var_osiz(var_bacg):
            for var_wnki in var_osiz(var_bacg):
                var_egyk = var_ayzf * 3
                var_dcmd = var_wnki * 3
                if arg_rcsn[var_ayzf][var_wnki] == '\\':
                    var_rgwu[var_egyk][var_dcmd] = 1
                    var_rgwu[var_egyk + 1][var_dcmd + 1] = 1
                    var_rgwu[var_egyk + 2][var_dcmd + 2] = 1
                elif arg_rcsn[var_ayzf][var_wnki] == '/':
                    var_rgwu[var_egyk][var_dcmd + 2] = 1
                    var_rgwu[var_egyk + 1][var_dcmd + 1] = 1
                    var_rgwu[var_egyk + 2][var_dcmd] = 1
        var_llti = 0
        for var_ayzf in var_osiz(var_bacg * 3):
            for var_wnki in var_osiz(var_bacg * 3):
                if var_rgwu[var_ayzf][var_wnki] == 0:
                    arg_xdvx._flood_fill(var_rgwu, var_ayzf, var_wnki)
                    var_llti += 1
        return var_llti

    def func_zbxo(arg_xdvx, var_rgwu, arg_rdmc, arg_rjut):
        var_lsgw = [(arg_rdmc, arg_rjut)]
        var_rgwu[arg_rdmc][arg_rjut] = 1
        while var_lsgw:
            var_cbvh = var_lsgw.pop(0)
            for var_yjch in arg_xdvx.DIRECTIONS:
                var_dmio = var_yjch[0] + var_cbvh[0]
                var_ulfl = var_yjch[1] + var_cbvh[1]
                if arg_xdvx._is_valid_cell(var_rgwu, var_dmio, var_ulfl):
                    var_rgwu[var_dmio][var_ulfl] = 1
                    var_lsgw.append((var_dmio, var_ulfl))

    def func_lgvi(arg_xdvx, var_rgwu, arg_rdmc, arg_rjut):
        var_wvuc = var_hqta(var_rgwu)
        return (arg_rdmc >= 0 and arg_rjut >= 0 and arg_rdmc < var_wvuc and
            arg_rjut < var_wvuc and var_rgwu[arg_rdmc][arg_rjut] == 0)
