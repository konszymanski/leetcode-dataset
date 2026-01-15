class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def func_bacg(arg_hqta, arg_rgwu, arg_wrnh):
            var_osiz = var_ayzf(arg_hqta)
            var_osiz[arg_rgwu], var_osiz[arg_wrnh] = var_osiz[arg_wrnh
                ], var_osiz[arg_rgwu]
            return ''.join(var_osiz)
        var_wnki = '123450'
        var_egyk = ''.join(var_dcmd(var_llti) for var_zbxo in arg_xdvx for
            var_llti in var_zbxo)
        var_rdmc = var_rjut()
        var_lsgw = var_cbvh([var_egyk])
        var_rdmc.add(var_egyk)
        var_yjch = 0
        while var_lsgw:
            for var_dmio in var_ulfl(var_lgvi(var_lsgw)):
                var_wvuc = var_lsgw.popleft()
                if var_wvuc == var_wnki:
                    return var_yjch
                var_tufr = var_wvuc.index('0')
                for var_xhfo in var_rcsn[var_tufr]:
                    var_miuw = func_bacg(var_wvuc, var_tufr, var_xhfo)
                    if var_miuw in var_rdmc:
                        continue
                    var_rdmc.add(var_miuw)
                    var_lsgw.append(var_miuw)
            var_yjch += 1
        return -1
