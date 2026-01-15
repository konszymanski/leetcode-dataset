class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = var_wrnh.defaultdict(var_osiz)
        for var_ayzf, var_wnki, var_egyk in arg_rcsn:
            var_rgwu[var_ayzf][var_wnki] = var_rgwu[var_wnki][var_ayzf
                ] = var_egyk
        var_dcmd = [(0, 0)]
        var_llti = {(0): 0}
        var_zbxo = {}
        var_rdmc = 0
        while var_dcmd:
            var_rjut, var_lsgw = var_cbvh.heappop(var_dcmd)
            if var_rjut > var_llti[var_lsgw]:
                continue
            var_rdmc += 1
            for var_yjch, var_dmio in var_rgwu[var_lsgw].iteritems():
                var_wnki = var_ulfl(var_dmio, arg_bacg - var_rjut)
                var_zbxo[var_lsgw, var_yjch] = var_wnki
                var_lgvi = var_rjut + var_dmio + 1
                if var_lgvi < var_llti.get(var_yjch, arg_bacg + 1):
                    var_cbvh.heappush(var_dcmd, (var_lgvi, var_yjch))
                    var_llti[var_yjch] = var_lgvi
        for var_ayzf, var_wnki, var_egyk in arg_rcsn:
            var_rdmc += var_ulfl(var_egyk, var_zbxo.get((var_ayzf, var_wnki
                ), 0) + var_zbxo.get((var_wnki, var_ayzf), 0))
        return var_rdmc
