class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = ''
        for var_wrnh in arg_xdvx:
            var_rgwu += var_bacg(var_osiz(var_wrnh) - var_osiz('a') + 1)
        for var_ayzf in var_wnki(arg_rcsn):
            var_egyk = 0
            for var_dcmd in var_rgwu:
                var_egyk += var_hqta(var_dcmd)
            if var_egyk < 10:
                return var_egyk
            var_rgwu = var_bacg(var_egyk)
        return var_hqta(var_rgwu)
