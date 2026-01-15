class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [0] * var_bacg
        var_wrnh = 0
        for var_osiz in var_ayzf(var_bacg - 1, -1, -1):
            var_rgwu[var_osiz] = var_wrnh
            if arg_xdvx[var_osiz] == 'a':
                var_wrnh += 1
        var_wnki = var_bacg
        var_egyk = 0
        for var_osiz in var_ayzf(var_bacg):
            var_wnki = var_dcmd(var_rgwu[var_osiz] + var_egyk, var_wnki)
            if arg_xdvx[var_osiz] == 'b':
                var_egyk += 1
        return var_wnki
