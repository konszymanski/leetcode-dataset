class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 1
        var_wrnh = var_osiz(var_ayzf)
        for var_wnki in arg_xdvx:
            var_egyk = var_wnki % arg_rcsn
            var_wrnh[var_egyk][var_wnki] = var_wrnh[var_egyk].get(var_wnki, 0
                ) + 1
        for var_dcmd in var_wrnh.values():
            var_llti = var_zbxo(var_dcmd)
            var_rdmc = var_rjut(var_dcmd.items())
            var_lsgw = [0] * (var_llti + 1)
            var_lsgw[var_llti] = 1
            for var_cbvh in var_yjch(var_llti - 1, -1, -1):
                var_dmio = var_lsgw[var_cbvh + 1]
                var_ulfl = 2 ** var_rdmc[var_cbvh][1] - 1
                if var_cbvh + 1 < var_llti and var_rdmc[var_cbvh + 1][0
                    ] - var_rdmc[var_cbvh][0] == arg_rcsn:
                    var_ulfl *= var_lsgw[var_cbvh + 2]
                else:
                    var_ulfl *= var_lsgw[var_cbvh + 1]
                var_lsgw[var_cbvh] = var_dmio + var_ulfl
            var_rgwu *= var_lsgw[0]
        return var_rgwu - 1
