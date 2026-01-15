class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [1, -1][arg_xdvx < 0]
        var_hqta, arg_xdvx = 0, var_rgwu(arg_xdvx)
        while arg_xdvx:
            arg_xdvx, var_wrnh = var_osiz(arg_xdvx, 10)
            var_hqta = var_hqta * 10 + var_wrnh
            if var_hqta > 2 ** 31 - 1:
                return 0
        return var_bacg * var_hqta
