class Solution:
    var_udax = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg, var_hqta = var_rgwu(arg_rcsn), var_rgwu(arg_rcsn[0])
        var_wrnh = {'has_articulation_point': False, 'time': 0}
        var_osiz = 0
        var_ayzf = 0
        var_wnki = [([-1] * var_hqta) for var_egyk in var_dcmd(var_bacg)]
        var_llti = [([-1] * var_hqta) for var_egyk in var_dcmd(var_bacg)]
        var_zbxo = [([-1] * var_hqta) for var_egyk in var_dcmd(var_bacg)]

        def func_rdmc(arg_rjut, arg_lsgw):
            var_wnki[arg_rjut][arg_lsgw] = var_wrnh['time']
            var_wrnh['time'] += 1
            var_llti[arg_rjut][arg_lsgw] = var_wnki[arg_rjut][arg_lsgw]
            var_cbvh = 0
            for var_yjch in arg_xdvx.DIRECTIONS:
                var_dmio = arg_rjut + var_yjch[0]
                var_ulfl = arg_lsgw + var_yjch[1]
                if (0 <= var_dmio < var_bacg and 0 <= var_ulfl < var_hqta and
                    arg_rcsn[var_dmio][var_ulfl] == 1):
                    if var_wnki[var_dmio][var_ulfl] == -1:
                        var_cbvh += 1
                        var_zbxo[var_dmio][var_ulfl
                            ] = arg_rjut * var_hqta + arg_lsgw
                        func_rdmc(var_dmio, var_ulfl)
                        var_llti[arg_rjut][arg_lsgw] = var_lgvi(var_llti[
                            arg_rjut][arg_lsgw], var_llti[var_dmio][var_ulfl])
                        if var_llti[var_dmio][var_ulfl] >= var_wnki[arg_rjut][
                            arg_lsgw] and var_zbxo[arg_rjut][arg_lsgw] != -1:
                            var_wrnh['has_articulation_point'] = True
                    elif var_dmio * var_hqta + var_ulfl != var_zbxo[arg_rjut][
                        arg_lsgw]:
                        var_llti[arg_rjut][arg_lsgw] = var_lgvi(var_llti[
                            arg_rjut][arg_lsgw], var_wnki[var_dmio][var_ulfl])
            if var_zbxo[arg_rjut][arg_lsgw] == -1 and var_cbvh > 1:
                var_wrnh['has_articulation_point'] = True
        for var_wvuc in var_dcmd(var_bacg):
            for var_tufr in var_dcmd(var_hqta):
                if arg_rcsn[var_wvuc][var_tufr] == 1:
                    var_osiz += 1
                    if var_wnki[var_wvuc][var_tufr] == -1:
                        func_rdmc(var_wvuc, var_tufr)
                        var_ayzf += 1
        if var_ayzf == 0 or var_ayzf >= 2:
            return 0
        if var_osiz == 1:
            return 1
        if var_wrnh['has_articulation_point']:
            return 1
        return 2
