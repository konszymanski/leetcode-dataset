class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        return arg_xdvx[0] <= arg_rcsn[1] and arg_rcsn[0] <= arg_xdvx[1]

    def func_bacg(arg_ihhe, arg_hqta):
        var_rgwu = var_wrnh.defaultdict(var_osiz)
        for var_ayzf, var_wnki in var_egyk(arg_hqta):
            for var_dcmd in var_llti(var_ayzf + 1, var_zbxo(arg_hqta)):
                if arg_ihhe.overlap(var_wnki, arg_hqta[var_dcmd]):
                    var_rgwu[var_rdmc(var_wnki)].append(arg_hqta[var_dcmd])
                    var_rgwu[var_rdmc(arg_hqta[var_dcmd])].append(var_wnki)
        return var_rgwu

    def func_rjut(arg_ihhe, arg_lsgw):
        var_cbvh = var_yjch(var_dmio[0] for var_dmio in arg_lsgw)
        var_ulfl = var_lgvi(var_dmio[1] for var_dmio in arg_lsgw)
        return [var_cbvh, var_ulfl]

    def func_wvuc(arg_ihhe, var_rgwu, arg_hqta):
        var_tufr = var_xhfo()
        var_miuw = 0
        var_rhvk = var_wrnh.defaultdict(var_osiz)

        def func_yybh(arg_bzkm):
            var_icgs = [arg_bzkm]
            while var_icgs:
                var_dmio = var_rdmc(var_icgs.pop())
                if var_dmio not in var_tufr:
                    var_tufr.add(var_dmio)
                    var_rhvk[var_miuw].append(var_dmio)
                    var_icgs.extend(var_rgwu[var_dmio])
        for var_wkgu in arg_hqta:
            if var_rdmc(var_wkgu) not in var_tufr:
                func_yybh(var_wkgu)
                var_miuw += 1
        return var_rhvk, var_miuw

    def func_pmuo(arg_ihhe, arg_hqta: var_eieh[var_eieh[var_xrri]]) ->var_eieh[
        var_eieh[var_xrri]]:
        var_rgwu = arg_ihhe.buildGraph(arg_hqta)
        var_rhvk, var_xsns = arg_ihhe.getComponents(var_rgwu, arg_hqta)
        return [arg_ihhe.mergeNodes(var_rhvk[var_mlhe]) for var_mlhe in
            var_llti(var_xsns)]
