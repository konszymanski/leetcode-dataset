class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn, var_bacg = 0, var_hqta(arg_xdvx) - 1
        var_rgwu = var_hqta(arg_xdvx)
        while var_rcsn <= var_bacg:
            var_wrnh = (var_rcsn + var_bacg) // 2
            if arg_xdvx[var_wrnh] < 0:
                var_rcsn = var_wrnh + 1
            else:
                var_bacg = var_wrnh - 1
                var_rgwu = var_wrnh
        return var_rgwu

    def func_osiz(arg_ihhe, arg_xdvx):
        var_rcsn, var_bacg = 0, var_hqta(arg_xdvx) - 1
        var_rgwu = var_hqta(arg_xdvx)
        while var_rcsn <= var_bacg:
            var_wrnh = (var_rcsn + var_bacg) // 2
            if arg_xdvx[var_wrnh] <= 0:
                var_rcsn = var_wrnh + 1
            else:
                var_bacg = var_wrnh - 1
                var_rgwu = var_wrnh
        return var_rgwu

    def func_ayzf(arg_ihhe, arg_xdvx):
        var_wnki = var_hqta(arg_xdvx) - arg_ihhe.upper_bound(arg_xdvx)
        var_egyk = arg_ihhe.lower_bound(arg_xdvx)
        return var_dcmd(var_wnki, var_egyk)
