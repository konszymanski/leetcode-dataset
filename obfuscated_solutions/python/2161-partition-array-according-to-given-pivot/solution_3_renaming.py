class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [0] * var_hqta(arg_xdvx)
        var_rgwu = 0
        var_wrnh = var_hqta(arg_xdvx) - 1
        for var_osiz, var_ayzf in var_wnki(var_egyk(var_hqta(arg_xdvx)),
            var_egyk(var_hqta(arg_xdvx) - 1, -1, -1)):
            if arg_xdvx[var_osiz] < arg_rcsn:
                var_bacg[var_rgwu] = arg_xdvx[var_osiz]
                var_rgwu += 1
            if arg_xdvx[var_ayzf] > arg_rcsn:
                var_bacg[var_wrnh] = arg_xdvx[var_ayzf]
                var_wrnh -= 1
        while var_rgwu <= var_wrnh:
            var_bacg[var_rgwu] = arg_rcsn
            var_rgwu += 1
        return var_bacg
