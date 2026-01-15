class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu.heapify(arg_xdvx)
        var_wrnh = 0
        while arg_xdvx[0] < arg_rcsn:
            var_osiz = var_rgwu.heappop(arg_xdvx)
            var_ayzf = var_rgwu.heappop(arg_xdvx)
            var_rgwu.heappush(arg_xdvx, var_wnki(var_osiz, var_ayzf) * 2 +
                var_egyk(var_osiz, var_ayzf))
            var_wrnh += 1
        return var_wrnh
