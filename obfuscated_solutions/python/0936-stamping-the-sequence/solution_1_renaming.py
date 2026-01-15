class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta, var_rgwu = var_wrnh(arg_rcsn), var_wrnh(arg_bacg)
        var_osiz = var_ayzf.deque()
        var_wnki = [False] * var_rgwu
        var_egyk = []
        var_dcmd = []
        for var_llti in var_zbxo(var_rgwu - var_hqta + 1):
            var_rdmc, var_rjut = var_lsgw(), var_lsgw()
            for var_cbvh, var_yjch in var_dmio(arg_rcsn):
                var_ulfl = arg_bacg[var_llti + var_cbvh]
                if var_ulfl == var_yjch:
                    var_rdmc.add(var_llti + var_cbvh)
                else:
                    var_rjut.add(var_llti + var_cbvh)
            var_dcmd.append((var_rdmc, var_rjut))
            if not var_rjut:
                var_egyk.append(var_llti)
                for var_cbvh in var_zbxo(var_llti, var_llti + var_wrnh(
                    arg_rcsn)):
                    if not var_wnki[var_cbvh]:
                        var_osiz.append(var_cbvh)
                        var_wnki[var_cbvh] = True
        while var_osiz:
            var_llti = var_osiz.popleft()
            for var_cbvh in var_zbxo(var_lgvi(0, var_llti - var_hqta + 1), 
                var_wvuc(var_rgwu - var_hqta, var_llti) + 1):
                if var_llti in var_dcmd[var_cbvh][1]:
                    var_dcmd[var_cbvh][1].discard(var_llti)
                    if not var_dcmd[var_cbvh][1]:
                        var_egyk.append(var_cbvh)
                        for var_tufr in var_dcmd[var_cbvh][0]:
                            if not var_wnki[var_tufr]:
                                var_osiz.append(var_tufr)
                                var_wnki[var_tufr] = True
        return var_egyk[::-1] if var_xhfo(var_wnki) else []
