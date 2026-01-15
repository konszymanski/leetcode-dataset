class Solution:
    var_udax = 0
    var_ihhe = 1
    var_xdvx = 2
    var_rcsn = 3

    def func_bacg(arg_hqta, arg_rgwu: var_wnki, arg_wrnh: var_wnki,
        arg_osiz: var_egyk[var_egyk[var_wnki]], arg_ayzf: var_egyk[var_egyk
        [var_wnki]]) ->var_wnki:
        var_dcmd = [([arg_hqta.UNGUARDED] * arg_wrnh) for var_llti in
            var_zbxo(arg_rgwu)]
        for var_rdmc, var_rjut in arg_osiz:
            var_dcmd[var_rdmc][var_rjut] = arg_hqta.GUARD
        for var_rdmc, var_rjut in arg_ayzf:
            var_dcmd[var_rdmc][var_rjut] = arg_hqta.WALL

        def func_lsgw(var_rdmc, var_rjut, arg_cbvh):
            if var_dcmd[var_rdmc][var_rjut] == arg_hqta.GUARD:
                return True
            if var_dcmd[var_rdmc][var_rjut] == arg_hqta.WALL:
                return False
            if arg_cbvh:
                var_dcmd[var_rdmc][var_rjut] = arg_hqta.GUARDED
            return arg_cbvh
        for var_rdmc in var_zbxo(arg_rgwu):
            arg_cbvh = var_dcmd[var_rdmc][0] == arg_hqta.GUARD
            for var_rjut in var_zbxo(1, arg_wrnh):
                arg_cbvh = func_lsgw(var_rdmc, var_rjut, arg_cbvh)
            arg_cbvh = var_dcmd[var_rdmc][arg_wrnh - 1] == arg_hqta.GUARD
            for var_rjut in var_zbxo(arg_wrnh - 2, -1, -1):
                arg_cbvh = func_lsgw(var_rdmc, var_rjut, arg_cbvh)
        for var_rjut in var_zbxo(arg_wrnh):
            arg_cbvh = var_dcmd[0][var_rjut] == arg_hqta.GUARD
            for var_rdmc in var_zbxo(1, arg_rgwu):
                arg_cbvh = func_lsgw(var_rdmc, var_rjut, arg_cbvh)
            arg_cbvh = var_dcmd[arg_rgwu - 1][var_rjut] == arg_hqta.GUARD
            for var_rdmc in var_zbxo(arg_rgwu - 2, -1, -1):
                arg_cbvh = func_lsgw(var_rdmc, var_rjut, arg_cbvh)
        var_yjch = 0
        for var_rdmc in var_zbxo(arg_rgwu):
            for var_rjut in var_zbxo(arg_wrnh):
                if var_dcmd[var_rdmc][var_rjut] == arg_hqta.UNGUARDED:
                    var_yjch += 1
        return var_yjch
