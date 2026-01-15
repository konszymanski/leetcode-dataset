class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        arg_xdvx -= 1
        var_rgwu = [0] * 64
        var_wrnh = [0] * 64
        for var_osiz in var_ayzf(64):
            var_wnki = arg_rcsn >> var_osiz & 1
            var_rgwu[var_osiz] = var_wnki
            var_wnki = arg_xdvx >> var_osiz & 1
            var_wrnh[var_osiz] = var_wnki
        var_egyk = 0
        var_dcmd = 0
        while var_egyk < 63:
            while var_rgwu[var_egyk] != 0 and var_egyk < 63:
                var_egyk += 1
            var_rgwu[var_egyk] = var_wrnh[var_dcmd]
            var_egyk += 1
            var_dcmd += 1
        for var_osiz in var_ayzf(64):
            if var_rgwu[var_osiz] == 1:
                var_hqta += var_llti(2, var_osiz)
        return var_hqta
