class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 10 ** 9 + 7

        def func_hqta(arg_rgwu: var_rcsn, arg_wrnh: var_rcsn) ->var_rcsn:
            var_osiz, var_ayzf = 1, arg_rgwu
            while arg_wrnh > 0:
                if arg_wrnh % 2 == 1:
                    var_osiz = var_osiz * var_ayzf % var_bacg
                var_ayzf = var_ayzf * var_ayzf % var_bacg
                arg_wrnh //= 2
            return var_osiz
        return func_hqta(5, (arg_xdvx + 1) // 2) * func_hqta(4, arg_xdvx // 2
            ) % var_bacg
