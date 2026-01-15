class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh(arg_rcsn)
        var_osiz = var_hqta(var_ayzf.sqrt(var_rgwu))
        var_wnki = (var_rgwu + var_osiz - 1) // var_osiz
        var_egyk = 0
        var_dcmd = [0] * var_wnki
        for var_llti in var_zbxo(var_rgwu):
            var_dcmd[var_llti // var_osiz] = var_rdmc(var_dcmd[var_llti //
                var_osiz], arg_rcsn[var_llti])
        for var_rjut in arg_xdvx:
            var_lsgw = 1
            for var_cbvh in var_zbxo(var_wnki):
                if var_dcmd[var_cbvh] < var_rjut:
                    continue
                var_yjch = 0
                var_dcmd[var_cbvh] = 0
                for var_llti in var_zbxo(var_osiz):
                    var_dmio = var_cbvh * var_osiz + var_llti
                    if var_dmio < var_rgwu and arg_rcsn[var_dmio
                        ] >= var_rjut and not var_yjch:
                        arg_rcsn[var_dmio] = 0
                        var_yjch = 1
                    if var_dmio < var_rgwu:
                        var_dcmd[var_cbvh] = var_rdmc(var_dcmd[var_cbvh],
                            arg_rcsn[var_dmio])
                var_lsgw = 0
                break
            var_egyk += var_lsgw
        return var_egyk
