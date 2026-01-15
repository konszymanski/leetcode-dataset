class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = var_ayzf('inf')
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            if arg_xdvx[var_wnki] == 'W':
                var_wrnh += 1
            if var_wnki - var_rgwu + 1 == arg_rcsn:
                var_osiz = var_llti(var_osiz, var_wrnh)
                if arg_xdvx[var_rgwu] == 'W':
                    var_wrnh -= 1
                var_rgwu += 1
        return var_osiz
