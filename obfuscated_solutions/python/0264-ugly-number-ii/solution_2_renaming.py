import heapq


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = []
        var_hqta = var_rgwu()
        var_wrnh = [2, 3, 5]
        var_osiz.heappush(var_bacg, 1)
        var_hqta.add(1)
        var_ayzf = 1
        for var_wnki in var_egyk(arg_xdvx):
            var_ayzf = var_osiz.heappop(var_bacg)
            for var_dcmd in var_wrnh:
                var_llti = var_ayzf * var_dcmd
                if var_llti not in var_hqta:
                    var_osiz.heappush(var_bacg, var_llti)
                    var_hqta.add(var_llti)
        return var_ayzf
