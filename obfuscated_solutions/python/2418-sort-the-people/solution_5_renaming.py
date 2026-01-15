class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_bacg[var_hqta]:
        arg_ihhe._merge_sort(arg_xdvx, arg_rcsn, 0, var_wrnh(arg_rcsn) - 1)
        return arg_xdvx

    def func_osiz(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu], arg_ayzf: var_rgwu, arg_wnki: var_rgwu):
        if arg_ayzf < arg_wnki:
            var_egyk = arg_ayzf + (arg_wnki - arg_ayzf) // 2
            arg_ihhe._merge_sort(arg_xdvx, arg_rcsn, arg_ayzf, var_egyk)
            arg_ihhe._merge_sort(arg_xdvx, arg_rcsn, var_egyk + 1, arg_wnki)
            arg_ihhe._merge(arg_xdvx, arg_rcsn, arg_ayzf, var_egyk, arg_wnki)

    def func_dcmd(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu], arg_ayzf: var_rgwu, var_egyk: var_rgwu,
        arg_wnki: var_rgwu):
        var_llti = var_egyk - arg_ayzf + 1
        var_zbxo = arg_wnki - var_egyk
        var_rdmc = arg_rcsn[arg_ayzf:arg_ayzf + var_llti]
        var_rjut = arg_rcsn[var_egyk + 1:var_egyk + 1 + var_zbxo]
        var_lsgw = arg_xdvx[arg_ayzf:arg_ayzf + var_llti]
        var_cbvh = arg_xdvx[var_egyk + 1:var_egyk + 1 + var_zbxo]
        var_yjch, var_dmio = 0, 0
        var_ulfl = arg_ayzf
        while var_yjch < var_llti and var_dmio < var_zbxo:
            if var_rdmc[var_yjch] >= var_rjut[var_dmio]:
                arg_rcsn[var_ulfl] = var_rdmc[var_yjch]
                arg_xdvx[var_ulfl] = var_lsgw[var_yjch]
                var_yjch += 1
            else:
                arg_rcsn[var_ulfl] = var_rjut[var_dmio]
                arg_xdvx[var_ulfl] = var_cbvh[var_dmio]
                var_dmio += 1
            var_ulfl += 1
        while var_yjch < var_llti:
            arg_rcsn[var_ulfl] = var_rdmc[var_yjch]
            arg_xdvx[var_ulfl] = var_lsgw[var_yjch]
            var_yjch += 1
            var_ulfl += 1
        while var_dmio < var_zbxo:
            arg_rcsn[var_ulfl] = var_rjut[var_dmio]
            arg_xdvx[var_ulfl] = var_cbvh[var_dmio]
            var_dmio += 1
            var_ulfl += 1
