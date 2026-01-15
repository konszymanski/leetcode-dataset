class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(var_rgwu.values())
        var_wnki.heapify(var_osiz)
        var_egyk = 0
        while var_osiz:
            var_egyk += var_wnki.heappop(var_osiz)
            if var_egyk > arg_rcsn:
                return var_dcmd(var_osiz) + 1
        return 0
