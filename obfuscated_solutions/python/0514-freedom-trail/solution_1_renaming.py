class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_wvuc:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)

        def func_osiz(arg_ayzf, arg_wnki):
            var_egyk = var_dcmd(arg_ayzf - arg_wnki)
            var_llti = var_hqta - var_egyk
            return var_zbxo(var_egyk, var_llti)

        def func_rdmc(arg_rjut, arg_lsgw, arg_cbvh):
            if arg_lsgw == var_rgwu(arg_rcsn):
                return 0
            for var_yjch in var_dmio(var_rgwu(arg_xdvx)):
                if arg_xdvx[var_yjch] == arg_rcsn[arg_lsgw]:
                    var_ulfl = func_osiz(arg_rjut, var_yjch) + 1 + func_rdmc(
                        var_yjch, arg_lsgw + 1, var_lgvi)
                    arg_cbvh = var_zbxo(arg_cbvh, var_ulfl)
            return arg_cbvh
        return func_rdmc(0, 0, var_lgvi)
