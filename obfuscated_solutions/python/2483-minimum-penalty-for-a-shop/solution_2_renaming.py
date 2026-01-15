class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_wnki = arg_xdvx[var_wrnh]
            if var_wnki == 'Y':
                var_hqta -= 1
            else:
                var_hqta += 1
            if var_hqta < var_bacg:
                var_rgwu = var_wrnh + 1
                var_bacg = var_hqta
        return var_rgwu
