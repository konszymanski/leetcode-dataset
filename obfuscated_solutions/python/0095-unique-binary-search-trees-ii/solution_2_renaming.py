class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_lsgw[var_osiz]:
        var_bacg = [[[] for var_hqta in var_rgwu(arg_xdvx + 1)] for
            var_hqta in var_rgwu(arg_xdvx + 1)]
        for var_wrnh in var_rgwu(1, arg_xdvx + 1):
            var_bacg[var_wrnh][var_wrnh] = [var_osiz(var_wrnh)]
        for var_ayzf in var_rgwu(2, arg_xdvx + 1):
            for var_wnki in var_rgwu(1, arg_xdvx - var_ayzf + 2):
                var_egyk = var_wnki + var_ayzf - 1
                for var_wrnh in var_rgwu(var_wnki, var_egyk + 1):
                    var_dcmd = var_bacg[var_wnki][var_wrnh - 1
                        ] if var_wrnh != var_wnki else [None]
                    var_llti = var_bacg[var_wrnh + 1][var_egyk
                        ] if var_wrnh != var_egyk else [None]
                    for var_zbxo in var_dcmd:
                        for var_rdmc in var_llti:
                            var_rjut = var_osiz(var_wrnh, var_zbxo, var_rdmc)
                            var_bacg[var_wnki][var_egyk].append(var_rjut)
        return var_bacg[1][arg_xdvx]
