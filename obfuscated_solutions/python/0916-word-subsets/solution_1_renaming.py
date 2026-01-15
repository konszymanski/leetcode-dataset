class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:

        def func_rgwu(arg_wrnh):
            var_osiz = [0] * 26
            for var_ayzf in arg_wrnh:
                var_osiz[var_wnki(var_ayzf) - var_wnki('a')] += 1
            return var_osiz
        var_egyk = [0] * 26
        for var_dcmd in arg_rcsn:
            for var_llti, var_zbxo in var_rdmc(func_rgwu(var_dcmd)):
                var_egyk[var_llti] = var_rjut(var_egyk[var_llti], var_zbxo)
        var_osiz = []
        for var_lsgw in arg_xdvx:
            if var_cbvh(var_yjch >= var_dmio for var_yjch, var_dmio in
                var_ulfl(func_rgwu(var_lsgw), var_egyk)):
                var_osiz.append(var_lsgw)
        return var_osiz
