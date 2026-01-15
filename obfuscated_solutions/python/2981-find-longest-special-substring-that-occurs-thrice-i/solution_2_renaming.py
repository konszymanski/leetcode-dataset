class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo:
        var_bacg = {}
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            var_osiz = arg_xdvx[var_hqta]
            var_ayzf = 0
            for var_wnki in var_rgwu(var_hqta, var_wrnh(arg_xdvx)):
                if var_osiz == arg_xdvx[var_wnki]:
                    var_ayzf += 1
                    var_bacg[var_osiz, var_ayzf] = var_bacg.get((var_osiz,
                        var_ayzf), 0) + 1
                else:
                    break
        var_egyk = -1
        for var_dcmd in var_bacg.items():
            var_llti = var_dcmd[0][1]
            if var_dcmd[1] >= 3 and var_llti > var_egyk:
                var_egyk = var_llti
        return var_egyk
