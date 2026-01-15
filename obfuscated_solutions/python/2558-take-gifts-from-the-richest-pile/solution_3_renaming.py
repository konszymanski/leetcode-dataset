class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [(-var_hqta) for var_hqta in arg_xdvx]
        var_rgwu.heapify(var_bacg)
        for var_wrnh in var_osiz(arg_rcsn):
            var_ayzf = -var_rgwu.heappop(var_bacg)
            var_rgwu.heappush(var_bacg, -var_wnki.floor(var_wnki.sqrt(
                var_ayzf)))
        var_egyk = 0
        while var_bacg:
            var_egyk -= var_rgwu.heappop(var_bacg)
        return var_egyk
