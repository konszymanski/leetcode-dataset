class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn, var_bacg = var_hqta(arg_xdvx), var_hqta(arg_xdvx[0])
        var_rgwu = [([0] * var_bacg) for var_wrnh in var_osiz(var_rcsn)]
        for var_ayzf in var_osiz(var_rcsn):
            var_rgwu[var_ayzf][0] = 1
        var_wnki = 0
        for var_egyk in var_osiz(1, var_bacg):
            for var_ayzf in var_osiz(var_rcsn):
                if arg_xdvx[var_ayzf][var_egyk] > arg_xdvx[var_ayzf][
                    var_egyk - 1] and var_rgwu[var_ayzf][var_egyk - 1] > 0:
                    var_rgwu[var_ayzf][var_egyk] = var_dcmd(var_rgwu[
                        var_ayzf][var_egyk], var_rgwu[var_ayzf][var_egyk - 
                        1] + 1)
                if var_ayzf - 1 >= 0 and arg_xdvx[var_ayzf][var_egyk
                    ] > arg_xdvx[var_ayzf - 1][var_egyk - 1] and var_rgwu[
                    var_ayzf - 1][var_egyk - 1] > 0:
                    var_rgwu[var_ayzf][var_egyk] = var_dcmd(var_rgwu[
                        var_ayzf][var_egyk], var_rgwu[var_ayzf - 1][
                        var_egyk - 1] + 1)
                if var_ayzf + 1 < var_rcsn and arg_xdvx[var_ayzf][var_egyk
                    ] > arg_xdvx[var_ayzf + 1][var_egyk - 1] and var_rgwu[
                    var_ayzf + 1][var_egyk - 1] > 0:
                    var_rgwu[var_ayzf][var_egyk] = var_dcmd(var_rgwu[
                        var_ayzf][var_egyk], var_rgwu[var_ayzf + 1][
                        var_egyk - 1] + 1)
                var_wnki = var_dcmd(var_wnki, var_rgwu[var_ayzf][var_egyk] - 1)
        return var_wnki
