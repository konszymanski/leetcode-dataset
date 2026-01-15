class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti:
        var_bacg = 1000000007
        var_hqta = [([-1] * 3) for var_rgwu in var_wrnh(var_osiz(arg_xdvx))]

        def func_ayzf(arg_wnki, arg_egyk):
            if arg_wnki == var_osiz(arg_xdvx):
                return 1 if arg_egyk == 2 else 0
            if var_hqta[arg_wnki][arg_egyk] != -1:
                return var_hqta[arg_wnki][arg_egyk]
            if arg_egyk == 2:
                if arg_xdvx[arg_wnki] == 'S':
                    var_dcmd = func_ayzf(arg_wnki + 1, 1)
                else:
                    var_dcmd = (func_ayzf(arg_wnki + 1, 0) + func_ayzf(
                        arg_wnki + 1, 2)) % var_bacg
            elif arg_xdvx[arg_wnki] == 'S':
                var_dcmd = func_ayzf(arg_wnki + 1, arg_egyk + 1)
            else:
                var_dcmd = func_ayzf(arg_wnki + 1, arg_egyk)
            var_hqta[arg_wnki][arg_egyk] = var_dcmd
            return var_hqta[arg_wnki][arg_egyk]
        return func_ayzf(0, 0)
