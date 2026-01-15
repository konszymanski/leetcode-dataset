class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_llti:
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            var_rgwu |= 1 << var_osiz(var_wrnh) - var_osiz('a')
        var_ayzf = 0
        for var_wnki in arg_rcsn:
            var_egyk = True
            for var_wrnh in var_wnki:
                var_dcmd = var_rgwu >> var_osiz(var_wrnh) - var_osiz('a') & 1
                if not var_dcmd:
                    var_egyk = False
                    break
            if var_egyk:
                var_ayzf += 1
        return var_ayzf
