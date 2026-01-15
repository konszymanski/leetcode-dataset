class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wvuc:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)
        var_osiz = [([var_ayzf] * (var_wrnh + 1)) for var_wnki in var_egyk(
            var_hqta)]

        def func_dcmd(arg_llti, arg_zbxo):
            var_rdmc = var_rjut(arg_llti - arg_zbxo)
            var_lsgw = var_hqta - var_rdmc
            return var_cbvh(var_rdmc, var_lsgw)
        for var_yjch in var_osiz:
            var_yjch[var_wrnh] = 0
        for var_dmio in var_egyk(var_wrnh - 1, -1, -1):
            for var_ulfl in var_egyk(var_hqta):
                for var_lgvi in var_egyk(var_hqta):
                    if arg_xdvx[var_lgvi] == arg_rcsn[var_dmio]:
                        var_osiz[var_ulfl][var_dmio] = var_cbvh(var_osiz[
                            var_ulfl][var_dmio], 1 + func_dcmd(var_ulfl,
                            var_lgvi) + var_osiz[var_lgvi][var_dmio + 1])
        return var_osiz[0][0]
