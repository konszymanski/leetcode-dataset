class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        if arg_rcsn == 1:
            return arg_xdvx
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [-1] * (var_bacg - arg_rcsn + 1)
        var_wrnh = 1
        for var_osiz in var_ayzf(var_bacg - 1):
            if arg_xdvx[var_osiz] + 1 == arg_xdvx[var_osiz + 1]:
                var_wrnh += 1
            else:
                var_wrnh = 1
            if var_wrnh >= arg_rcsn:
                var_rgwu[var_osiz - arg_rcsn + 2] = arg_xdvx[var_osiz + 1]
        return var_rgwu
