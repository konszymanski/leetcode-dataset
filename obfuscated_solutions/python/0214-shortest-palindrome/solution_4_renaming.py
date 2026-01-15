class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 29
        var_hqta = var_rgwu(1000000000.0 + 7)
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = 1
        var_wnki = -1
        for var_egyk, var_dcmd in var_llti(arg_xdvx):
            var_wrnh = (var_wrnh * var_bacg + (var_zbxo(var_dcmd) -
                var_zbxo('a') + 1)) % var_hqta
            var_osiz = (var_osiz + (var_zbxo(var_dcmd) - var_zbxo('a') + 1) *
                var_ayzf) % var_hqta
            var_ayzf = var_ayzf * var_bacg % var_hqta
            if var_wrnh == var_osiz:
                var_wnki = var_egyk
        var_rdmc = arg_xdvx[var_wnki + 1:]
        var_rjut = var_rdmc[::-1]
        return var_rjut + arg_xdvx
