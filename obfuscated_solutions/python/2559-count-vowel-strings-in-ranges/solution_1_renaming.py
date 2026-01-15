class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_rgwu]]) ->var_bacg[var_rgwu]:
        var_wrnh = [0] * var_osiz(arg_rcsn)
        var_ayzf = {'a', 'e', 'i', 'o', 'u'}
        var_wnki = [0] * var_osiz(arg_xdvx)
        var_egyk = 0
        for var_dcmd in var_llti(var_osiz(arg_xdvx)):
            var_zbxo = arg_xdvx[var_dcmd]
            if var_zbxo[0] in var_ayzf and var_zbxo[var_osiz(var_zbxo) - 1
                ] in var_ayzf:
                var_egyk += 1
            var_wnki[var_dcmd] = var_egyk
        for var_dcmd in var_llti(var_osiz(arg_rcsn)):
            var_rdmc = arg_rcsn[var_dcmd]
            var_wrnh[var_dcmd] = var_wnki[var_rdmc[1]] - (0 if var_rdmc[0] ==
                0 else var_wnki[var_rdmc[0] - 1])
        return var_wrnh
