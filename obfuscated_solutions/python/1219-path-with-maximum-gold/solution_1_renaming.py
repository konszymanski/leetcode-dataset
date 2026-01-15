class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = [0, 1, 0, -1, 0]
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])
        var_ayzf = 0

        def func_wnki(arg_xdvx, var_rgwu, var_osiz, arg_egyk, arg_dcmd):
            if (arg_egyk < 0 or arg_dcmd < 0 or arg_egyk == var_rgwu or 
                arg_dcmd == var_osiz or arg_xdvx[arg_egyk][arg_dcmd] == 0):
                return 0
            var_ayzf = 0
            var_llti = arg_xdvx[arg_egyk][arg_dcmd]
            arg_xdvx[arg_egyk][arg_dcmd] = 0
            for var_zbxo in var_rdmc(4):
                var_ayzf = var_rjut(var_ayzf, func_wnki(arg_xdvx, var_rgwu,
                    var_osiz, var_hqta[var_zbxo] + arg_egyk, var_hqta[
                    var_zbxo + 1] + arg_dcmd))
            arg_xdvx[arg_egyk][arg_dcmd] = var_llti
            return var_ayzf + var_llti
        for arg_egyk in var_rdmc(var_rgwu):
            for arg_dcmd in var_rdmc(var_osiz):
                var_ayzf = var_rjut(var_ayzf, func_wnki(arg_xdvx, var_rgwu,
                    var_osiz, arg_egyk, arg_dcmd))
        return var_ayzf
