class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_wrnh) ->var_rgwu:
        var_osiz = var_wrnh(arg_xdvx)
        var_ayzf = var_wrnh(arg_rcsn)
        var_wnki = var_egyk(var_ayzf)
        var_osiz = var_osiz.zfill(var_wnki)
        var_dcmd = var_wnki - var_egyk(arg_hqta)

        @var_tufr
        def func_llti(arg_zbxo, arg_rdmc, arg_rjut):
            if arg_zbxo == var_wnki:
                return 1
            var_lsgw = var_rgwu(var_osiz[arg_zbxo]) if arg_rdmc else 0
            var_cbvh = var_rgwu(var_ayzf[arg_zbxo]) if arg_rjut else 9
            var_yjch = 0
            if arg_zbxo < var_dcmd:
                for var_dmio in var_ulfl(var_lsgw, var_lgvi(var_cbvh,
                    arg_bacg) + 1):
                    var_yjch += func_llti(arg_zbxo + 1, arg_rdmc and 
                        var_dmio == var_lsgw, arg_rjut and var_dmio == var_cbvh
                        )
            else:
                var_wvuc = var_rgwu(arg_hqta[arg_zbxo - var_dcmd])
                if var_lsgw <= var_wvuc <= var_lgvi(var_cbvh, arg_bacg):
                    var_yjch = func_llti(arg_zbxo + 1, arg_rdmc and 
                        var_wvuc == var_lsgw, arg_rjut and var_wvuc == var_cbvh
                        )
            return var_yjch
        return func_llti(0, True, True)
