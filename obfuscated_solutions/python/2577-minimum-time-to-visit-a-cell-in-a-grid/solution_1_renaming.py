class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        if arg_xdvx[0][1] > 1 and arg_xdvx[1][0] > 1:
            return -1
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var_ayzf = var_wnki()
        var_egyk = [(arg_xdvx[0][0], 0, 0)]
        while var_egyk:
            var_dcmd, var_llti, var_zbxo = var_rdmc.heappop(var_egyk)
            if (var_llti, var_zbxo) == (var_hqta - 1, var_rgwu - 1):
                return var_dcmd
            if (var_llti, var_zbxo) in var_ayzf:
                continue
            var_ayzf.add((var_llti, var_zbxo))
            for var_rjut, var_lsgw in var_osiz:
                var_cbvh, var_yjch = var_llti + var_rjut, var_zbxo + var_lsgw
                if not arg_ihhe._is_valid(var_ayzf, var_cbvh, var_yjch,
                    var_hqta, var_rgwu):
                    continue
                var_dmio = 1 if (arg_xdvx[var_cbvh][var_yjch] - var_dcmd
                    ) % 2 == 0 else 0
                var_ulfl = var_lgvi(arg_xdvx[var_cbvh][var_yjch] + var_dmio,
                    var_dcmd + 1)
                var_rdmc.heappush(var_egyk, (var_ulfl, var_cbvh, var_yjch))
        return -1

    def func_wvuc(arg_ihhe, var_ayzf, var_llti, var_zbxo, var_hqta, var_rgwu):
        return 0 <= var_llti < var_hqta and 0 <= var_zbxo < var_rgwu and (
            var_llti, var_zbxo) not in var_ayzf
