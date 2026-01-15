class Solution:


    class Cell:

        def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
            arg_ihhe.height = arg_xdvx
            arg_ihhe.row = arg_rcsn
            arg_ihhe.col = arg_bacg

        def func_hqta(arg_ihhe, arg_rgwu):
            return arg_ihhe.height < arg_rgwu.height

    def func_wrnh(arg_ihhe, arg_rcsn, arg_bacg, arg_osiz, arg_ayzf):
        return 0 <= arg_rcsn < arg_osiz and 0 <= arg_bacg < arg_ayzf

    def func_wnki(arg_ihhe, arg_egyk):
        var_dcmd = [0, 0, -1, 1]
        var_llti = [-1, 1, 0, 0]
        arg_osiz = var_zbxo(arg_egyk)
        arg_ayzf = var_zbxo(arg_egyk[0])
        var_rdmc = [([False] * arg_ayzf) for var_rjut in var_lsgw(arg_osiz)]
        var_cbvh = []
        for var_yjch in var_lsgw(arg_osiz):
            var_dmio.heappush(var_cbvh, arg_ihhe.Cell(arg_egyk[var_yjch][0],
                var_yjch, 0))
            var_dmio.heappush(var_cbvh, arg_ihhe.Cell(arg_egyk[var_yjch][
                arg_ayzf - 1], var_yjch, arg_ayzf - 1))
            var_rdmc[var_yjch][0] = var_rdmc[var_yjch][arg_ayzf - 1] = True
        for var_yjch in var_lsgw(arg_ayzf):
            var_dmio.heappush(var_cbvh, arg_ihhe.Cell(arg_egyk[0][var_yjch],
                0, var_yjch))
            var_dmio.heappush(var_cbvh, arg_ihhe.Cell(arg_egyk[arg_osiz - 1
                ][var_yjch], arg_osiz - 1, var_yjch))
            var_rdmc[0][var_yjch] = var_rdmc[arg_osiz - 1][var_yjch] = True
        var_ulfl = 0
        while var_cbvh:
            var_lgvi = var_dmio.heappop(var_cbvh)
            var_wvuc = var_lgvi.row
            var_tufr = var_lgvi.col
            var_xhfo = var_lgvi.height
            for var_miuw in var_lsgw(4):
                var_rhvk = var_wvuc + var_dcmd[var_miuw]
                var_yybh = var_tufr + var_llti[var_miuw]
                if arg_ihhe._is_valid_cell(var_rhvk, var_yybh, arg_osiz,
                    arg_ayzf) and not var_rdmc[var_rhvk][var_yybh]:
                    var_bzkm = arg_egyk[var_rhvk][var_yybh]
                    if var_bzkm < var_xhfo:
                        var_ulfl += var_xhfo - var_bzkm
                    var_dmio.heappush(var_cbvh, arg_ihhe.Cell(var_icgs(
                        var_bzkm, var_xhfo), var_rhvk, var_yybh))
                    var_rdmc[var_rhvk][var_yybh] = True
        return var_ulfl
