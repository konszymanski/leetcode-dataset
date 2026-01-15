import heapq


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [(-arg_xdvx[0], 0)]
        var_wrnh = arg_xdvx[0]
        for var_osiz in var_ayzf(1, var_wnki(arg_xdvx)):
            while var_osiz - var_rgwu[0][1] > arg_rcsn:
                var_egyk.heappop(var_rgwu)
            var_dcmd = var_llti(0, -var_rgwu[0][0]) + arg_xdvx[var_osiz]
            var_wrnh = var_llti(var_wrnh, var_dcmd)
            var_egyk.heappush(var_rgwu, (-var_dcmd, var_osiz))
        return var_wrnh
