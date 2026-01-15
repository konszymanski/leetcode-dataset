class Solution:
    var_udax = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        return arg_hqta[arg_rcsn][arg_bacg] == 1

    def func_rgwu(arg_xdvx, arg_rcsn, arg_bacg, arg_wrnh, arg_osiz, arg_ayzf):
        var_wnki = var_egyk(arg_osiz)
        var_dcmd = var_egyk(arg_osiz[0])
        func_rgwu = True
        var_llti = var_zbxo()
        var_llti.append((arg_rcsn, arg_bacg))
        arg_ayzf[arg_rcsn][arg_bacg] = True
        while var_llti:
            var_rdmc, var_rjut = var_llti.popleft()
            if not arg_xdvx.is_cell_land(var_rdmc, var_rjut, arg_wrnh):
                func_rgwu = False
            for var_lsgw in arg_xdvx.directions:
                var_cbvh = var_rdmc + var_lsgw[0]
                var_yjch = var_rjut + var_lsgw[1]
                if (0 <= var_cbvh < var_wnki and 0 <= var_yjch < var_dcmd and
                    not arg_ayzf[var_cbvh][var_yjch] and arg_xdvx.
                    is_cell_land(var_cbvh, var_yjch, arg_osiz)):
                    var_llti.append((var_cbvh, var_yjch))
                    arg_ayzf[var_cbvh][var_yjch] = True
        return func_rgwu

    def func_dmio(arg_xdvx, arg_wrnh: var_ulfl[var_ulfl[var_lgvi]],
        arg_osiz: var_ulfl[var_ulfl[var_lgvi]]) ->var_lgvi:
        var_wnki = var_egyk(arg_osiz)
        var_dcmd = var_egyk(arg_osiz[0])
        arg_ayzf = [([False] * var_dcmd) for var_wvuc in var_tufr(var_wnki)]
        var_xhfo = 0
        for arg_rcsn in var_tufr(var_wnki):
            for arg_bacg in var_tufr(var_dcmd):
                if not arg_ayzf[arg_rcsn][arg_bacg] and arg_xdvx.is_cell_land(
                    arg_rcsn, arg_bacg, arg_osiz) and arg_xdvx.is_sub_island(
                    arg_rcsn, arg_bacg, arg_wrnh, arg_osiz, arg_ayzf):
                    var_xhfo += 1
        return var_xhfo
