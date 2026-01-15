import heapq


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = []
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_rgwu.append(arg_xdvx[var_wrnh] / arg_rcsn[var_wrnh])
        var_wnki.heapify(var_rgwu)
        var_egyk = 0
        while var_rgwu:
            if var_wnki.heappop(var_rgwu) <= var_egyk:
                break
            var_egyk += 1
        return var_egyk
