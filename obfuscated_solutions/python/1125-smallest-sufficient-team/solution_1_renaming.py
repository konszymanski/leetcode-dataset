class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_lgvi]:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = var_wrnh(arg_xdvx)
        var_ayzf = var_wnki()
        for var_egyk, var_dcmd in var_llti(arg_xdvx):
            var_ayzf[var_dcmd] = var_egyk
        var_zbxo = [0] * var_rgwu
        for var_egyk in var_rdmc(var_rgwu):
            for var_dcmd in arg_rcsn[var_egyk]:
                var_zbxo[var_egyk] |= 1 << var_ayzf[var_dcmd]
        var_rjut = [(1 << var_rgwu) - 1] * (1 << var_osiz)
        var_rjut[0] = 0
        for var_lsgw in var_rdmc(1, 1 << var_osiz):
            for var_egyk in var_rdmc(var_rgwu):
                var_cbvh = var_lsgw & ~var_zbxo[var_egyk]
                if var_cbvh != var_lsgw:
                    var_yjch = var_rjut[var_cbvh] | 1 << var_egyk
                    if var_yjch.bit_count() < var_rjut[var_lsgw].bit_count():
                        var_rjut[var_lsgw] = var_yjch
        var_dmio = var_rjut[(1 << var_osiz) - 1]
        var_ulfl = []
        for var_egyk in var_rdmc(var_rgwu):
            if var_dmio >> var_egyk & 1:
                var_ulfl.append(var_egyk)
        return var_ulfl
