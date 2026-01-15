class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu[var_wrnh], arg_rcsn:
        var_rgwu[var_wrnh], arg_bacg: var_rgwu[var_wrnh], arg_hqta:
        var_rgwu[var_wrnh]) ->var_dmio:

        def func_osiz(arg_xdvx, arg_rcsn):
            return (arg_rcsn[1] - arg_xdvx[1]) ** 2 + (arg_rcsn[0] -
                arg_xdvx[0]) ** 2

        def func_ayzf(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
            return func_osiz(arg_xdvx, arg_rcsn) > 0 and func_osiz(arg_xdvx,
                arg_rcsn) == func_osiz(arg_rcsn, arg_bacg) and func_osiz(
                arg_rcsn, arg_bacg) == func_osiz(arg_bacg, arg_hqta
                ) and func_osiz(arg_bacg, arg_hqta) == func_osiz(arg_hqta,
                arg_xdvx) and func_osiz(arg_xdvx, arg_bacg) == func_osiz(
                arg_rcsn, arg_hqta)

        def func_wnki(arg_egyk, arg_dcmd):
            if arg_dcmd == 4:
                return func_ayzf(arg_egyk[0], arg_egyk[1], arg_egyk[2],
                    arg_egyk[3])
            else:
                var_llti = False
                for var_zbxo in var_rdmc(arg_dcmd, 4):
                    arg_egyk[arg_dcmd], arg_egyk[var_zbxo] = arg_egyk[var_zbxo
                        ], arg_egyk[arg_dcmd]
                    var_llti |= func_wnki(arg_egyk, arg_dcmd + 1)
                    arg_egyk[arg_dcmd], arg_egyk[var_zbxo] = arg_egyk[var_zbxo
                        ], arg_egyk[arg_dcmd]
                return var_llti
        arg_egyk = [arg_xdvx, arg_rcsn, arg_bacg, arg_hqta]
        var_rjut = [func_osiz(arg_egyk[var_zbxo], arg_egyk[(var_zbxo + 1) %
            4]) for var_zbxo in var_rdmc(4)]
        var_rjut += [func_osiz(arg_egyk[var_zbxo], arg_egyk[(var_zbxo + 2) %
            4]) for var_zbxo in var_rdmc(4)]
        return var_lsgw(var_cbvh(var_rjut)) == 2 and var_yjch(var_rjut
            ) != 0 and func_wnki(arg_egyk, 0)
