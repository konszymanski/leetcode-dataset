class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])
        for var_ayzf in var_wnki(var_rgwu):
            for var_egyk in var_wnki(var_osiz):
                if arg_xdvx[var_ayzf][var_egyk] == 0:
                    continue
                var_dcmd = True
                for var_llti in var_wnki(var_rgwu):
                    if var_llti != var_ayzf and arg_xdvx[var_llti][var_egyk
                        ] == 1:
                        var_dcmd = False
                        break
                for var_zbxo in var_wnki(var_osiz):
                    if var_zbxo != var_egyk and arg_xdvx[var_ayzf][var_zbxo
                        ] == 1:
                        var_dcmd = False
                        break
                if var_dcmd:
                    var_hqta += 1
        return var_hqta
