class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = []
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            for var_ayzf in arg_xdvx[var_rgwu]:
                var_hqta.append((var_ayzf, var_rgwu))
        var_hqta.sort()
        var_wnki = var_egyk(var_bacg)
        var_dcmd, var_llti = 0, 0
        var_zbxo, var_rdmc = 0, var_rjut('inf')
        for var_lsgw in var_wrnh(var_osiz(var_hqta)):
            var_wnki[var_hqta[var_lsgw][1]] += 1
            if var_wnki[var_hqta[var_lsgw][1]] == 1:
                var_llti += 1
            while var_llti == var_osiz(arg_xdvx):
                var_cbvh = var_hqta[var_lsgw][0] - var_hqta[var_dcmd][0]
                if var_cbvh < var_rdmc - var_zbxo:
                    var_zbxo = var_hqta[var_dcmd][0]
                    var_rdmc = var_hqta[var_lsgw][0]
                var_wnki[var_hqta[var_dcmd][1]] -= 1
                if var_wnki[var_hqta[var_dcmd][1]] == 0:
                    var_llti -= 1
                var_dcmd += 1
        return [var_zbxo, var_rdmc]
