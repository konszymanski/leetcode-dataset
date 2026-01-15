class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_rgwu]) ->var_rgwu:
        var_wrnh = [(0, 0)]
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            var_wrnh.append((arg_rcsn[var_osiz], arg_xdvx[var_osiz]))
        var_wrnh.sort(reverse=True)
        for var_osiz in var_ayzf(var_wnki(var_wrnh) - 1):
            var_wrnh[var_osiz + 1] = var_wrnh[var_osiz + 1][0], var_egyk(
                var_wrnh[var_osiz][1], var_wrnh[var_osiz + 1][1])
        var_dcmd = 0
        for var_llti in arg_bacg:
            var_zbxo, var_rdmc = 0, var_wnki(var_wrnh) - 1
            var_rjut = 0
            while var_zbxo <= var_rdmc:
                var_lsgw = (var_zbxo + var_rdmc) // 2
                if var_wrnh[var_lsgw][1] <= var_llti:
                    var_rjut = var_cbvh(var_rjut, var_wrnh[var_lsgw][0])
                    var_rdmc = var_lsgw - 1
                else:
                    var_zbxo = var_lsgw + 1
            var_dcmd += var_rjut
        return var_dcmd
