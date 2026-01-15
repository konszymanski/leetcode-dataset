from typing import List
import bisect


class SegmentTree:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]):
        arg_ihhe.xs = arg_xdvx
        arg_ihhe.n = var_hqta(arg_xdvx) - 1
        arg_ihhe.count = [0] * (4 * arg_ihhe.n)
        arg_ihhe.covered = [0] * (4 * arg_ihhe.n)

    def func_rgwu(arg_ihhe, arg_wrnh, arg_osiz, arg_ayzf, arg_wnki,
        arg_egyk, arg_dcmd):
        if arg_ihhe.xs[arg_egyk + 1] <= arg_wrnh or arg_ihhe.xs[arg_wnki
            ] >= arg_osiz:
            return
        if arg_wrnh <= arg_ihhe.xs[arg_wnki] and arg_ihhe.xs[arg_egyk + 1
            ] <= arg_osiz:
            arg_ihhe.count[arg_dcmd] += arg_ayzf
        else:
            var_llti = (arg_wnki + arg_egyk) // 2
            arg_ihhe.update(arg_wrnh, arg_osiz, arg_ayzf, arg_wnki,
                var_llti, arg_dcmd * 2 + 1)
            arg_ihhe.update(arg_wrnh, arg_osiz, arg_ayzf, var_llti + 1,
                arg_egyk, arg_dcmd * 2 + 2)
        if arg_ihhe.count[arg_dcmd] > 0:
            arg_ihhe.covered[arg_dcmd] = arg_ihhe.xs[arg_egyk + 1
                ] - arg_ihhe.xs[arg_wnki]
        elif arg_wnki == arg_egyk:
            arg_ihhe.covered[arg_dcmd] = 0
        else:
            arg_ihhe.covered[arg_dcmd] = arg_ihhe.covered[arg_dcmd * 2 + 1
                ] + arg_ihhe.covered[arg_dcmd * 2 + 2]

    def func_zbxo(arg_ihhe):
        return arg_ihhe.covered[0]


class Solution:

    def func_rdmc(arg_ihhe, arg_rjut: var_rcsn[var_rcsn[var_bacg]]) ->var_tcmm:
        var_lsgw = []
        var_cbvh = var_yjch()
        for var_dmio, var_ulfl, var_lgvi in arg_rjut:
            var_lsgw.append((var_ulfl, 1, var_dmio, var_dmio + var_lgvi))
            var_lsgw.append((var_ulfl + var_lgvi, -1, var_dmio, var_dmio +
                var_lgvi))
            var_cbvh.update([var_dmio, var_dmio + var_lgvi])
        arg_xdvx = var_wvuc(var_cbvh)
        var_tufr = var_xhfo(arg_xdvx)
        var_lsgw.sort()
        var_miuw = []
        var_rhvk = []
        var_yybh = 0.0
        var_bzkm = var_lsgw[0][0]
        for var_ulfl, var_icgs, var_wkgu, var_pmuo in var_lsgw:
            var_eieh = var_tufr.query()
            var_yybh += var_eieh * (var_ulfl - var_bzkm)
            var_tufr.update(var_wkgu, var_pmuo, var_icgs, 0, var_tufr.n - 1, 0)
            var_miuw.append(var_yybh)
            var_rhvk.append(var_tufr.query())
            var_bzkm = var_ulfl
        var_xrri = (var_yybh + 1) // 2
        var_xsns = var_mlhe.bisect_left(var_miuw, var_xrri) - 1
        var_qpcy = var_miuw[var_xsns]
        var_bdeu = var_rhvk[var_xsns]
        var_fzvn = var_lsgw[var_xsns][0]
        return var_fzvn + (var_yybh - var_qpcy * 2) / (var_bdeu * 2.0)
