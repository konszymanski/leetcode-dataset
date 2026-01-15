class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:

        def func_rgwu(arg_xdvx, arg_rcsn):
            var_wrnh = var_osiz(arg_xdvx)
            var_ayzf = [0] * arg_rcsn
            var_wnki = var_egyk
            for var_dcmd in var_llti(arg_rcsn - 1, -1, -1):
                var_wnki = var_zbxo(var_wnki, arg_xdvx[var_dcmd])
                var_ayzf[var_dcmd] = var_wnki
            var_rdmc = []
            var_wnki = var_egyk
            for var_dcmd in var_llti(arg_rcsn, var_wrnh):
                var_wnki = var_zbxo(var_wnki, arg_xdvx[var_dcmd])
                var_rdmc.append(var_wnki)
            var_rjut = 0
            for var_lsgw in var_llti(var_osiz(var_rdmc)):
                var_wnki = var_rdmc[var_lsgw]
                var_dcmd = var_cbvh(var_ayzf, var_wnki)
                var_yjch = arg_rcsn + var_lsgw - var_dcmd + 1
                var_rjut = var_dmio(var_rjut, var_wnki * var_yjch)
            return var_rjut
        return var_dmio(func_rgwu(arg_xdvx, arg_rcsn), func_rgwu(arg_xdvx[:
            :-1], var_osiz(arg_xdvx) - arg_rcsn - 1))
