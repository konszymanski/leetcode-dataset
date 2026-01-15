class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu, var_wrnh = 1, arg_xdvx % arg_bacg
        while arg_rcsn:
            if arg_rcsn & 1:
                var_rgwu = var_rgwu * var_wrnh % arg_bacg
            arg_rcsn >>= 1
            var_wrnh = var_wrnh * var_wrnh % arg_bacg
        return var_rgwu

    def func_osiz(arg_ihhe, arg_ayzf: var_hqta, arg_wnki: var_hqta,
        arg_egyk: var_dcmd[var_hqta]) ->var_hqta:
        var_llti = var_zbxo(arg_egyk)
        arg_bacg = 10 ** 9 + 7
        var_rdmc = [1] * (arg_ayzf + 1)
        for var_rjut in var_lsgw(1, arg_ayzf + 1):
            var_rdmc[var_rjut] = var_rdmc[var_rjut - 1] * var_rjut % arg_bacg
        var_cbvh = [1] * (arg_ayzf + 1)
        for var_rjut in var_lsgw(2, arg_ayzf + 1):
            var_cbvh[var_rjut] = arg_ihhe.quickmul(var_rjut, arg_bacg - 2,
                arg_bacg)
        for var_rjut in var_lsgw(2, arg_ayzf + 1):
            var_cbvh[var_rjut] = var_cbvh[var_rjut - 1] * var_cbvh[var_rjut
                ] % arg_bacg
        var_yjch = [([1] * (arg_ayzf + 1)) for var_dmio in var_lsgw(var_llti)]
        for var_rjut in var_lsgw(var_llti):
            for var_ulfl in var_lsgw(1, arg_ayzf + 1):
                var_yjch[var_rjut][var_ulfl] = var_yjch[var_rjut][var_ulfl - 1
                    ] * arg_egyk[var_rjut] % arg_bacg
        var_lgvi = [[[([0] * (arg_wnki + 1)) for var_dmio in var_lsgw(
            arg_ayzf * 2 + 1)] for var_dmio in var_lsgw(arg_ayzf + 1)] for
            var_dmio in var_lsgw(var_llti)]
        for var_ulfl in var_lsgw(arg_ayzf + 1):
            var_lgvi[0][var_ulfl][var_ulfl][0] = var_yjch[0][var_ulfl
                ] * var_cbvh[var_ulfl] % arg_bacg
        for var_rjut in var_lsgw(var_llti - 1):
            for var_ulfl in var_lsgw(arg_ayzf + 1):
                for var_wvuc in var_lsgw(arg_ayzf * 2 + 1):
                    for var_tufr in var_lsgw(arg_wnki + 1):
                        if var_lgvi[var_rjut][var_ulfl][var_wvuc][var_tufr
                            ] == 0:
                            continue
                        var_xhfo = var_wvuc % 2 + var_tufr
                        if var_xhfo > arg_wnki:
                            break
                        for var_miuw in var_lsgw(arg_ayzf - var_ulfl + 1):
                            var_rhvk = var_wvuc // 2 + var_miuw
                            if var_rhvk > arg_ayzf * 2:
                                continue
                            var_lgvi[var_rjut + 1][var_ulfl + var_miuw][
                                var_rhvk][var_xhfo] = (var_lgvi[var_rjut + 
                                1][var_ulfl + var_miuw][var_rhvk][var_xhfo] +
                                var_lgvi[var_rjut][var_ulfl][var_wvuc][
                                var_tufr] * var_yjch[var_rjut + 1][var_miuw
                                ] % arg_bacg * var_cbvh[var_miuw] % arg_bacg
                                ) % arg_bacg
        var_rgwu = 0
        for var_wvuc in var_lsgw(arg_ayzf * 2 + 1):
            for var_tufr in var_lsgw(arg_wnki + 1):
                if var_yybh(var_wvuc).count('1') + var_tufr == arg_wnki:
                    var_rgwu = (var_rgwu + var_lgvi[var_llti - 1][arg_ayzf]
                        [var_wvuc][var_tufr] * var_rdmc[arg_ayzf] % arg_bacg
                        ) % arg_bacg
        return var_rgwu
