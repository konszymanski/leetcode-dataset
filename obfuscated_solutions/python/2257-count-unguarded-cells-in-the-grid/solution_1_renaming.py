class Solution:
    var_udax = 0
    var_ihhe = 1
    var_xdvx = 2
    var_rcsn = 3

    def func_bacg(arg_hqta, arg_rgwu: var_ayzf, arg_wrnh: var_ayzf,
        arg_osiz: var_wnki[var_wnki[var_ayzf]]) ->None:
        for var_egyk in var_dcmd(arg_rgwu - 1, -1, -1):
            if arg_osiz[var_egyk][arg_wrnh] == arg_hqta.WALL or arg_osiz[
                var_egyk][arg_wrnh] == arg_hqta.GUARD:
                break
            arg_osiz[var_egyk][arg_wrnh] = arg_hqta.GUARDED
        for var_egyk in var_dcmd(arg_rgwu + 1, var_llti(arg_osiz)):
            if arg_osiz[var_egyk][arg_wrnh] == arg_hqta.WALL or arg_osiz[
                var_egyk][arg_wrnh] == arg_hqta.GUARD:
                break
            arg_osiz[var_egyk][arg_wrnh] = arg_hqta.GUARDED
        for var_zbxo in var_dcmd(arg_wrnh - 1, -1, -1):
            if arg_osiz[arg_rgwu][var_zbxo] == arg_hqta.WALL or arg_osiz[
                arg_rgwu][var_zbxo] == arg_hqta.GUARD:
                break
            arg_osiz[arg_rgwu][var_zbxo] = arg_hqta.GUARDED
        for var_zbxo in var_dcmd(arg_wrnh + 1, var_llti(arg_osiz[0])):
            if arg_osiz[arg_rgwu][var_zbxo] == arg_hqta.WALL or arg_osiz[
                arg_rgwu][var_zbxo] == arg_hqta.GUARD:
                break
            arg_osiz[arg_rgwu][var_zbxo] = arg_hqta.GUARDED

    def func_rdmc(arg_hqta, arg_rjut: var_ayzf, arg_lsgw: var_ayzf,
        arg_cbvh: var_wnki[var_wnki[var_ayzf]], arg_yjch: var_wnki[var_wnki
        [var_ayzf]]) ->var_ayzf:
        arg_osiz = [([arg_hqta.UNGUARDED] * arg_lsgw) for var_dmio in
            var_dcmd(arg_rjut)]
        for var_ulfl in arg_cbvh:
            arg_osiz[var_ulfl[0]][var_ulfl[1]] = arg_hqta.GUARD
        for var_lgvi in arg_yjch:
            arg_osiz[var_lgvi[0]][var_lgvi[1]] = arg_hqta.WALL
        for var_ulfl in arg_cbvh:
            arg_hqta._mark_guarded(var_ulfl[0], var_ulfl[1], arg_osiz)
        var_wvuc = 0
        for arg_rgwu in arg_osiz:
            for var_tufr in arg_rgwu:
                if var_tufr == arg_hqta.UNGUARDED:
                    var_wvuc += 1
        return var_wvuc
