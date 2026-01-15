class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = 10 ** 9 + 7

        def func_wrnh(arg_xdvx, arg_rcsn, arg_osiz):
            var_ayzf = 0
            var_wnki = 0
            var_egyk = 0
            var_dcmd = 0
            var_llti = 0
            for var_zbxo in var_rdmc(arg_rcsn):
                var_wnki += arg_xdvx[var_zbxo]
                var_dcmd += arg_xdvx[var_zbxo] * (var_zbxo - var_llti + 1)
                while var_wnki > arg_osiz:
                    var_dcmd -= var_wnki
                    var_wnki -= arg_xdvx[var_llti]
                    var_llti += 1
                var_ayzf += var_zbxo - var_llti + 1
                var_egyk += var_dcmd
            return var_ayzf, var_egyk

        def func_rjut(arg_xdvx, arg_rcsn, arg_lsgw):
            var_cbvh = var_yjch(arg_xdvx)
            var_dmio = var_ulfl(arg_xdvx)
            arg_bacg = var_cbvh
            arg_hqta = var_dmio
            while arg_bacg <= arg_hqta:
                var_lgvi = arg_bacg + (arg_hqta - arg_bacg) // 2
                if func_wrnh(arg_xdvx, arg_rcsn, var_lgvi)[0] >= arg_lsgw:
                    arg_hqta = var_lgvi - 1
                else:
                    arg_bacg = var_lgvi + 1
            var_ayzf, var_egyk = func_wrnh(arg_xdvx, arg_rcsn, arg_bacg)
            return var_egyk - arg_bacg * (var_ayzf - arg_lsgw)
        var_wvuc = (func_rjut(arg_xdvx, arg_rcsn, arg_hqta) - func_rjut(
            arg_xdvx, arg_rcsn, arg_bacg - 1)) % var_rgwu
        return (var_wvuc + var_rgwu) % var_rgwu
