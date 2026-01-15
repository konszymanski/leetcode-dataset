class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = {}
        var_rgwu = 2
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            for var_wnki in var_osiz(var_ayzf(arg_xdvx[0])):
                if arg_xdvx[var_wrnh][var_wnki] == 1:
                    var_hqta[var_rgwu] = arg_ihhe.explore_island(arg_xdvx,
                        var_rgwu, var_wrnh, var_wnki)
                    var_rgwu += 1
        if not var_hqta:
            return 1
        if var_ayzf(var_hqta) == 1:
            var_rgwu -= 1
            return var_hqta[var_rgwu] if var_hqta[var_rgwu] == var_ayzf(
                arg_xdvx) * var_ayzf(arg_xdvx[0]) else var_hqta[var_rgwu] + 1
        var_egyk = 1
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            for var_wnki in var_osiz(var_ayzf(arg_xdvx[0])):
                if arg_xdvx[var_wrnh][var_wnki] == 0:
                    var_dcmd = 1
                    var_llti = var_zbxo()
                    if var_wrnh + 1 < var_ayzf(arg_xdvx) and arg_xdvx[
                        var_wrnh + 1][var_wnki] > 1:
                        var_llti.add(arg_xdvx[var_wrnh + 1][var_wnki])
                    if var_wrnh - 1 >= 0 and arg_xdvx[var_wrnh - 1][var_wnki
                        ] > 1:
                        var_llti.add(arg_xdvx[var_wrnh - 1][var_wnki])
                    if var_wnki + 1 < var_ayzf(arg_xdvx[0]) and arg_xdvx[
                        var_wrnh][var_wnki + 1] > 1:
                        var_llti.add(arg_xdvx[var_wrnh][var_wnki + 1])
                    if var_wnki - 1 >= 0 and arg_xdvx[var_wrnh][var_wnki - 1
                        ] > 1:
                        var_llti.add(arg_xdvx[var_wrnh][var_wnki - 1])
                    for var_rgwu in var_llti:
                        var_dcmd += var_hqta[var_rgwu]
                    var_egyk = var_rdmc(var_egyk, var_dcmd)
        return var_egyk

    def func_rjut(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]],
        var_rgwu: var_bacg, var_wrnh: var_bacg, var_wnki: var_bacg) ->var_bacg:
        if var_wrnh < 0 or var_wrnh >= var_ayzf(arg_xdvx
            ) or var_wnki < 0 or var_wnki >= var_ayzf(arg_xdvx[0]) or arg_xdvx[
            var_wrnh][var_wnki] != 1:
            return 0
        arg_xdvx[var_wrnh][var_wnki] = var_rgwu
        return 1 + arg_ihhe.explore_island(arg_xdvx, var_rgwu, var_wrnh + 1,
            var_wnki) + arg_ihhe.explore_island(arg_xdvx, var_rgwu, 
            var_wrnh - 1, var_wnki) + arg_ihhe.explore_island(arg_xdvx,
            var_rgwu, var_wrnh, var_wnki + 1) + arg_ihhe.explore_island(
            arg_xdvx, var_rgwu, var_wrnh, var_wnki - 1)
