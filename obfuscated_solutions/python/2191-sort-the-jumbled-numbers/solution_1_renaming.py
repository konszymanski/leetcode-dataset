class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        for var_hqta in var_rgwu(var_wrnh(arg_rcsn)):
            var_osiz = var_ayzf(arg_rcsn[var_hqta])
            var_wnki = ''
            for var_egyk in var_rgwu(var_wrnh(var_osiz)):
                var_wnki = var_wnki + var_ayzf(arg_xdvx[var_dcmd(var_osiz[
                    var_egyk])])
            var_llti = var_dcmd(var_wnki)
            var_bacg.append((var_llti, var_hqta))
        var_bacg.sort()
        var_zbxo = []
        for var_rdmc in var_bacg:
            var_zbxo.append(arg_rcsn[var_rdmc[1]])
        return var_zbxo
