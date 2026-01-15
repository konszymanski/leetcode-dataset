class Solution:
    var_udax = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_rcsn), var_osiz(arg_rcsn[0])
        var_ayzf = [([var_wnki('inf')] * var_wrnh) for var_egyk in var_dcmd
            (var_rgwu)]
        var_ayzf[0][0] = 0
        var_llti = var_zbxo.deque([(0, 0)])
        while var_llti:
            var_rdmc, var_rjut = var_llti.popleft()
            for var_lsgw, (var_cbvh, var_yjch) in var_dmio(arg_xdvx._dirs):
                var_ulfl, var_lgvi = var_rdmc + var_cbvh, var_rjut + var_yjch
                var_wvuc = 0 if arg_rcsn[var_rdmc][var_rjut
                    ] == var_lsgw + 1 else 1
                if arg_xdvx._is_valid(var_ulfl, var_lgvi, var_rgwu, var_wrnh
                    ) and var_ayzf[var_rdmc][var_rjut] + var_wvuc < var_ayzf[
                    var_ulfl][var_lgvi]:
                    var_ayzf[var_ulfl][var_lgvi] = var_ayzf[var_rdmc][var_rjut
                        ] + var_wvuc
                    if var_wvuc == 1:
                        var_llti.append((var_ulfl, var_lgvi))
                    else:
                        var_llti.appendleft((var_ulfl, var_lgvi))
        return var_ayzf[var_rgwu - 1][var_wrnh - 1]

    def func_tufr(arg_xdvx, var_rdmc: var_hqta, var_rjut: var_hqta,
        var_rgwu: var_hqta, var_wrnh: var_hqta) ->var_xhfo:
        return 0 <= var_rdmc < var_rgwu and 0 <= var_rjut < var_wrnh
