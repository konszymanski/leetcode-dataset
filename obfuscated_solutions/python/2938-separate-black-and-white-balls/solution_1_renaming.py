class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = 0
        var_hqta = 0
        for var_rgwu, var_wrnh in var_osiz(arg_xdvx):
            if var_wrnh == '0':
                var_hqta += var_rgwu - var_bacg
                var_bacg += 1
        return var_hqta
