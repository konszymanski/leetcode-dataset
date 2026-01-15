class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        arg_ihhe.row2, arg_ihhe.col2 = 0, 0

    def func_xdvx(arg_ihhe, arg_rcsn: var_wrnh, arg_bacg: var_wrnh,
        arg_hqta: var_wrnh, arg_rgwu: var_wrnh) ->var_osiz:
        return 0 <= arg_rcsn < arg_hqta and 0 <= arg_bacg < arg_rgwu

    def func_ayzf(arg_ihhe, arg_wnki: var_dcmd[var_dcmd[var_wrnh]],
        arg_egyk: var_dcmd[var_dcmd[var_osiz]], arg_rcsn: var_wrnh,
        arg_bacg: var_wrnh):
        arg_egyk[arg_rcsn][arg_bacg] = True
        arg_ihhe.row2 = var_llti(arg_ihhe.row2, arg_rcsn)
        arg_ihhe.col2 = var_llti(arg_ihhe.col2, arg_bacg)
        for var_zbxo in arg_ihhe.dirs:
            var_rdmc, var_rjut = arg_rcsn + var_zbxo[0], arg_bacg + var_zbxo[1]
            if arg_ihhe.is_within_farm(var_rdmc, var_rjut, var_lsgw(
                arg_wnki), var_lsgw(arg_wnki[0])) and not arg_egyk[var_rdmc][
                var_rjut] and arg_wnki[var_rdmc][var_rjut] == 1:
                arg_ihhe.dfs(arg_wnki, arg_egyk, var_rdmc, var_rjut)

    def func_cbvh(arg_ihhe, arg_wnki: var_dcmd[var_dcmd[var_wrnh]]) ->var_dcmd[
        var_dcmd[var_wrnh]]:
        arg_egyk = [([False] * var_lsgw(arg_wnki[0])) for var_yjch in
            var_dmio(var_lsgw(arg_wnki))]
        var_ulfl = []
        for var_lgvi in var_dmio(var_lsgw(arg_wnki)):
            for var_wvuc in var_dmio(var_lsgw(arg_wnki[0])):
                if arg_wnki[var_lgvi][var_wvuc] == 1 and not arg_egyk[var_lgvi
                    ][var_wvuc]:
                    arg_ihhe.row2, arg_ihhe.col2 = 0, 0
                    arg_ihhe.dfs(arg_wnki, arg_egyk, var_lgvi, var_wvuc)
                    var_ulfl.append([var_lgvi, var_wvuc, arg_ihhe.row2,
                        arg_ihhe.col2])
        return var_ulfl
