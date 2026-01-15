class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_rgwu[var_hqta]:
        arg_rcsn.sort(key=lambda x: var_wrnh[2])
        var_osiz = var_ayzf(var_wnki)
        for var_wrnh, var_egyk, var_dcmd in arg_rcsn:
            var_osiz[var_dcmd].append((var_wrnh, var_egyk))
        var_llti = var_zbxo(arg_xdvx)
        var_llti.unite(arg_bacg, 0)
        for var_dcmd in var_osiz:
            for var_wrnh, var_egyk in var_osiz[var_dcmd]:
                var_llti.unite(var_wrnh, var_egyk)
            for var_wrnh, var_egyk in var_osiz[var_dcmd]:
                if not var_llti.connected(var_wrnh, 0):
                    var_llti.reset(var_wrnh)
                    var_llti.reset(var_egyk)
        return [var_rdmc for var_rdmc in var_rjut(arg_xdvx) if var_llti.
            connected(var_rdmc, 0)]


class UnionFind:

    def func_lsgw(arg_ihhe, arg_cbvh: var_hqta):
        arg_ihhe.parent = [var_rdmc for var_rdmc in var_rjut(arg_cbvh)]
        arg_ihhe.rank = [0] * arg_cbvh

    def func_yjch(arg_ihhe, var_wrnh: var_hqta) ->var_hqta:
        if arg_ihhe.parent[var_wrnh] != var_wrnh:
            arg_ihhe.parent[var_wrnh] = arg_ihhe.find(arg_ihhe.parent[var_wrnh]
                )
        return arg_ihhe.parent[var_wrnh]

    def func_dmio(arg_ihhe, var_wrnh: var_hqta, var_egyk: var_hqta) ->None:
        var_ulfl = arg_ihhe.find(var_wrnh)
        var_lgvi = arg_ihhe.find(var_egyk)
        if var_ulfl != var_lgvi:
            if arg_ihhe.rank[var_ulfl] > arg_ihhe.rank[var_lgvi]:
                arg_ihhe.parent[var_lgvi] = var_ulfl
            elif arg_ihhe.rank[var_ulfl] < arg_ihhe.rank[var_lgvi]:
                arg_ihhe.parent[var_ulfl] = var_lgvi
            else:
                arg_ihhe.parent[var_lgvi] = var_ulfl
                arg_ihhe.rank[var_ulfl] += 1

    def func_wvuc(arg_ihhe, var_wrnh: var_hqta, var_egyk: var_hqta) ->var_tufr:
        return arg_ihhe.find(var_wrnh) == arg_ihhe.find(var_egyk)

    def func_xhfo(arg_ihhe, var_wrnh: var_hqta) ->None:
        arg_ihhe.parent[var_wrnh] = var_wrnh
        arg_ihhe.rank[var_wrnh] = 0
