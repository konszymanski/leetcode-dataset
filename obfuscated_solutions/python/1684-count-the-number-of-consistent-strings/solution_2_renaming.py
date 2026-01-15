class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_dcmd:
        var_rgwu = [False] * 26
        for var_wrnh in arg_xdvx:
            var_rgwu[var_osiz(var_wrnh) - var_osiz('a')] = True
        var_ayzf = 0
        for var_wnki in arg_rcsn:
            var_egyk = True
            for var_wrnh in var_wnki:
                if not var_rgwu[var_osiz(var_wrnh) - var_osiz('a')]:
                    var_egyk = False
                    break
            if var_egyk:
                var_ayzf += 1
        return var_ayzf
