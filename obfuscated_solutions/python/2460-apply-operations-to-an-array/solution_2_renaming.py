class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        for var_hqta in var_rgwu(var_rcsn - 1):
            if arg_xdvx[var_hqta] == arg_xdvx[var_hqta + 1] and arg_xdvx[
                var_hqta] != 0:
                arg_xdvx[var_hqta] *= 2
                arg_xdvx[var_hqta + 1] = 0
        var_wrnh = 0
        for var_osiz in var_rgwu(var_rcsn):
            if arg_xdvx[var_osiz] != 0:
                arg_xdvx[var_wrnh] = arg_xdvx[var_osiz]
                var_wrnh += 1
        while var_wrnh < var_rcsn:
            arg_xdvx[var_wrnh] = 0
            var_wrnh += 1
        return arg_xdvx
