class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_bacg[var_hqta]:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [1] * var_wrnh
        var_wnki = [-1] * var_wrnh
        var_egyk, var_dcmd = 1, 0
        for var_llti in var_zbxo(1, var_wrnh):
            var_rdmc, var_rjut = 1, -1
            for var_lsgw in var_zbxo(var_llti - 1, -1, -1):
                if arg_rcsn[var_llti] != arg_rcsn[var_lsgw] and var_ayzf[
                    var_lsgw] + 1 > var_rdmc:
                    var_rdmc, var_rjut = var_ayzf[var_lsgw] + 1, var_lsgw
            var_ayzf[var_llti] = var_rdmc
            var_wnki[var_llti] = var_rjut
            if var_ayzf[var_llti] > var_egyk:
                var_egyk, var_dcmd = var_ayzf[var_llti], var_llti
        var_cbvh = []
        var_llti = var_dcmd
        while var_llti != -1:
            var_cbvh.append(arg_xdvx[var_llti])
            var_llti = var_wnki[var_llti]
        return var_cbvh[::-1]
