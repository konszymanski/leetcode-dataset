class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [0] * var_hqta(arg_rcsn)
        for var_rgwu, (var_wrnh, var_osiz) in var_ayzf(arg_rcsn):
            var_wnki = var_wrnh + var_osiz
            var_bacg[var_rgwu] += var_osiz
            for var_egyk in var_dcmd(var_rgwu + 1, var_hqta(arg_rcsn)):
                var_llti, var_zbxo = arg_rcsn[var_egyk]
                var_rdmc = var_llti + var_zbxo
                if var_llti < var_wnki and var_wrnh < var_rdmc:
                    var_bacg[var_egyk] = var_rjut(var_bacg[var_egyk],
                        var_bacg[var_rgwu])
        var_lsgw = []
        for var_cbvh in var_bacg:
            var_lsgw.append(var_rjut(var_lsgw[-1], var_cbvh) if var_lsgw else
                var_cbvh)
        return var_lsgw
