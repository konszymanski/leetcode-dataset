class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki[var_egyk]:
        var_bacg = [0] * var_hqta(arg_xdvx)
        for var_rgwu in var_wrnh(var_hqta(arg_xdvx)):
            if arg_xdvx[var_rgwu] == '1':
                for var_osiz in var_wrnh(var_hqta(arg_xdvx)):
                    var_bacg[var_osiz] += var_ayzf(var_osiz - var_rgwu)
        return var_bacg
