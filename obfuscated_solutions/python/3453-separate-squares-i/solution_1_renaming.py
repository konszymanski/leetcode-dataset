class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_dmio:
        var_hqta, var_rgwu = 0, 0
        for var_wrnh, var_osiz, var_ayzf in arg_xdvx:
            var_rgwu += var_ayzf ** 2
            var_hqta = var_wnki(var_hqta, var_osiz + var_ayzf)

        def func_egyk(arg_dcmd):
            var_llti = 0
            for var_wrnh, var_osiz, var_ayzf in arg_xdvx:
                if var_osiz < arg_dcmd:
                    var_llti += var_ayzf * var_zbxo(arg_dcmd - var_osiz,
                        var_ayzf)
            return var_llti >= var_rgwu / 2
        var_rdmc, var_rjut = 0, var_hqta
        var_lsgw = 1e-05
        while var_cbvh(var_rjut - var_rdmc) > var_lsgw:
            var_yjch = (var_rjut + var_rdmc) / 2
            if func_egyk(var_yjch):
                var_rjut = var_yjch
            else:
                var_rdmc = var_yjch
        return var_rjut
