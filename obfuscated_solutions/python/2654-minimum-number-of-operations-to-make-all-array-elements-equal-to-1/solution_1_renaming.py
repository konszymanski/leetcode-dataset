class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = 0
        for var_ayzf in arg_xdvx:
            if var_ayzf == 1:
                var_wrnh += 1
            var_osiz = var_wnki(var_osiz, var_ayzf)
        if var_wrnh > 0:
            return var_hqta - var_wrnh
        if var_osiz > 1:
            return -1
        var_egyk = var_hqta
        for var_dcmd in var_llti(var_hqta):
            var_osiz = 0
            for var_zbxo in var_llti(var_dcmd, var_hqta):
                var_osiz = var_wnki(var_osiz, arg_xdvx[var_zbxo])
                if var_osiz == 1:
                    var_egyk = var_rdmc(var_egyk, var_zbxo - var_dcmd + 1)
                    break
        return var_egyk + var_hqta - 2
