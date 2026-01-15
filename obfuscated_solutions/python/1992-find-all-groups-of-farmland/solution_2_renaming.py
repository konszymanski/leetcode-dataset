class Solution:
    var_udax = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn: var_wrnh, arg_bacg: var_wrnh,
        arg_hqta: var_wrnh, arg_rgwu: var_wrnh) ->var_osiz:
        return 0 <= arg_rcsn < arg_hqta and 0 <= arg_bacg < arg_rgwu

    def func_ayzf(arg_xdvx, arg_wnki: var_llti, arg_egyk: var_zbxo[var_zbxo
        [var_wrnh]], arg_dcmd: var_zbxo[var_zbxo[var_osiz]]) ->var_dmio:
        var_rdmc = 0, 0
        while arg_wnki:
            var_rdmc = arg_wnki.popleft()
            arg_rcsn, arg_bacg = var_rdmc
            for var_rjut in arg_xdvx.dirs:
                var_lsgw, var_cbvh = arg_rcsn + var_rjut[0
                    ], arg_bacg + var_rjut[1]
                if arg_xdvx.is_within_farm(var_lsgw, var_cbvh, var_yjch(
                    arg_egyk), var_yjch(arg_egyk[0])) and not arg_dcmd[var_lsgw
                    ][var_cbvh] and arg_egyk[var_lsgw][var_cbvh] == 1:
                    arg_dcmd[var_lsgw][var_cbvh] = True
                    arg_wnki.append((var_lsgw, var_cbvh))
        return var_rdmc

    def func_ulfl(arg_xdvx, arg_egyk: var_zbxo[var_zbxo[var_wrnh]]) ->var_zbxo[
        var_zbxo[var_wrnh]]:
        arg_dcmd = [([False] * var_yjch(arg_egyk[0])) for var_lgvi in
            var_wvuc(var_yjch(arg_egyk))]
        var_tufr = []
        for var_xhfo in var_wvuc(var_yjch(arg_egyk)):
            for var_miuw in var_wvuc(var_yjch(arg_egyk[0])):
                if arg_egyk[var_xhfo][var_miuw] == 1 and not arg_dcmd[var_xhfo
                    ][var_miuw]:
                    arg_wnki = var_llti([(var_xhfo, var_miuw)])
                    arg_dcmd[var_xhfo][var_miuw] = True
                    var_rhvk = arg_xdvx.bfs(arg_wnki, arg_egyk, arg_dcmd)
                    var_tufr.append([var_xhfo, var_miuw, var_rhvk[0],
                        var_rhvk[1]])
        return var_tufr
