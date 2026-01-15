class Solution:
    var_udax = 0
    var_ihhe = 1
    var_xdvx = 2
    var_rcsn = 3

    def func_bacg(arg_hqta, arg_rgwu: var_wnki, arg_wrnh: var_wnki,
        arg_osiz: var_egyk[var_egyk[var_wnki]], arg_ayzf: var_dcmd) ->None:
        if arg_rgwu < 0 or arg_rgwu >= var_llti(arg_osiz
            ) or arg_wrnh < 0 or arg_wrnh >= var_llti(arg_osiz[0]) or arg_osiz[
            arg_rgwu][arg_wrnh] == arg_hqta.GUARD or arg_osiz[arg_rgwu][
            arg_wrnh] == arg_hqta.WALL:
            return
        arg_osiz[arg_rgwu][arg_wrnh] = arg_hqta.GUARDED
        if arg_ayzf == 'U':
            arg_hqta._recurse(arg_rgwu - 1, arg_wrnh, arg_osiz, 'U')
        if arg_ayzf == 'D':
            arg_hqta._recurse(arg_rgwu + 1, arg_wrnh, arg_osiz, 'D')
        if arg_ayzf == 'L':
            arg_hqta._recurse(arg_rgwu, arg_wrnh - 1, arg_osiz, 'L')
        if arg_ayzf == 'R':
            arg_hqta._recurse(arg_rgwu, arg_wrnh + 1, arg_osiz, 'R')

    def func_zbxo(arg_hqta, arg_rdmc: var_wnki, arg_rjut: var_wnki,
        arg_lsgw: var_egyk[var_egyk[var_wnki]], arg_cbvh: var_egyk[var_egyk
        [var_wnki]]) ->var_wnki:
        arg_osiz = [([arg_hqta.UNGUARDED] * arg_rjut) for var_yjch in
            var_dmio(arg_rdmc)]
        for var_ulfl in arg_lsgw:
            arg_osiz[var_ulfl[0]][var_ulfl[1]] = arg_hqta.GUARD
        for var_lgvi in arg_cbvh:
            arg_osiz[var_lgvi[0]][var_lgvi[1]] = arg_hqta.WALL
        for var_ulfl in arg_lsgw:
            arg_hqta._recurse(var_ulfl[0] - 1, var_ulfl[1], arg_osiz, 'U')
            arg_hqta._recurse(var_ulfl[0] + 1, var_ulfl[1], arg_osiz, 'D')
            arg_hqta._recurse(var_ulfl[0], var_ulfl[1] - 1, arg_osiz, 'L')
            arg_hqta._recurse(var_ulfl[0], var_ulfl[1] + 1, arg_osiz, 'R')
        var_wvuc = var_tufr(arg_rgwu.count(arg_hqta.UNGUARDED) for arg_rgwu in
            arg_osiz)
        return var_wvuc
