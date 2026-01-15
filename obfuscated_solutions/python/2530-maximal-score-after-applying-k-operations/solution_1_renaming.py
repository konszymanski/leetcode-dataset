class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [(-var_wrnh) for var_wrnh in var_osiz(arg_xdvx, reverse=
            True)[:arg_rcsn]]
        var_ayzf = 0
        for var_wnki in var_egyk(arg_rcsn):
            var_dcmd = var_llti.heappop(var_rgwu)
            var_ayzf -= var_dcmd
            var_llti.heappush(var_rgwu, var_dcmd // 3)
        return var_ayzf
