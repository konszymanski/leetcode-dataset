class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_wrnh,
        arg_bacg: var_osiz[var_wrnh], arg_hqta: var_osiz[var_wrnh],
        arg_rgwu: var_osiz[var_ayzf]) ->var_ayzf:
        var_wnki = [[] for var_egyk in var_dcmd(26)]
        var_llti = var_zbxo(arg_bacg)
        for var_rdmc in var_dcmd(var_llti):
            var_wnki[var_rjut(arg_bacg[var_rdmc]) - var_rjut('a')].append((
                var_rjut(arg_hqta[var_rdmc]) - var_rjut('a'), arg_rgwu[
                var_rdmc]))
        var_lsgw = [arg_ihhe._dijkstra(var_rdmc, var_wnki) for var_rdmc in
            var_dcmd(26)]
        var_cbvh = 0
        for var_yjch, var_dmio in var_ulfl(arg_xdvx, arg_rcsn):
            if var_yjch != var_dmio:
                var_lgvi = var_lsgw[var_rjut(var_yjch) - var_rjut('a')][
                    var_rjut(var_dmio) - var_rjut('a')]
                if var_lgvi == var_wvuc('inf'):
                    return -1
                var_cbvh += var_lgvi
        return var_cbvh

    def func_tufr(arg_ihhe, arg_xhfo: var_ayzf, var_wnki: var_osiz[var_osiz
        [var_miuw]]) ->var_osiz[var_ayzf]:
        var_rhvk = [(0, arg_xhfo)]
        var_yybh = [var_wvuc('inf')] * 26
        while var_rhvk:
            var_bzkm, var_icgs = var_wkgu.heappop(var_rhvk)
            if var_yybh[var_icgs] != var_wvuc('inf'):
                continue
            var_yybh[var_icgs] = var_bzkm
            for var_pmuo, var_eieh in var_wnki[var_icgs]:
                var_xrri = var_bzkm + var_eieh
                if var_yybh[var_pmuo] == var_wvuc('inf'):
                    var_wkgu.heappush(var_rhvk, (var_xrri, var_pmuo))
        return var_yybh
