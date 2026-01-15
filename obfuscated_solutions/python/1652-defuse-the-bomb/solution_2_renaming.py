class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = [(0) for var_wrnh in var_osiz(var_ayzf(arg_xdvx))]
        if arg_rcsn == 0:
            return var_rgwu
        var_wnki, var_egyk, var_dcmd = 1, arg_rcsn, 0
        if arg_rcsn < 0:
            var_wnki = var_ayzf(arg_xdvx) - var_llti(arg_rcsn)
            var_egyk = var_ayzf(arg_xdvx) - 1
        for var_zbxo in var_osiz(var_wnki, var_egyk + 1):
            var_dcmd += arg_xdvx[var_zbxo]
        for var_zbxo in var_osiz(var_ayzf(arg_xdvx)):
            var_rgwu[var_zbxo] = var_dcmd
            var_dcmd -= arg_xdvx[var_wnki % var_ayzf(arg_xdvx)]
            var_dcmd += arg_xdvx[(var_egyk + 1) % var_ayzf(arg_xdvx)]
            var_wnki += 1
            var_egyk += 1
        return var_rgwu
