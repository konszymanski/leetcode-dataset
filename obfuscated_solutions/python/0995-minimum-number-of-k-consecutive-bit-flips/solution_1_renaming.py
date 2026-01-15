class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [False] * var_wrnh(arg_xdvx)
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in var_egyk(var_wrnh(arg_xdvx)):
            if var_wnki >= arg_rcsn:
                if var_rgwu[var_wnki - arg_rcsn]:
                    var_osiz -= 1
            if var_osiz % 2 == arg_xdvx[var_wnki]:
                if var_wnki + arg_rcsn > var_wrnh(arg_xdvx):
                    return -1
                var_osiz += 1
                var_rgwu[var_wnki] = True
                var_ayzf += 1
        return var_ayzf
