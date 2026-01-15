class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        arg_xdvx.sort()
        arg_rcsn.sort()
        var_rgwu = []
        for var_wrnh in arg_rcsn:
            for var_osiz in var_ayzf(var_wrnh[1]):
                var_rgwu.append(var_wrnh[0])
        var_wnki = var_egyk(arg_xdvx)
        var_dcmd = var_egyk(var_rgwu)
        var_llti = [(0) for var_zbxo in var_ayzf(var_dcmd + 1)]
        var_rdmc = [(0) for var_zbxo in var_ayzf(var_dcmd + 1)]
        var_rdmc[var_dcmd] = 1000000000000.0
        for var_osiz in var_ayzf(var_wnki - 1, -1, -1):
            for var_rjut in var_ayzf(var_dcmd - 1, -1, -1):
                var_lsgw = var_cbvh(arg_xdvx[var_osiz] - var_rgwu[var_rjut]
                    ) + var_llti[var_rjut + 1]
                var_yjch = var_rdmc[var_rjut + 1]
                var_rdmc[var_rjut] = var_dmio(var_lsgw, var_yjch)
            var_llti = var_rdmc[:]
        return var_rdmc[0]
