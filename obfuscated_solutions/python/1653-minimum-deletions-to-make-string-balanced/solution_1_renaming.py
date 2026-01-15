class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [0] * var_bacg
        var_wrnh = [0] * var_bacg
        var_osiz = 0
        for var_ayzf in var_wnki(var_bacg):
            var_wrnh[var_ayzf] = var_osiz
            if arg_xdvx[var_ayzf] == 'b':
                var_osiz += 1
        var_egyk = 0
        for var_ayzf in var_wnki(var_bacg - 1, -1, -1):
            var_rgwu[var_ayzf] = var_egyk
            if arg_xdvx[var_ayzf] == 'a':
                var_egyk += 1
        var_dcmd = var_bacg
        for var_ayzf in var_wnki(var_bacg):
            var_dcmd = var_llti(var_dcmd, var_rgwu[var_ayzf] + var_wrnh[
                var_ayzf])
        return var_dcmd
