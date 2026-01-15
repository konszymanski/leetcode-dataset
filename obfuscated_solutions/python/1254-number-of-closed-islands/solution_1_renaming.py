class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [([False] * var_wrnh) for var_ayzf in var_wnki(var_hqta)]
        var_egyk = 0
        for var_dcmd in var_wnki(var_hqta):
            for var_llti in var_wnki(var_wrnh):
                if arg_xdvx[var_dcmd][var_llti] == 0 and not var_osiz[var_dcmd
                    ][var_llti] and arg_ihhe.bfs(var_dcmd, var_llti,
                    var_hqta, var_wrnh, arg_xdvx, var_osiz):
                    var_egyk += 1
        return var_egyk

    def func_zbxo(arg_ihhe, arg_rdmc: var_bacg, arg_rjut: var_bacg,
        var_hqta: var_bacg, var_wrnh: var_bacg, arg_xdvx: var_rcsn[var_rcsn
        [var_bacg]], var_osiz: var_rcsn[var_rcsn[var_lsgw]]) ->var_lsgw:
        var_cbvh = var_yjch([(arg_rdmc, arg_rjut)])
        var_osiz[arg_rdmc][arg_rjut] = True
        var_dmio = True
        var_ulfl = [0, 1, 0, -1]
        var_lgvi = [-1, 0, 1, 0]
        while var_cbvh:
            arg_rdmc, arg_rjut = var_cbvh.popleft()
            for var_dcmd in var_wnki(4):
                var_wvuc, var_tufr = arg_rdmc + var_ulfl[var_dcmd
                    ], arg_rjut + var_lgvi[var_dcmd]
                if (var_wvuc < 0 or var_wvuc >= var_hqta or var_tufr < 0 or
                    var_tufr >= var_wrnh):
                    var_dmio = False
                elif arg_xdvx[var_wvuc][var_tufr] == 0 and not var_osiz[
                    var_wvuc][var_tufr]:
                    var_cbvh.append((var_wvuc, var_tufr))
                    var_osiz[var_wvuc][var_tufr] = True
        return var_dmio
