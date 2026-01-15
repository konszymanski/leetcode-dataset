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
        var_yjch = [[-arg_rcsn[0][0], 0, 0]]
        arg_rcsn[0][0] = -1
        while var_yjch:
            var_dmio, var_wnki, var_dcmd = var_ulfl.heappop(var_yjch)
            if var_wnki == var_rgwu - 1 and var_dcmd == var_rgwu - 1:
                return -var_dmio
            for var_rdmc in arg_xdvx.dir:
                var_rjut, var_lsgw = var_wnki + var_rdmc[0
                    ], var_dcmd + var_rdmc[1]
                if arg_xdvx.isValidCell(arg_rcsn, var_rjut, var_lsgw
                    ) and arg_rcsn[var_rjut][var_lsgw] != -1:
                    var_ulfl.heappush(var_yjch, [-var_lgvi(-var_dmio,
                        arg_rcsn[var_rjut][var_lsgw]), var_rjut, var_lsgw])
                    arg_rcsn[var_rjut][var_lsgw] = -1
        return -1

    def func_wvuc(arg_xdvx, arg_rcsn, var_wnki, var_dcmd) ->var_tufr:
        var_rgwu = var_wrnh(arg_rcsn)
        return 0 <= var_wnki < var_rgwu and 0 <= var_dcmd < var_rgwu
