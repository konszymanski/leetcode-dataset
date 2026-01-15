class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        for var_bacg in var_hqta(var_rgwu(arg_xdvx)):
            var_wrnh = arg_xdvx[var_bacg]
            var_osiz = var_bacg + 1
            while var_osiz < var_rgwu(arg_xdvx) and arg_xdvx[var_osiz
                ] > arg_xdvx[var_osiz - 1]:
                var_wrnh += arg_xdvx[var_osiz]
                var_osiz += 1
            var_rcsn = var_ayzf(var_rcsn, var_wrnh)
        return var_rcsn
