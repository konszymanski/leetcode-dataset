class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = [0, 1, 0, -1, 0]
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])

        def func_ayzf(arg_wnki: var_bacg, arg_egyk: var_bacg) ->var_bacg:
            var_dcmd = var_llti()
            var_zbxo = var_rdmc()
            var_rjut = 0
            var_zbxo.add((arg_wnki, arg_egyk))
            var_dcmd.append((arg_wnki, arg_egyk, arg_xdvx[arg_wnki][
                arg_egyk], var_zbxo))
            while var_dcmd:
                var_lsgw, var_cbvh, var_yjch, var_dmio = var_dcmd.popleft()
                var_rjut = var_ulfl(var_rjut, var_yjch)
                for var_lgvi in var_wvuc(4):
                    var_tufr = var_lsgw + var_hqta[var_lgvi]
                    var_xhfo = var_cbvh + var_hqta[var_lgvi + 1]
                    if (0 <= var_tufr < var_rgwu and 0 <= var_xhfo <
                        var_osiz and arg_xdvx[var_tufr][var_xhfo] != 0 and 
                        (var_tufr, var_xhfo) not in var_dmio):
                        var_dmio.add((var_tufr, var_xhfo))
                        var_dcmd.append((var_tufr, var_xhfo, var_yjch +
                            arg_xdvx[var_tufr][var_xhfo], var_dmio.copy()))
                        var_dmio.remove((var_tufr, var_xhfo))
            return var_rjut
        var_miuw = var_rhvk(var_rhvk(arg_wnki) for arg_wnki in arg_xdvx)
        var_rjut = 0
        for arg_wnki in var_wvuc(var_rgwu):
            for arg_egyk in var_wvuc(var_osiz):
                if arg_xdvx[arg_wnki][arg_egyk] != 0:
                    var_rjut = var_ulfl(var_rjut, func_ayzf(arg_wnki, arg_egyk)
                        )
                    if var_rjut == var_miuw:
                        return var_miuw
        return var_rjut
