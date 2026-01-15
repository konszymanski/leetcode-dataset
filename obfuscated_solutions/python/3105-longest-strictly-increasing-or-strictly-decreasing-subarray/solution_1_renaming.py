class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            var_ayzf = 1
            for var_wnki in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                if arg_xdvx[var_wnki] > arg_xdvx[var_wnki - 1]:
                    var_ayzf += 1
                else:
                    break
            var_hqta = var_egyk(var_hqta, var_ayzf)
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            var_ayzf = 1
            for var_wnki in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                if arg_xdvx[var_wnki] < arg_xdvx[var_wnki - 1]:
                    var_ayzf += 1
                else:
                    break
            var_hqta = var_egyk(var_hqta, var_ayzf)
        return var_hqta
