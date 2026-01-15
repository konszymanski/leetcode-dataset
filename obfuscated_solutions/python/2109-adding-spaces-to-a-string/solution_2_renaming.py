class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_rgwu]
        ) ->var_bacg:
        var_wrnh = []
        var_wrnh = [None] * (var_osiz(arg_xdvx) + var_osiz(arg_rcsn))
        var_ayzf = 0
        var_wnki = 0
        for var_egyk in var_dcmd(var_osiz(arg_xdvx)):
            if var_ayzf < var_osiz(arg_rcsn) and var_egyk == arg_rcsn[var_ayzf
                ]:
                var_wrnh[var_wnki] = ' '
                var_wnki += 1
                var_ayzf += 1
            var_wrnh[var_wnki] = arg_xdvx[var_egyk]
            var_wnki += 1
        return ''.join(var_wrnh[:var_wnki])
