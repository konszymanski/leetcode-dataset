class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = [True] * (arg_xdvx + 1)
        var_rcsn[0] = var_rcsn[1] = False
        for var_bacg in var_hqta(2, var_rgwu(arg_xdvx ** 0.5) + 1):
            if var_rcsn[var_bacg]:
                for var_wrnh in var_hqta(var_bacg * var_bacg, arg_xdvx + 1,
                    var_bacg):
                    var_rcsn[var_wrnh] = False
        return var_rcsn

    def func_osiz(arg_ihhe, arg_ayzf, arg_wnki):
        var_egyk = arg_ihhe._sieve(arg_wnki)
        var_dcmd = [var_llti for var_llti in var_hqta(arg_ayzf, arg_wnki + 
            1) if var_egyk[var_llti]]
        if var_zbxo(var_dcmd) < 2:
            return -1, -1
        var_rdmc = var_rjut('inf')
        var_lsgw = -1, -1
        for var_cbvh in var_hqta(1, var_zbxo(var_dcmd)):
            var_yjch = var_dcmd[var_cbvh] - var_dcmd[var_cbvh - 1]
            if var_yjch < var_rdmc:
                var_rdmc = var_yjch
                var_lsgw = var_dcmd[var_cbvh - 1], var_dcmd[var_cbvh]
        return var_lsgw
