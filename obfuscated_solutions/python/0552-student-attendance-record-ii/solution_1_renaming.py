class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 1000000007
        var_hqta = [[([-1] * 3) for var_rgwu in var_wrnh(2)] for var_rgwu in
            var_wrnh(arg_xdvx + 1)]

        def func_osiz(arg_xdvx, arg_ayzf, arg_wnki):
            if arg_ayzf >= 2 or arg_wnki >= 3:
                return 0
            if arg_xdvx == 0:
                return 1
            if var_hqta[arg_xdvx][arg_ayzf][arg_wnki] != -1:
                return var_hqta[arg_xdvx][arg_ayzf][arg_wnki]
            var_egyk = func_osiz(arg_xdvx - 1, arg_ayzf, 0)
            var_egyk = (var_egyk + func_osiz(arg_xdvx - 1, arg_ayzf + 1, 0)
                ) % var_bacg
            var_egyk = (var_egyk + func_osiz(arg_xdvx - 1, arg_ayzf, 
                arg_wnki + 1)) % var_bacg
            var_hqta[arg_xdvx][arg_ayzf][arg_wnki] = var_egyk
            return var_egyk
        return func_osiz(arg_xdvx, 0, 0)
