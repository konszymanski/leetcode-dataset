class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_lgvi:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)
        var_osiz = [var_ayzf for var_wnki in var_egyk(var_hqta)]
        var_dcmd = [(0) for var_wnki in var_egyk(var_hqta)]

        def func_llti(var_osiz, arg_zbxo):
            var_rdmc = var_rjut(var_osiz - arg_zbxo)
            var_lsgw = var_hqta - var_rdmc
            return var_cbvh(var_rdmc, var_lsgw)
        for var_yjch in var_egyk(var_wrnh - 1, -1, -1):
            var_osiz = [var_ayzf for var_wnki in var_egyk(var_hqta)]
            for var_dmio in var_egyk(var_hqta):
                for var_ulfl in var_egyk(var_hqta):
                    if arg_xdvx[var_ulfl] == arg_rcsn[var_yjch]:
                        var_osiz[var_dmio] = var_cbvh(var_osiz[var_dmio], 1 +
                            func_llti(var_dmio, var_ulfl) + var_dcmd[var_ulfl])
            var_dcmd = var_osiz.copy()
        return var_dcmd[0]
