class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg, var_hqta = 1, arg_xdvx
        var_rgwu = arg_xdvx * (arg_xdvx + 1) // 2
        while var_bacg < var_hqta:
            var_wrnh = (var_bacg + var_hqta) // 2
            if var_wrnh * var_wrnh - var_rgwu < 0:
                var_bacg = var_wrnh + 1
            else:
                var_hqta = var_wrnh
        if var_bacg * var_bacg - var_rgwu == 0:
            return var_bacg
        else:
            return -1
