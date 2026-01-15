class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_wvuc]:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = var_wrnh(arg_xdvx)
        var_ayzf = var_wnki()
        for var_egyk, var_dcmd in var_llti(arg_xdvx):
            var_ayzf[var_dcmd] = var_egyk
        var_zbxo = [0] * var_rgwu
        for var_egyk in var_rdmc(var_rgwu):
            for var_dcmd in arg_rcsn[var_egyk]:
                var_zbxo[var_egyk] |= 1 << var_ayzf[var_dcmd]
        var_rjut = [-1] * (1 << var_osiz)
        var_rjut[0] = 0

        def func_lsgw(arg_cbvh):
            if var_rjut[arg_cbvh] != -1:
                return var_rjut[arg_cbvh]
            for var_egyk in var_rdmc(var_rgwu):
                var_yjch = arg_cbvh & ~var_zbxo[var_egyk]
                if var_yjch != arg_cbvh:
                    var_dmio = func_lsgw(var_yjch) | 1 << var_egyk
                    if var_rjut[arg_cbvh] == -1 or var_dmio.bit_count(
                        ) < var_rjut[arg_cbvh].bit_count():
                        var_rjut[arg_cbvh] = var_dmio
            return var_rjut[arg_cbvh]
        var_ulfl = func_lsgw((1 << var_osiz) - 1)
        var_lgvi = []
        for var_egyk in var_rdmc(var_rgwu):
            if var_ulfl >> var_egyk & 1:
                var_lgvi.append(var_egyk)
        return var_lgvi
