class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        if arg_rcsn == 0:
            return 0
        var_rgwu = var_wrnh.log(arg_rcsn)
        var_osiz = [0]
        for var_ayzf in arg_xdvx:
            var_osiz.append(var_osiz[-1] + var_wrnh.log(var_ayzf))
        var_wnki = 0
        for var_egyk in var_dcmd(var_llti(var_osiz)):
            var_zbxo, var_rdmc = var_egyk + 1, var_llti(var_osiz)
            while var_zbxo < var_rdmc:
                var_rjut = (var_zbxo + var_rdmc) // 2
                if var_osiz[var_rjut] < var_osiz[var_egyk] + var_rgwu - 1e-09:
                    var_zbxo = var_rjut + 1
                else:
                    var_rdmc = var_rjut
            var_wnki += var_zbxo - var_egyk - 1
        return var_wnki
