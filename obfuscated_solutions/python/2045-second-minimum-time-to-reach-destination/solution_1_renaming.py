import heapq


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_wrnh
        [var_rgwu]], arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_rgwu:
        var_osiz = [[] for var_ayzf in var_wnki(arg_xdvx + 1)]
        for var_egyk, var_dcmd in arg_rcsn:
            var_osiz[var_egyk].append(var_dcmd)
            var_osiz[var_dcmd].append(var_egyk)
        var_llti = [var_zbxo('inf')] * (arg_xdvx + 1)
        var_rdmc = [var_zbxo('inf')] * (arg_xdvx + 1)
        var_rjut = [0] * (arg_xdvx + 1)
        var_lsgw = [(0, 1)]
        var_llti[1] = 0
        while var_lsgw:
            var_cbvh, var_yjch = var_dmio.heappop(var_lsgw)
            var_rjut[var_yjch] += 1
            if var_rjut[var_yjch] == 2 and var_yjch == arg_xdvx:
                return var_cbvh
            if var_cbvh // arg_hqta % 2:
                var_cbvh = arg_hqta * (var_cbvh // arg_hqta + 1) + arg_bacg
            else:
                var_cbvh = var_cbvh + arg_bacg
            for var_ulfl in var_osiz[var_yjch]:
                if var_rjut[var_ulfl] == 2:
                    continue
                if var_llti[var_ulfl] > var_cbvh:
                    var_rdmc[var_ulfl] = var_llti[var_ulfl]
                    var_llti[var_ulfl] = var_cbvh
                    var_dmio.heappush(var_lsgw, (var_cbvh, var_ulfl))
                elif var_rdmc[var_ulfl] > var_cbvh and var_llti[var_ulfl
                    ] != var_cbvh:
                    var_rdmc[var_ulfl] = var_cbvh
                    var_dmio.heappush(var_lsgw, (var_cbvh, var_ulfl))
        return 0
