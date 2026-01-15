from queue import PriorityQueue


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_xdvx[0])
        var_ayzf = [0] * var_osiz(arg_rcsn)
        var_wnki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var_egyk = var_dcmd([(var_llti, var_zbxo) for var_zbxo, var_llti in
            var_rdmc(arg_rcsn)])
        var_rjut = var_lsgw()
        var_cbvh = [([False] * var_wrnh) for var_yjch in var_dmio(var_rgwu)]
        var_ulfl = 0
        var_rjut.put((arg_xdvx[0][0], 0, 0))
        var_cbvh[0][0] = True
        for var_lgvi, var_wvuc in var_egyk:
            while not var_rjut.empty() and var_rjut.queue[0][0] < var_lgvi:
                var_tufr, var_xhfo, var_miuw = var_rjut.get()
                var_ulfl += 1
                for var_rhvk, var_yybh in var_wnki:
                    var_bzkm, var_icgs = (var_xhfo + var_rhvk, var_miuw +
                        var_yybh)
                    if (var_bzkm >= 0 and var_icgs >= 0 and var_bzkm <
                        var_rgwu and var_icgs < var_wrnh and not var_cbvh[
                        var_bzkm][var_icgs]):
                        var_rjut.put((arg_xdvx[var_bzkm][var_icgs],
                            var_bzkm, var_icgs))
                        var_cbvh[var_bzkm][var_icgs] = True
            var_ayzf[var_wvuc] = var_ulfl
        return var_ayzf
