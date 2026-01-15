class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_wrnh]) ->var_wrnh:
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = [(0) for var_egyk in var_dcmd(26)]
        for var_llti in arg_rcsn:
            var_wnki[var_zbxo(var_llti) - 97] += 1

        def func_rdmc(arg_rjut, arg_bacg, var_wnki):
            var_lsgw = 0
            for var_llti in var_dcmd(26):
                var_lsgw += arg_rjut[var_llti] * arg_bacg[var_llti]
                if arg_rjut[var_llti] > var_wnki[var_llti]:
                    return 0
            return var_lsgw
        var_cbvh = 0
        arg_rjut = {}
        for var_yjch in var_dcmd(1 << var_osiz):
            arg_rjut = [(0) for var_egyk in var_dcmd(26)]
            for var_egyk in var_dcmd(var_osiz):
                if var_yjch & 1 << var_egyk > 0:
                    var_dmio = var_ayzf(arg_xdvx[var_egyk])
                    for var_ulfl in var_dcmd(var_dmio):
                        arg_rjut[var_zbxo(arg_xdvx[var_egyk][var_ulfl]) - 97
                            ] += 1
            var_cbvh = var_lgvi(var_cbvh, func_rdmc(arg_rjut, arg_bacg,
                var_wnki))
        return var_cbvh
