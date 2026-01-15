class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = 0
        var_wnki = 0
        var_egyk = 0
        for var_dcmd in var_llti(var_wrnh):
            var_egyk += var_zbxo(var_rdmc(arg_xdvx[var_dcmd]) - var_rdmc(
                arg_rcsn[var_dcmd]))
            while var_egyk > arg_bacg:
                var_egyk -= var_zbxo(var_rdmc(arg_xdvx[var_wnki]) -
                    var_rdmc(arg_rcsn[var_wnki]))
                var_wnki += 1
            var_ayzf = var_rjut(var_ayzf, var_dcmd - var_wnki + 1)
        return var_ayzf
