class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = None
        for var_wrnh in arg_xdvx:
            if var_wrnh == var_rgwu:
                var_bacg += 1
            else:
                var_rgwu = var_wrnh
                var_bacg = 1
            var_hqta = var_osiz(var_hqta, var_bacg)
        return var_hqta
