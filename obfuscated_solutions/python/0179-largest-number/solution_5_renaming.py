class Solution:
    var_udax = 32

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg[var_hqta]) ->var_osiz:
        arg_xdvx.tim_sort(arg_rcsn)
        var_rgwu = ''.join(var_wrnh(var_osiz, arg_rcsn))
        return '0' if var_rgwu[0] == '0' else var_rgwu

    def func_ayzf(arg_xdvx, arg_rcsn: var_bacg[var_hqta], arg_wnki:
        var_hqta, arg_egyk: var_hqta):
        for var_dcmd in var_llti(arg_wnki + 1, arg_egyk + 1):
            var_zbxo = arg_rcsn[var_dcmd]
            var_rdmc = var_dcmd - 1
            while var_rdmc >= arg_wnki and arg_xdvx.compare(var_zbxo,
                arg_rcsn[var_rdmc]):
                arg_rcsn[var_rdmc + 1] = arg_rcsn[var_rdmc]
                var_rdmc -= 1
            arg_rcsn[var_rdmc + 1] = var_zbxo

    def func_rjut(arg_xdvx, arg_rcsn: var_bacg[var_hqta], arg_wnki:
        var_hqta, arg_lsgw: var_hqta, arg_egyk: var_hqta):
        var_cbvh = arg_rcsn[arg_wnki:arg_lsgw + 1]
        var_yjch = arg_rcsn[arg_lsgw + 1:arg_egyk + 1]
        var_dcmd, var_rdmc, var_dmio = 0, 0, arg_wnki
        while var_dcmd < var_ulfl(var_cbvh) and var_rdmc < var_ulfl(var_yjch):
            if arg_xdvx.compare(var_cbvh[var_dcmd], var_yjch[var_rdmc]):
                arg_rcsn[var_dmio] = var_cbvh[var_dcmd]
                var_dcmd += 1
            else:
                arg_rcsn[var_dmio] = var_yjch[var_rdmc]
                var_rdmc += 1
            var_dmio += 1
        arg_rcsn[var_dmio:arg_egyk + 1] = var_cbvh[var_dcmd:] + var_yjch[
            var_rdmc:]

    def func_lgvi(arg_xdvx, arg_rcsn: var_bacg[var_hqta]):
        var_wvuc = var_ulfl(arg_rcsn)
        for var_dcmd in var_llti(0, var_wvuc, arg_xdvx.RUN):
            arg_xdvx.insertion_sort(arg_rcsn, var_dcmd, var_tufr(var_dcmd +
                arg_xdvx.RUN - 1, var_wvuc - 1))
        var_xhfo = arg_xdvx.RUN
        while var_xhfo < var_wvuc:
            for arg_wnki in var_llti(0, var_wvuc, 2 * var_xhfo):
                arg_lsgw = arg_wnki + var_xhfo - 1
                arg_egyk = var_tufr(arg_wnki + 2 * var_xhfo - 1, var_wvuc - 1)
                if arg_lsgw < arg_egyk:
                    arg_xdvx.merge(arg_rcsn, arg_wnki, arg_lsgw, arg_egyk)
            var_xhfo *= 2

    def func_miuw(arg_xdvx, arg_rhvk: var_hqta, arg_yybh: var_hqta) ->var_bzkm:
        return var_osiz(arg_rhvk) + var_osiz(arg_yybh) > var_osiz(arg_yybh
            ) + var_osiz(arg_rhvk)
