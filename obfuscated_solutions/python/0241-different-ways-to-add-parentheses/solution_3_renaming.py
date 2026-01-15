class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd[var_llti]:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [[[] for var_wrnh in var_osiz(var_bacg)] for var_wrnh in
            var_osiz(var_bacg)]
        arg_ihhe._initialize_base_cases(arg_xdvx, var_rgwu)
        for var_ayzf in var_osiz(3, var_bacg + 1):
            for var_wnki in var_osiz(var_bacg - var_ayzf + 1):
                var_egyk = var_wnki + var_ayzf - 1
                arg_ihhe._process_subexpression(arg_xdvx, var_rgwu,
                    var_wnki, var_egyk)
        return var_rgwu[0][var_bacg - 1]

    def func_zbxo(arg_ihhe, arg_xdvx: var_rcsn, var_rgwu: var_dcmd[var_dcmd
        [var_dcmd[var_llti]]]):
        for var_rdmc, var_rjut in var_lsgw(arg_xdvx):
            if var_rjut.isdigit():
                var_cbvh = var_yjch(var_rjut) - var_yjch('0')
                if var_rdmc + 1 < var_hqta(arg_xdvx) and arg_xdvx[var_rdmc + 1
                    ].isdigit():
                    var_dmio = var_yjch(arg_xdvx[var_rdmc + 1]) - var_yjch('0')
                    var_ulfl = var_cbvh * 10 + var_dmio
                    var_rgwu[var_rdmc][var_rdmc + 1].append(var_ulfl)
                var_rgwu[var_rdmc][var_rdmc].append(var_cbvh)

    def func_lgvi(arg_ihhe, arg_xdvx: var_rcsn, var_rgwu: var_dcmd[var_dcmd
        [var_dcmd[var_llti]]], var_wnki: var_llti, var_egyk: var_llti):
        for var_wvuc in var_osiz(var_wnki, var_egyk + 1):
            if arg_xdvx[var_wvuc].isdigit():
                continue
            var_tufr = var_rgwu[var_wnki][var_wvuc - 1]
            var_xhfo = var_rgwu[var_wvuc + 1][var_egyk]
            arg_ihhe._compute_results(arg_xdvx[var_wvuc], var_tufr,
                var_xhfo, var_rgwu[var_wnki][var_egyk])

    def func_miuw(arg_ihhe, arg_rhvk: var_rcsn, var_tufr: var_dcmd[var_llti
        ], var_xhfo: var_dcmd[var_llti], arg_yybh: var_dcmd[var_llti]):
        for var_bzkm in var_tufr:
            for var_icgs in var_xhfo:
                if arg_rhvk == '+':
                    arg_yybh.append(var_bzkm + var_icgs)
                elif arg_rhvk == '-':
                    arg_yybh.append(var_bzkm - var_icgs)
                elif arg_rhvk == '*':
                    arg_yybh.append(var_bzkm * var_icgs)
