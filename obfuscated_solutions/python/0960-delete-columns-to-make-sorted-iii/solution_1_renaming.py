class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn[0])
        var_rgwu = [1] * var_bacg
        for var_wrnh in var_osiz(var_bacg - 2, -1, -1):
            for var_ayzf in var_osiz(var_wrnh + 1, var_bacg):
                if var_wnki(var_egyk[var_wrnh] <= var_egyk[var_ayzf] for
                    var_egyk in arg_rcsn):
                    var_rgwu[var_wrnh] = var_dcmd(var_rgwu[var_wrnh], 1 +
                        var_rgwu[var_ayzf])
        return var_bacg - var_dcmd(var_rgwu)
