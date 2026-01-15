class Graph:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]):
        arg_ihhe.adj_list = [[] for var_rgwu in var_wrnh(arg_xdvx)]
        for var_osiz, var_ayzf, var_wnki in arg_rcsn:
            arg_ihhe.adj_list[var_osiz].append((var_ayzf, var_wnki))

    def func_egyk(arg_ihhe, arg_dcmd: var_hqta[var_bacg]) ->None:
        var_osiz, var_ayzf, var_wnki = arg_dcmd
        arg_ihhe.adj_list[var_osiz].append((var_ayzf, var_wnki))

    def func_llti(arg_ihhe, arg_zbxo: var_bacg, arg_rdmc: var_bacg) ->var_bacg:
        arg_xdvx = var_rjut(arg_ihhe.adj_list)
        var_lsgw = [(0, arg_zbxo)]
        var_cbvh = [var_yjch] * arg_xdvx
        var_cbvh[arg_zbxo] = 0
        while var_lsgw:
            var_dmio, var_ulfl = var_lgvi(var_lsgw)
            if var_dmio > var_cbvh[var_ulfl]:
                continue
            if var_ulfl == arg_rdmc:
                return var_dmio
            for var_wvuc, var_wnki in arg_ihhe.adj_list[var_ulfl]:
                var_tufr = var_dmio + var_wnki
                if var_tufr < var_cbvh[var_wvuc]:
                    var_cbvh[var_wvuc] = var_tufr
                    var_xhfo(var_lsgw, (var_tufr, var_wvuc))
        return -1
