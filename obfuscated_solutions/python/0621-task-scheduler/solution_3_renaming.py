class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_rgwu:
        var_wrnh = [0] * 26
        var_osiz = 0
        var_ayzf = 0
        for var_wnki in arg_xdvx:
            var_wrnh[var_egyk(var_wnki) - var_egyk('A')] += 1
            if var_osiz == var_wrnh[var_egyk(var_wnki) - var_egyk('A')]:
                var_ayzf += 1
            elif var_osiz < var_wrnh[var_egyk(var_wnki) - var_egyk('A')]:
                var_osiz = var_wrnh[var_egyk(var_wnki) - var_egyk('A')]
                var_ayzf = 1
        var_dcmd = var_osiz - 1
        var_llti = arg_rcsn - (var_ayzf - 1)
        var_zbxo = var_dcmd * var_llti
        var_rdmc = var_rjut(arg_xdvx) - var_osiz * var_ayzf
        var_lsgw = var_cbvh(0, var_zbxo - var_rdmc)
        return var_rjut(arg_xdvx) + var_lsgw
