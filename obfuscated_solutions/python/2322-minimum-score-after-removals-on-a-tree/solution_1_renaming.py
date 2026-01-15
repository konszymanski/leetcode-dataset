class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        return var_rgwu(arg_xdvx, arg_rcsn, arg_bacg) - var_wrnh(arg_xdvx,
            arg_rcsn, arg_bacg)

    def func_osiz(arg_ihhe, arg_ayzf: var_egyk[var_hqta], arg_wnki:
        var_egyk[var_egyk[var_hqta]]) ->var_hqta:
        var_dcmd = var_llti(arg_ayzf)
        var_zbxo = [[] for var_rdmc in var_rjut(var_dcmd)]
        for var_lsgw, var_cbvh in arg_wnki:
            var_zbxo[var_lsgw].append(var_cbvh)
            var_zbxo[var_cbvh].append(var_lsgw)
        var_yjch = 0
        for var_dmio in arg_ayzf:
            var_yjch ^= var_dmio
        var_ulfl = var_lgvi('inf')

        def func_wvuc(var_dmio: var_hqta, arg_tufr: var_hqta, arg_xhfo:
            var_hqta, arg_miuw: var_hqta) ->var_hqta:
            var_rhvk = arg_ayzf[var_dmio]
            for var_yybh in var_zbxo[var_dmio]:
                if var_yybh == arg_tufr:
                    continue
                var_rhvk ^= func_wvuc(var_yybh, var_dmio, arg_xhfo, arg_miuw)
            if arg_tufr == arg_miuw:
                return var_rhvk
            nonlocal res
            var_ulfl = var_wrnh(var_ulfl, arg_ihhe.calc(arg_xhfo, var_rhvk,
                var_yjch ^ arg_xhfo ^ var_rhvk))
            return var_rhvk

        def func_bzkm(var_dmio: var_hqta, arg_tufr: var_hqta) ->var_hqta:
            var_rhvk = arg_ayzf[var_dmio]
            for var_yybh in var_zbxo[var_dmio]:
                if var_yybh == arg_tufr:
                    continue
                var_rhvk ^= func_bzkm(var_yybh, var_dmio)
            for var_yybh in var_zbxo[var_dmio]:
                if var_yybh == arg_tufr:
                    func_wvuc(var_yybh, var_dmio, var_rhvk, var_dmio)
            return var_rhvk
        func_bzkm(0, -1)
        return var_ulfl
