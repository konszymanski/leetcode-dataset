class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(var_wrnh)
        for var_osiz, var_ayzf in arg_xdvx:
            var_hqta[var_osiz].append(var_ayzf)
            var_hqta[var_ayzf].append(var_osiz)
        var_wnki = None
        for var_egyk in var_hqta:
            if var_dcmd(var_hqta[var_egyk]) == 1:
                var_wnki = var_egyk
                break
        var_llti = var_wnki
        var_zbxo = [var_wnki]
        var_rdmc = None
        while var_dcmd(var_zbxo) < var_dcmd(var_hqta):
            for var_rjut in var_hqta[var_llti]:
                if var_rjut != var_rdmc:
                    var_zbxo.append(var_rjut)
                    var_rdmc = var_llti
                    var_llti = var_rjut
                    break
        return var_zbxo
