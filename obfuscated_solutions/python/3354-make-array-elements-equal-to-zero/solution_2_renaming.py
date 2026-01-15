class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz, var_ayzf = 0, var_rgwu
        for var_wnki in var_egyk(var_rcsn):
            if arg_xdvx[var_wnki] == 0:
                if 0 <= var_osiz - var_ayzf <= 1:
                    var_hqta += 1
                if 0 <= var_ayzf - var_osiz <= 1:
                    var_hqta += 1
            else:
                var_osiz += arg_xdvx[var_wnki]
                var_ayzf -= arg_xdvx[var_wnki]
        return var_hqta
