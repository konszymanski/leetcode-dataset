class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        arg_xdvx.sort()
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = {}
        var_ayzf = []
        var_wnki = 0
        for var_egyk in var_rgwu:
            while var_wnki < var_dcmd(arg_xdvx) and arg_xdvx[var_wnki][0
                ] <= var_egyk:
                var_llti.heappush(var_ayzf, arg_xdvx[var_wnki][1])
                var_wnki += 1
            while var_ayzf and var_ayzf[0] < var_egyk:
                var_llti.heappop(var_ayzf)
            var_osiz[var_egyk] = var_dcmd(var_ayzf)
        return [var_osiz[var_zbxo] for var_zbxo in arg_rcsn]
