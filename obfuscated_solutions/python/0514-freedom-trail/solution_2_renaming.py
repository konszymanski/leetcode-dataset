class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wvuc:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)
        var_osiz = {}

        def func_ayzf(arg_wnki, arg_egyk):
            var_dcmd = var_llti(arg_wnki - arg_egyk)
            var_zbxo = var_hqta - var_dcmd
            return var_rdmc(var_dcmd, var_zbxo)

        def func_rjut(arg_lsgw, arg_cbvh):
            if (arg_lsgw, arg_cbvh) in var_osiz:
                return var_osiz[arg_lsgw, arg_cbvh]
            if arg_cbvh == var_wrnh:
                var_osiz[arg_lsgw, arg_cbvh] = 0
                return 0
            var_yjch = var_dmio
            for var_ulfl in var_lgvi(var_hqta):
                if arg_xdvx[var_ulfl] == arg_rcsn[arg_cbvh]:
                    var_yjch = var_rdmc(var_yjch, func_ayzf(arg_lsgw,
                        var_ulfl) + 1 + func_rjut(var_ulfl, arg_cbvh + 1))
            var_osiz[arg_lsgw, arg_cbvh] = var_yjch
            return var_yjch
        return func_rjut(0, 0)
