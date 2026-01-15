class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_lsgw[
        var_bacg]:
        if arg_xdvx == 1:
            return [var_hqta for var_hqta in var_rgwu(10)]
        var_wrnh = [var_osiz for var_osiz in var_rgwu(1, 10)]
        for var_ayzf in var_rgwu(arg_xdvx - 1):
            var_wnki = []
            for var_egyk in var_wrnh:
                var_dcmd = var_egyk % 10
                var_llti = var_zbxo([var_dcmd + arg_rcsn, var_dcmd - arg_rcsn])
                for var_rdmc in var_llti:
                    if 0 <= var_rdmc < 10:
                        var_rjut = var_egyk * 10 + var_rdmc
                        var_wnki.append(var_rjut)
            var_wrnh = var_wnki
        return var_wrnh
