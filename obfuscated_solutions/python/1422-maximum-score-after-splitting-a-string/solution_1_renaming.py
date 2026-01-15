class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = 0
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx) - 1):
            var_osiz = 0
            for var_ayzf in var_rgwu(var_hqta + 1):
                if arg_xdvx[var_ayzf] == '0':
                    var_osiz += 1
            for var_ayzf in var_rgwu(var_hqta + 1, var_wrnh(arg_xdvx)):
                if arg_xdvx[var_ayzf] == '1':
                    var_osiz += 1
            var_bacg = var_wnki(var_bacg, var_osiz)
        return var_bacg
