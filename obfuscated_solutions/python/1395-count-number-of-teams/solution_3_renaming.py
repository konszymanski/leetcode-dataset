class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            var_wnki = 0
            var_egyk = 0
            for var_dcmd in var_ayzf(var_osiz - 1, -1, -1):
                if arg_xdvx[var_dcmd] < arg_xdvx[var_osiz]:
                    var_wnki += 1
            for var_llti in var_ayzf(var_osiz + 1, var_hqta):
                if arg_xdvx[var_llti] > arg_xdvx[var_osiz]:
                    var_egyk += 1
            var_wrnh += var_wnki * var_egyk
            var_zbxo = var_osiz - var_wnki
            var_rdmc = var_hqta - var_osiz - 1 - var_egyk
            var_wrnh += var_zbxo * var_rdmc
        return var_wrnh
