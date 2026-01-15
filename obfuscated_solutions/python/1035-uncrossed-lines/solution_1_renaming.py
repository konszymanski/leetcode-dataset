class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_rgwu(arg_bacg)
        var_osiz = {}

        def func_ayzf(arg_wnki, arg_egyk):
            if arg_wnki <= 0 or arg_egyk <= 0:
                return 0
            if (arg_wnki, arg_egyk) in var_osiz:
                return var_osiz[arg_wnki, arg_egyk]
            if arg_rcsn[arg_wnki - 1] == arg_bacg[arg_egyk - 1]:
                var_osiz[arg_wnki, arg_egyk] = 1 + func_ayzf(arg_wnki - 1, 
                    arg_egyk - 1)
            else:
                var_osiz[arg_wnki, arg_egyk] = var_dcmd(func_ayzf(arg_wnki -
                    1, arg_egyk), func_ayzf(arg_wnki, arg_egyk - 1))
            return var_osiz[arg_wnki, arg_egyk]
        return func_ayzf(var_hqta, var_wrnh)
