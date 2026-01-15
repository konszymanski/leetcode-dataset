class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * (var_wrnh + 1)
        for var_wnki in var_egyk(var_wrnh):
            var_dcmd = var_llti(0, var_wnki - arg_rcsn)
            var_zbxo = var_rdmc(var_wrnh, var_wnki + arg_rcsn + 1)
            var_ayzf[var_dcmd] += arg_xdvx[var_wnki]
            var_ayzf[var_zbxo] -= arg_xdvx[var_wnki]

        def func_rjut(arg_lsgw: var_rgwu) ->var_wvuc:
            var_cbvh = var_ayzf.copy()
            var_yjch = 0
            var_dmio = arg_bacg
            for var_wnki in var_egyk(var_wrnh):
                var_yjch += var_cbvh[var_wnki]
                if var_yjch < arg_lsgw:
                    var_ulfl = arg_lsgw - var_yjch
                    if var_dmio < var_ulfl:
                        return False
                    var_dmio -= var_ulfl
                    var_lgvi = var_rdmc(var_wrnh, var_wnki + 2 * arg_rcsn + 1)
                    var_cbvh[var_lgvi] -= var_ulfl
                    var_yjch += var_ulfl
            return True
        var_tufr, var_xhfo = var_rdmc(arg_xdvx), var_miuw(arg_xdvx) + arg_bacg
        var_rhvk = 0
        while var_tufr <= var_xhfo:
            var_yybh = (var_tufr + var_xhfo) // 2
            if func_rjut(var_yybh):
                var_rhvk = var_yybh
                var_tufr = var_yybh + 1
            else:
                var_xhfo = var_yybh - 1
        return var_rhvk
