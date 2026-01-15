class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = (1 << var_wrnh - 1) * var_hqta
        for var_ayzf in var_wnki(1, var_wrnh):
            var_egyk = 0
            for var_dcmd in var_wnki(var_hqta):
                if arg_xdvx[var_dcmd][var_ayzf] == arg_xdvx[var_dcmd][0]:
                    var_egyk += 1
            var_egyk = var_llti(var_egyk, var_hqta - var_egyk)
            var_zbxo = (1 << var_wrnh - var_ayzf - 1) * var_egyk
            var_osiz += var_zbxo
        return var_osiz
