class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        arg_xdvx.sort()
        arg_rcsn.sort(key=lambda x: var_rgwu[0])
        var_wrnh = []
        for var_osiz in arg_rcsn:
            var_wrnh.extend([var_osiz[0]] * var_osiz[1])
        var_ayzf = var_wnki(arg_xdvx)
        var_egyk = var_wnki(var_wrnh)
        var_dcmd = [([None] * (var_egyk + 1)) for var_llti in var_zbxo(
            var_ayzf + 1)]

        def func_rdmc(arg_rjut: var_hqta, arg_lsgw: var_hqta) ->var_hqta:
            if var_dcmd[arg_rjut][arg_lsgw] is not None:
                return var_dcmd[arg_rjut][arg_lsgw]
            if arg_rjut == var_ayzf:
                var_dcmd[arg_rjut][arg_lsgw] = 0
                return 0
            if arg_lsgw == var_egyk:
                var_dcmd[arg_rjut][arg_lsgw] = var_hqta(1000000000000.0)
                return var_hqta(1000000000000.0)
            var_cbvh = var_yjch(arg_xdvx[arg_rjut] - var_wrnh[arg_lsgw]
                ) + func_rdmc(arg_rjut + 1, arg_lsgw + 1)
            var_dmio = func_rdmc(arg_rjut, arg_lsgw + 1)
            var_dcmd[arg_rjut][arg_lsgw] = var_ulfl(var_cbvh, var_dmio)
            return var_dcmd[arg_rjut][arg_lsgw]
        return func_rdmc(0, 0)
