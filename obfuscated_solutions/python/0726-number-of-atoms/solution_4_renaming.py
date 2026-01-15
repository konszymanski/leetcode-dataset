class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = '([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)'
        var_hqta = var_rgwu.findall(var_bacg, arg_xdvx)
        var_wrnh = [var_osiz(var_ayzf)]
        for var_wnki, var_egyk, var_dcmd, var_llti, var_zbxo in var_hqta:
            if var_wnki:
                var_wrnh[-1][var_wnki] += var_ayzf(var_egyk) if var_egyk else 1
            elif var_dcmd:
                var_wrnh.append(var_osiz(var_ayzf))
            elif var_llti:
                var_rdmc = var_wrnh.pop()
                if var_zbxo:
                    var_zbxo = var_ayzf(var_zbxo)
                    for var_wnki in var_rdmc:
                        var_rdmc[var_wnki] *= var_zbxo
                for var_wnki in var_rdmc:
                    var_wrnh[-1][var_wnki] += var_rdmc[var_wnki]
        var_rjut = var_lsgw(var_cbvh(var_wrnh[0].items()))
        var_yjch = ''
        for var_wnki in var_rjut:
            var_yjch += var_wnki
            if var_rjut[var_wnki] > 1:
                var_yjch += var_rcsn(var_rjut[var_wnki])
        return var_yjch
