class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_bacg:
        var_rgwu = [(-var_wrnh(var_osiz), var_ayzf) for var_osiz, var_ayzf in
            var_wnki(arg_xdvx).items()]
        var_egyk(var_rgwu)
        var_dcmd = []
        while var_rgwu:
            var_llti, var_zbxo = var_rdmc(var_rgwu)
            var_rjut = var_lsgw(-var_llti)
            var_cbvh = var_yjch(var_zbxo, arg_rcsn)
            var_dcmd.append(var_rjut * var_cbvh)
            if var_zbxo > var_cbvh and var_rgwu:
                var_dmio, var_ulfl = var_rdmc(var_rgwu)
                var_dcmd.append(var_lsgw(-var_dmio))
                if var_ulfl > 1:
                    var_lgvi(var_rgwu, (var_dmio, var_ulfl - 1))
                var_lgvi(var_rgwu, (var_llti, var_zbxo - var_cbvh))
        return ''.join(var_dcmd)
