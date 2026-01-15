class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd:
        var_bacg = var_hqta(var_rgwu == 'Y' for var_rgwu in arg_xdvx)
        var_wrnh = var_bacg
        var_osiz = 0
        for var_ayzf, var_wnki in var_egyk(arg_xdvx):
            if var_wnki == 'Y':
                var_bacg -= 1
            else:
                var_bacg += 1
            if var_bacg < var_wrnh:
                var_osiz = var_ayzf + 1
                var_wrnh = var_bacg
        return var_osiz
