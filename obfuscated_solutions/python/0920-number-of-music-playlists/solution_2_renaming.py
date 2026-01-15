class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu = 1000000007
        var_wrnh = [[(-1) for var_osiz in var_ayzf(arg_xdvx + 1)] for
            var_osiz in var_ayzf(arg_rcsn + 1)]

        def func_wnki(arg_egyk, arg_dcmd):
            if arg_egyk == 0 and arg_dcmd == 0:
                return 1
            if arg_egyk == 0 or arg_dcmd == 0:
                return 0
            if var_wrnh[arg_egyk][arg_dcmd] != -1:
                return var_wrnh[arg_egyk][arg_dcmd]
            var_wrnh[arg_egyk][arg_dcmd] = func_wnki(arg_egyk - 1, arg_dcmd - 1
                ) * (arg_xdvx - arg_dcmd + 1) % var_rgwu
            if arg_dcmd > arg_bacg:
                var_wrnh[arg_egyk][arg_dcmd] += func_wnki(arg_egyk - 1,
                    arg_dcmd) * (arg_dcmd - arg_bacg) % var_rgwu
                var_wrnh[arg_egyk][arg_dcmd] %= var_rgwu
            return var_wrnh[arg_egyk][arg_dcmd]
        return func_wnki(arg_rcsn, arg_xdvx)
