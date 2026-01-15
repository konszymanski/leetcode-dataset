class Solution:
    import heapq

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = []
        for var_wrnh in var_osiz(arg_rcsn):
            var_ayzf.heappush(var_rgwu, (arg_xdvx[var_wrnh], var_wrnh))
        var_wnki = 0
        var_egyk = 1000000000.0 + 7
        for var_wrnh in var_osiz(1, arg_hqta + 1):
            var_dcmd = var_ayzf.heappop(var_rgwu)
            if var_wrnh >= arg_bacg:
                var_wnki = (var_wnki + var_dcmd[0]) % var_egyk
            if var_dcmd[1] < arg_rcsn - 1:
                var_dcmd = var_dcmd[0] + arg_xdvx[var_dcmd[1] + 1], var_dcmd[1
                    ] + 1
                var_ayzf.heappush(var_rgwu, var_dcmd)
        return var_llti(var_wnki)
