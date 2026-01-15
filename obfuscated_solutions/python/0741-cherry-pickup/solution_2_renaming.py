class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = [[([None] * var_bacg) for var_wrnh in var_osiz(var_bacg)
            ] for var_ayzf in var_osiz(var_bacg)]

        def func_wnki(arg_egyk, arg_dcmd, arg_llti):
            var_zbxo = arg_egyk + arg_dcmd - arg_llti
            if (var_bacg == arg_egyk or var_bacg == var_zbxo or var_bacg ==
                arg_dcmd or var_bacg == arg_llti or arg_rcsn[arg_egyk][
                arg_dcmd] == -1 or arg_rcsn[var_zbxo][arg_llti] == -1):
                return var_rdmc('-inf')
            elif arg_egyk == arg_dcmd == var_bacg - 1:
                return arg_rcsn[arg_egyk][arg_dcmd]
            elif var_rgwu[arg_egyk][arg_dcmd][arg_llti] is not None:
                return var_rgwu[arg_egyk][arg_dcmd][arg_llti]
            else:
                var_rjut = arg_rcsn[arg_egyk][arg_dcmd] + (arg_dcmd != arg_llti
                    ) * arg_rcsn[var_zbxo][arg_llti]
                var_rjut += var_lsgw(func_wnki(arg_egyk, arg_dcmd + 1, 
                    arg_llti + 1), func_wnki(arg_egyk + 1, arg_dcmd, 
                    arg_llti + 1), func_wnki(arg_egyk, arg_dcmd + 1,
                    arg_llti), func_wnki(arg_egyk + 1, arg_dcmd, arg_llti))
            var_rgwu[arg_egyk][arg_dcmd][arg_llti] = var_rjut
            return var_rjut
        return var_lsgw(0, func_wnki(0, 0, 0))
