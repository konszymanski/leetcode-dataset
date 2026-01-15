class Solution:
    var_udax = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = var_ayzf()
        for var_wnki in var_egyk(var_rgwu):
            for var_dcmd in var_egyk(var_rgwu):
                if arg_rcsn[var_wnki][var_dcmd] == 1:
                    var_osiz.append((var_wnki, var_dcmd))
                    arg_rcsn[var_wnki][var_dcmd] = 0
                else:
                    arg_rcsn[var_wnki][var_dcmd] = -1
        while var_osiz:
            var_llti = var_wrnh(var_osiz)
            while var_llti > 0:
                var_zbxo = var_osiz.popleft()
                for var_rdmc in arg_xdvx.dir:
                    var_rjut, var_lsgw = var_zbxo[0] + var_rdmc[0], var_zbxo[1
                        ] + var_rdmc[1]
                    var_cbvh = arg_rcsn[var_zbxo[0]][var_zbxo[1]]
                    if arg_xdvx.isValidCell(arg_rcsn, var_rjut, var_lsgw
                        ) and arg_rcsn[var_rjut][var_lsgw] == -1:
                        arg_rcsn[var_rjut][var_lsgw] = var_cbvh + 1
                        var_osiz.append((var_rjut, var_lsgw))
                var_llti -= 1
        var_yjch, var_dmio, var_ulfl = 0, 0, -1
        for var_wnki in var_egyk(var_rgwu):
            for var_dcmd in var_egyk(var_rgwu):
                var_dmio = var_lgvi(var_dmio, arg_rcsn[var_wnki][var_dcmd])
        while var_yjch <= var_dmio:
            var_wvuc = var_yjch + (var_dmio - var_yjch) // 2
            if arg_xdvx.isValidSafeness(arg_rcsn, var_wvuc):
                var_ulfl = var_wvuc
                var_yjch = var_wvuc + 1
            else:
                var_dmio = var_wvuc - 1
        return var_ulfl

    def func_tufr(arg_xdvx, arg_rcsn, var_wnki, var_dcmd) ->var_xhfo:
        var_rgwu = var_wrnh(arg_rcsn)
        return 0 <= var_wnki < var_rgwu and 0 <= var_dcmd < var_rgwu

    def func_miuw(arg_xdvx, arg_rcsn, arg_rhvk) ->var_xhfo:
        var_rgwu = var_wrnh(arg_rcsn)
        if arg_rcsn[0][0] < arg_rhvk or arg_rcsn[var_rgwu - 1][var_rgwu - 1
            ] < arg_rhvk:
            return False
        var_yybh = var_ayzf([(0, 0)])
        var_bzkm = [([False] * var_rgwu) for var_icgs in var_egyk(var_rgwu)]
        var_bzkm[0][0] = True
        while var_yybh:
            var_zbxo = var_yybh.popleft()
            if var_zbxo[0] == var_rgwu - 1 and var_zbxo[1] == var_rgwu - 1:
                return True
            for var_rdmc in arg_xdvx.dir:
                var_rjut, var_lsgw = var_zbxo[0] + var_rdmc[0], var_zbxo[1
                    ] + var_rdmc[1]
                if arg_xdvx.isValidCell(arg_rcsn, var_rjut, var_lsgw
                    ) and not var_bzkm[var_rjut][var_lsgw] and arg_rcsn[
                    var_rjut][var_lsgw] >= arg_rhvk:
                    var_bzkm[var_rjut][var_lsgw] = True
                    var_yybh.append((var_rjut, var_lsgw))
        return False
