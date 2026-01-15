class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:

        @var_wnki
        def func_hqta(arg_rgwu, arg_wrnh):
            if arg_wrnh == 0:
                if arg_rgwu == 0:
                    return 1
                return 0
            var_osiz = func_hqta(arg_rgwu, arg_wrnh - 1)
            if arg_rgwu > 0:
                var_osiz = (var_osiz + func_hqta(arg_rgwu - 1, arg_wrnh - 1)
                    ) % var_ayzf
            if arg_rgwu < arg_rcsn - 1:
                var_osiz = (var_osiz + func_hqta(arg_rgwu + 1, arg_wrnh - 1)
                    ) % var_ayzf
            return var_osiz
        var_ayzf = 10 ** 9 + 7
        return func_hqta(0, arg_xdvx)
