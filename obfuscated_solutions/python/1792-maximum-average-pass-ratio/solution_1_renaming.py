class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_yjch:
        var_rgwu = []
        for var_wrnh in arg_xdvx:
            var_osiz = var_wrnh[0] / var_wrnh[1]
            var_rgwu.append(var_osiz)
        while arg_rcsn > 0:
            var_ayzf = []
            for var_wrnh in arg_xdvx:
                var_wnki = (var_wrnh[0] + 1) / (var_wrnh[1] + 1)
                var_ayzf.append(var_wnki)
            var_egyk = 0
            var_dcmd = 0
            for var_llti in var_zbxo(var_rdmc(var_ayzf)):
                var_rjut = var_ayzf[var_llti] - var_rgwu[var_llti]
                if var_rjut > var_dcmd:
                    var_egyk = var_llti
                    var_dcmd = var_rjut
            var_rgwu[var_egyk] = var_ayzf[var_egyk]
            arg_xdvx[var_egyk][0] += 1
            arg_xdvx[var_egyk][1] += 1
            arg_rcsn -= 1
        var_lsgw = var_cbvh(var_rgwu)
        return var_lsgw / var_rdmc(arg_xdvx)
