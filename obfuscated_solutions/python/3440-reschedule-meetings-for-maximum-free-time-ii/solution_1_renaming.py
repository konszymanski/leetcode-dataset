class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_hqta
        ], arg_bacg: var_rgwu[var_hqta]) ->var_hqta:
        var_wrnh = var_osiz(arg_rcsn)
        var_ayzf = [False] * var_wrnh
        var_wnki = 0
        var_egyk = 0
        for var_dcmd in var_llti(var_wrnh):
            if arg_bacg[var_dcmd] - arg_rcsn[var_dcmd] <= var_wnki:
                var_ayzf[var_dcmd] = True
            var_wnki = var_zbxo(var_wnki, arg_rcsn[var_dcmd] - (0 if 
                var_dcmd == 0 else arg_bacg[var_dcmd - 1]))
            if arg_bacg[var_wrnh - var_dcmd - 1] - arg_rcsn[var_wrnh -
                var_dcmd - 1] <= var_egyk:
                var_ayzf[var_wrnh - var_dcmd - 1] = True
            var_egyk = var_zbxo(var_egyk, (arg_xdvx if var_dcmd == 0 else
                arg_rcsn[var_wrnh - var_dcmd]) - arg_bacg[var_wrnh -
                var_dcmd - 1])
        var_rdmc = 0
        for var_dcmd in var_llti(var_wrnh):
            var_rjut = 0 if var_dcmd == 0 else arg_bacg[var_dcmd - 1]
            var_lsgw = arg_xdvx if var_dcmd == var_wrnh - 1 else arg_rcsn[
                var_dcmd + 1]
            if var_ayzf[var_dcmd]:
                var_rdmc = var_zbxo(var_rdmc, var_lsgw - var_rjut)
            else:
                var_rdmc = var_zbxo(var_rdmc, var_lsgw - var_rjut - (
                    arg_bacg[var_dcmd] - arg_rcsn[var_dcmd]))
        return var_rdmc
