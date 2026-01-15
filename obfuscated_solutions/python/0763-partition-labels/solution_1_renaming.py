class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti[var_zbxo]:
        var_bacg = [0] * 26
        for var_hqta, var_rgwu in var_wrnh(arg_xdvx):
            var_bacg[var_osiz(var_rgwu) - var_osiz('a')] = var_hqta
        var_ayzf = 0
        var_wnki = 0
        var_egyk = []
        for var_hqta, var_rgwu in var_wrnh(arg_xdvx):
            var_ayzf = var_dcmd(var_ayzf, var_bacg[var_osiz(var_rgwu) -
                var_osiz('a')])
            if var_hqta == var_ayzf:
                var_egyk.append(var_hqta - var_wnki + 1)
                var_wnki = var_hqta + 1
        return var_egyk
