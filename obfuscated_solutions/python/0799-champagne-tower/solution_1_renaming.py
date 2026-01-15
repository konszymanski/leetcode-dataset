class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = [([0] * var_wrnh) for var_wrnh in var_osiz(1, 102)]
        var_rgwu[0][0] = arg_rcsn
        for var_ayzf in var_osiz(arg_bacg + 1):
            for var_wnki in var_osiz(var_ayzf + 1):
                var_egyk = (var_rgwu[var_ayzf][var_wnki] - 1.0) / 2.0
                if var_egyk > 0:
                    var_rgwu[var_ayzf + 1][var_wnki] += var_egyk
                    var_rgwu[var_ayzf + 1][var_wnki + 1] += var_egyk
        return var_dcmd(1, var_rgwu[arg_bacg][arg_hqta])
