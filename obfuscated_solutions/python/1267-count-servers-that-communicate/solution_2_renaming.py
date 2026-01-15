class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        if not arg_xdvx:
            return 0
        var_hqta = [0] * var_rgwu(arg_xdvx[0])
        var_wrnh = [0] * var_rgwu(arg_xdvx)
        for var_osiz in var_ayzf(var_rgwu(arg_xdvx)):
            for var_wnki in var_ayzf(var_rgwu(arg_xdvx[0])):
                if arg_xdvx[var_osiz][var_wnki]:
                    var_hqta[var_wnki] += 1
                    var_wrnh[var_osiz] += 1
        var_egyk = 0
        for var_osiz in var_ayzf(var_rgwu(arg_xdvx)):
            for var_wnki in var_ayzf(var_rgwu(arg_xdvx[0])):
                if arg_xdvx[var_osiz][var_wnki]:
                    if var_hqta[var_wnki] > 1 or var_wrnh[var_osiz] > 1:
                        var_egyk += 1
        return var_egyk
