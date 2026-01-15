class DSU:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        arg_ihhe.par = var_bacg(arg_xdvx * arg_rcsn + 1)
        arg_ihhe.rnk = [0] * (arg_xdvx * arg_rcsn + 1)
        arg_ihhe.sz = [1] * (arg_xdvx * arg_rcsn + 1)

    def func_hqta(arg_ihhe, arg_rgwu):
        if arg_ihhe.par[arg_rgwu] != arg_rgwu:
            arg_ihhe.par[arg_rgwu] = arg_ihhe.find(arg_ihhe.par[arg_rgwu])
        return arg_ihhe.par[arg_rgwu]

    def func_wrnh(arg_ihhe, arg_rgwu, arg_osiz):
        var_ayzf, var_wnki = arg_ihhe.find(arg_rgwu), arg_ihhe.find(arg_osiz)
        if var_ayzf == var_wnki:
            return
        if arg_ihhe.rnk[var_ayzf] < arg_ihhe.rnk[var_wnki]:
            var_ayzf, var_wnki = var_wnki, var_ayzf
        if arg_ihhe.rnk[var_ayzf] == arg_ihhe.rnk[var_wnki]:
            arg_ihhe.rnk[var_ayzf] += 1
        arg_ihhe.par[var_wnki] = var_ayzf
        arg_ihhe.sz[var_ayzf] += arg_ihhe.sz[var_wnki]

    def func_egyk(arg_ihhe, arg_rgwu):
        return arg_ihhe.sz[arg_ihhe.find(arg_rgwu)]

    def func_dcmd(arg_ihhe):
        return arg_ihhe.size(var_llti(arg_ihhe.sz) - 1) - 1


class Solution(var_zbxo):

    def func_rdmc(arg_ihhe, arg_rjut, arg_lsgw):
        arg_xdvx, arg_rcsn = var_llti(arg_rjut), var_llti(arg_rjut[0])

        def func_cbvh(arg_yjch, arg_dmio):
            return arg_yjch * arg_rcsn + arg_dmio

        def func_ulfl(arg_yjch, arg_dmio):
            for var_lgvi, var_wvuc in ((arg_yjch - 1, arg_dmio), (arg_yjch +
                1, arg_dmio), (arg_yjch, arg_dmio - 1), (arg_yjch, arg_dmio +
                1)):
                if 0 <= var_lgvi < arg_xdvx and 0 <= var_wvuc < arg_rcsn:
                    yield var_lgvi, var_wvuc
        var_tufr = [var_xhfo[:] for var_xhfo in arg_rjut]
        for var_miuw, var_rhvk in arg_lsgw:
            var_tufr[var_miuw][var_rhvk] = 0
        var_yybh = var_bzkm(arg_xdvx, arg_rcsn)
        for arg_yjch, var_xhfo in var_icgs(var_tufr):
            for arg_dmio, var_wkgu in var_icgs(var_xhfo):
                if var_wkgu:
                    var_miuw = func_cbvh(arg_yjch, arg_dmio)
                    if arg_yjch == 0:
                        var_yybh.union(var_miuw, arg_xdvx * arg_rcsn)
                    if arg_yjch and var_tufr[arg_yjch - 1][arg_dmio]:
                        var_yybh.union(var_miuw, func_cbvh(arg_yjch - 1,
                            arg_dmio))
                    if arg_dmio and var_tufr[arg_yjch][arg_dmio - 1]:
                        var_yybh.union(var_miuw, func_cbvh(arg_yjch, 
                            arg_dmio - 1))
        var_pmuo = []
        for arg_yjch, arg_dmio in var_eieh(arg_lsgw):
            var_xrri = var_yybh.top()
            if arg_rjut[arg_yjch][arg_dmio] == 0:
                var_pmuo.append(0)
            else:
                var_miuw = func_cbvh(arg_yjch, arg_dmio)
                for var_lgvi, var_wvuc in func_ulfl(arg_yjch, arg_dmio):
                    if var_tufr[var_lgvi][var_wvuc]:
                        var_yybh.union(var_miuw, func_cbvh(var_lgvi, var_wvuc))
                if arg_yjch == 0:
                    var_yybh.union(var_miuw, arg_xdvx * arg_rcsn)
                var_tufr[arg_yjch][arg_dmio] = 1
                var_pmuo.append(var_xsns(0, var_yybh.top() - var_xrri - 1))
        return var_pmuo[::-1]
