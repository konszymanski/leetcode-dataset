class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_rgwu[var_hqta]]) ->var_rgwu[
        var_rgwu[var_hqta]]:
        var_wrnh = arg_ihhe.__topo_sort(arg_rcsn, arg_xdvx)
        var_osiz = arg_ihhe.__topo_sort(arg_bacg, arg_xdvx)
        if not var_wrnh or not var_osiz:
            return []
        var_ayzf = [([0] * arg_xdvx) for var_wnki in var_egyk(arg_xdvx)]
        for var_dcmd in var_egyk(arg_xdvx):
            for var_llti in var_egyk(arg_xdvx):
                if var_wrnh[var_dcmd] == var_osiz[var_llti]:
                    var_ayzf[var_dcmd][var_llti] = var_wrnh[var_dcmd]
        return var_ayzf

    def func_zbxo(arg_ihhe, arg_rdmc, arg_rjut):
        var_lsgw = [[] for var_wnki in var_egyk(arg_rjut + 1)]
        var_cbvh = [0] * (arg_rjut + 1)
        var_yjch = []
        for var_dmio in arg_rdmc:
            var_lsgw[var_dmio[0]].append(var_dmio[1])
            var_cbvh[var_dmio[1]] += 1
        var_ulfl = var_lgvi()
        for var_dcmd in var_egyk(1, arg_rjut + 1):
            if var_cbvh[var_dcmd] == 0:
                var_ulfl.append(var_dcmd)
        while var_ulfl:
            var_wvuc = var_ulfl.popleft()
            var_yjch.append(var_wvuc)
            arg_rjut -= 1
            for var_tufr in var_lsgw[var_wvuc]:
                var_cbvh[var_tufr] -= 1
                if var_cbvh[var_tufr] == 0:
                    var_ulfl.append(var_tufr)
        if arg_rjut != 0:
            return []
        return var_yjch
