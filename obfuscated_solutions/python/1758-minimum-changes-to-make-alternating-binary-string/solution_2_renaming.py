class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = 0
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            if var_hqta % 2 == 0:
                if arg_xdvx[var_hqta] == '1':
                    var_bacg += 1
            elif arg_xdvx[var_hqta] == '0':
                var_bacg += 1
        return var_osiz(var_bacg, var_wrnh(arg_xdvx) - var_bacg)
