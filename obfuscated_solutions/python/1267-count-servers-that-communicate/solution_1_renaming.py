class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0]) if var_hqta > 0 else 0
        var_osiz = 0
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_wrnh):
                if arg_xdvx[var_ayzf][var_egyk] == 1:
                    var_dcmd = False
                    for var_llti in var_wnki(var_wrnh):
                        if var_llti != var_egyk and arg_xdvx[var_ayzf][var_llti
                            ] == 1:
                            var_dcmd = True
                            break
                    if var_dcmd:
                        var_osiz += 1
                    else:
                        for var_zbxo in var_wnki(var_hqta):
                            if var_zbxo != var_ayzf and arg_xdvx[var_zbxo][
                                var_egyk] == 1:
                                var_dcmd = True
                                break
                        if var_dcmd:
                            var_osiz += 1
        return var_osiz
