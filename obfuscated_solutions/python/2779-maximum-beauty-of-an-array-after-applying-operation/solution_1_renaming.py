class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = 0
        for var_wrnh, var_osiz in var_ayzf(arg_xdvx):
            var_wnki = arg_ihhe._find_upper_bound(arg_xdvx, var_osiz + 2 *
                arg_rcsn)
            var_rgwu = var_egyk(var_rgwu, var_wnki - var_wrnh + 1)
        return var_rgwu

    def func_dcmd(arg_ihhe, arg_llti: var_bacg[var_hqta], arg_zbxo: var_hqta
        ) ->var_hqta:
        var_rdmc, var_rjut, var_lsgw = 0, var_cbvh(arg_llti) - 1, 0
        while var_rdmc <= var_rjut:
            var_yjch = var_rdmc + (var_rjut - var_rdmc) // 2
            if arg_llti[var_yjch] <= arg_zbxo:
                var_lsgw = var_yjch
                var_rdmc = var_yjch + 1
            else:
                var_rjut = var_yjch - 1
        return var_lsgw
