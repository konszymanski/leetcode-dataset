class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        for var_bacg in var_hqta(24):
            var_rgwu = 0
            for var_wrnh in arg_xdvx:
                if var_wrnh & 1 << var_bacg != 0:
                    var_rgwu += 1
            var_rcsn = var_osiz(var_rcsn, var_rgwu)
        return var_rcsn
