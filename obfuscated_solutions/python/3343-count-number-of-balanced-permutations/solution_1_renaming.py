class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = 10 ** 9 + 7
        arg_xdvx = var_hqta(var_rgwu(var_wrnh, arg_xdvx))
        var_osiz = var_ayzf(arg_xdvx)
        if var_osiz % 2 != 0:
            return 0
        var_wnki = var_osiz // 2
        var_egyk = var_dcmd(arg_xdvx)
        var_llti = var_zbxo(arg_xdvx)
        var_rdmc = (var_llti + 1) // 2
        var_rjut = [0] * 11
        for var_lsgw in var_cbvh(9, -1, -1):
            var_rjut[var_lsgw] = var_rjut[var_lsgw + 1] + var_egyk[var_lsgw]

        @var_bzkm
        def func_yjch(arg_dmio, arg_ulfl, arg_lgvi):
            if arg_lgvi < 0 or var_rjut[arg_dmio
                ] < arg_lgvi or arg_ulfl > var_wnki:
                return 0
            if arg_dmio > 9:
                return var_wrnh(arg_ulfl == var_wnki and arg_lgvi == 0)
            var_wvuc = var_rjut[arg_dmio] - arg_lgvi
            var_tufr = 0
            for var_lsgw in var_cbvh(var_xhfo(0, var_egyk[arg_dmio] -
                var_wvuc), var_miuw(var_egyk[arg_dmio], arg_lgvi) + 1):
                var_rhvk = var_yybh(arg_lgvi, var_lsgw) * var_yybh(var_wvuc,
                    var_egyk[arg_dmio] - var_lsgw) % var_bacg
                var_tufr += var_rhvk * func_yjch(arg_dmio + 1, arg_ulfl + 
                    var_lsgw * arg_dmio, arg_lgvi - var_lsgw)
            return var_tufr % var_bacg
        return func_yjch(0, 0, var_rdmc)
