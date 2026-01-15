class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [(-var_wrnh) for var_wrnh in var_bacg.values()]
        var_osiz.heapify(var_rgwu)
        var_ayzf = 0
        var_wnki = 0
        while var_rgwu:
            var_ayzf += (1 + var_wnki // 8) * -var_osiz.heappop(var_rgwu)
            var_wnki += 1
        return var_ayzf
