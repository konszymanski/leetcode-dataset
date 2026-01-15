class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = var_wrnh()
        for var_osiz in var_ayzf(3 ** arg_xdvx):
            var_wnki = var_egyk()
            var_dcmd = var_osiz
            for var_llti in var_ayzf(arg_xdvx):
                var_wnki.append(var_dcmd % 3)
                var_dcmd //= 3
            if var_zbxo(var_wnki[var_llti] == var_wnki[var_llti + 1] for
                var_llti in var_ayzf(arg_xdvx - 1)):
                continue
            var_rgwu[var_osiz] = var_wnki
        var_rdmc = var_rjut(var_egyk)
        for var_lsgw, var_cbvh in var_rgwu.items():
            for var_yjch, var_dmio in var_rgwu.items():
                if not var_zbxo(var_ulfl == var_lgvi for var_ulfl, var_lgvi in
                    var_wvuc(var_cbvh, var_dmio)):
                    var_rdmc[var_lsgw].append(var_yjch)
        var_tufr = [var_bacg(var_osiz in var_rgwu) for var_osiz in var_ayzf
            (3 ** arg_xdvx)]
        for var_llti in var_ayzf(1, arg_rcsn):
            var_xhfo = [0] * 3 ** arg_xdvx
            for var_yjch in var_rgwu.keys():
                for var_lsgw in var_rdmc[var_yjch]:
                    var_xhfo[var_yjch] += var_tufr[var_lsgw]
                    if var_xhfo[var_yjch] >= var_hqta:
                        var_xhfo[var_yjch] -= var_hqta
            var_tufr = var_xhfo
        return var_miuw(var_tufr) % var_hqta
