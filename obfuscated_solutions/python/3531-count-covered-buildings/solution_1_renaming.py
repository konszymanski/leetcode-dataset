class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [0] * (arg_xdvx + 1)
        var_wrnh = [arg_xdvx + 1] * (arg_xdvx + 1)
        var_osiz = [0] * (arg_xdvx + 1)
        var_ayzf = [arg_xdvx + 1] * (arg_xdvx + 1)
        for var_wnki in arg_rcsn:
            var_egyk, var_dcmd = var_wnki[0], var_wnki[1]
            var_rgwu[var_dcmd] = var_llti(var_rgwu[var_dcmd], var_egyk)
            var_wrnh[var_dcmd] = var_zbxo(var_wrnh[var_dcmd], var_egyk)
            var_osiz[var_egyk] = var_llti(var_osiz[var_egyk], var_dcmd)
            var_ayzf[var_egyk] = var_zbxo(var_ayzf[var_egyk], var_dcmd)
        var_rdmc = 0
        for var_wnki in arg_rcsn:
            var_egyk, var_dcmd = var_wnki[0], var_wnki[1]
            if var_egyk > var_wrnh[var_dcmd] and var_egyk < var_rgwu[var_dcmd
                ] and var_dcmd > var_ayzf[var_egyk] and var_dcmd < var_osiz[
                var_egyk]:
                var_rdmc += 1
        return var_rdmc
