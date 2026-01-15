class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:

        def func_rgwu(arg_wrnh):
            var_osiz = arg_xdvx[arg_wrnh]
            var_ayzf = 0
            var_wnki = arg_wrnh
            var_egyk = arg_wrnh
            while var_ayzf <= var_wnki:
                var_dcmd = (var_ayzf + var_wnki) // 2
                var_llti = arg_wrnh - var_dcmd + 1
                var_zbxo = var_llti * var_osiz
                var_rdmc = var_rjut[arg_wrnh] - var_rjut[var_dcmd] + arg_xdvx[
                    var_dcmd]
                var_lsgw = var_zbxo - var_rdmc
                if var_lsgw > arg_rcsn:
                    var_ayzf = var_dcmd + 1
                else:
                    var_egyk = var_dcmd
                    var_wnki = var_dcmd - 1
            return arg_wrnh - var_egyk + 1
        arg_xdvx.sort()
        var_rjut = [arg_xdvx[0]]
        for arg_wrnh in var_cbvh(1, var_yjch(arg_xdvx)):
            var_rjut.append(arg_xdvx[arg_wrnh] + var_rjut[-1])
        var_dmio = 0
        for arg_wrnh in var_cbvh(var_yjch(arg_xdvx)):
            var_dmio = var_ulfl(var_dmio, func_rgwu(arg_wrnh))
        return var_dmio
