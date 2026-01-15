class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_hqta[var_rgwu]],
        arg_rcsn: var_hqta[var_hqta[var_rgwu]], arg_bacg: var_rgwu) ->var_hqta[
        var_rgwu]:

        def func_wrnh(arg_osiz: var_rgwu, arg_ayzf: var_rgwu, arg_wnki:
            var_hqta[var_hqta[var_rgwu]], arg_bacg: var_rgwu) ->var_rgwu:
            if arg_bacg < 0:
                return 0
            var_egyk = 1
            for var_dcmd in arg_wnki[arg_osiz]:
                if var_dcmd == arg_ayzf:
                    continue
                var_egyk += func_wrnh(var_dcmd, arg_osiz, arg_wnki, 
                    arg_bacg - 1)
            return var_egyk

        def func_llti(arg_zbxo: var_hqta[var_hqta[var_rgwu]], arg_bacg:
            var_rgwu) ->var_hqta[var_rgwu]:
            var_rdmc = var_rjut(arg_zbxo) + 1
            arg_wnki = [[] for var_lsgw in var_cbvh(var_rdmc)]
            for var_yjch, var_dmio in arg_zbxo:
                arg_wnki[var_yjch].append(var_dmio)
                arg_wnki[var_dmio].append(var_yjch)
            var_egyk = [0] * var_rdmc
            for var_ulfl in var_cbvh(var_rdmc):
                var_egyk[var_ulfl] = func_wrnh(var_ulfl, -1, arg_wnki, arg_bacg
                    )
            return var_egyk
        var_rdmc = var_rjut(arg_xdvx) + 1
        var_lgvi = func_llti(arg_xdvx, arg_bacg)
        var_wvuc = func_llti(arg_rcsn, arg_bacg - 1)
        var_tufr = var_xhfo(var_wvuc)
        var_egyk = [(var_lgvi[var_ulfl] + var_tufr) for var_ulfl in
            var_cbvh(var_rdmc)]
        return var_egyk
